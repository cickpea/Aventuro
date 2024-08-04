def process_image(upload_image, webcam_image):
    # Debugging statements to verify inputs
    print(f"Upload Image: {upload_image}")
    print(f"Webcam Image: {webcam_image}")

    # Determine which image is provided
    if upload_image is not None:
        image_path = upload_image
    elif webcam_image is not None:
