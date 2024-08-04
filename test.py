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
    if isinstance(image, np.ndarray):
        # Convert NumPy array to PIL Image
        pil_image = Image.fromarray(image)
        # Save the image to a temporary file
        temp_image_path = os.path.join(os.getcwd(), "temp_image.png")
        pil_image.save(temp_image_path)
        image_path = temp_image_path
    else:
        # Assume the image is already a file path
        image_path = image

    extracted_text = img2text(image_path)
    items = parse_items(extracted_text)
    csv_filename = os.path.join(os.getcwd(), "extracted_items.csv")
    save_to_csv(items, csv_filename)
    
    # Read the CSV file and return its contents as a string
    with open(csv_filename, 'r') as file:
        csv_contents = file.read()
    
    return csv_contents, csv_filename

# Create Gradio interface
iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(mirror_webcam=False , type="numpy"),
    outputs=["text", "file"]
)

iface.launch(share=True)