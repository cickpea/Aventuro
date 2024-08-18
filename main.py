import gradio as gr
import os
import csv
from dotenv import load_dotenv
from transformers import pipeline
import re
import torch
from PIL import Image
import numpy as np

def img2text(url):
    device = 0 if torch.cuda.is_available() else -1
    image_to_text = pipeline("image-to-text", model="AdamCodd/donut-receipts-extract", device=device)
    text = image_to_text(url)[0]["generated_text"]
    return text

def parse_items(text):
    item_pattern = re.compile(r'<s_item_name>(.*?)</s_item_name>.*?<s_item_value>(.*?)</s_item_value>', re.DOTALL)
    items = item_pattern.findall(text)
    return items

def save_to_csv(items, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item Name', 'Item Price'])
        writer.writerows(items)

def process_image(image):
    # Debugging statement to verify input
    print(f"Image: {image}")

    # Determine the type of image provided
    if isinstance(image, str):
        # Image is a file path
        image_path = image
    elif isinstance(image, np.ndarray):
        # Image is a NumPy array (webcam image)
        pil_image = Image.fromarray(image)
        # Save the image to a temporary file
        temp_image_path = os.path.join(os.getcwd(), "temp_image.png")
        pil_image.save(temp_image_path)
        print(f"Image saved to {temp_image_path}")  # Debugging statement
        image_path = temp_image_path
    else:
        raise ValueError("Unsupported image type")

    return image_path

# Create Gradio interface
iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(sources=["upload"], type="filepath"),
    outputs=["text", "file"]
)

iface.launch(share=True)