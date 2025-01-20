import os
from PIL import Image

def resize_and_add_canvas(input_image_path, output_image_path):
    # Open the input image
    with Image.open(input_image_path) as img:
        # Convert the image to RGBA to ensure it has an alpha channel
        img = img.convert("RGBA")
        
        # Calculate the new dimensions to resize height to 768 while maintaining aspect ratio
        aspect_ratio = img.width / img.height
        new_height = 768
        new_width = int(new_height * aspect_ratio)
        
        # Resize the image with LANCZOS for high-quality downsampling
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Create a transparent canvas of the desired size (2133x1280)
        canvas_width, canvas_height = 2133, 1280
        canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
        
        # Calculate the position to center the resized image on the canvas
        # x_offset = (canvas_width - new_width) // 2
        # y_offset = (canvas_height - new_height) // 2
        x_offset = (canvas_width - new_width) *0
        y_offset = (canvas_height - new_height) *0
        
        # Paste the resized image onto the transparent canvas
        canvas.paste(resized_img, (x_offset, y_offset), resized_img)
        
        # Save the result
        canvas.save(output_image_path, "PNG")

def process_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        # Check if the file is an image
        if os.path.isfile(input_path) and filename.lower().endswith(('png', 'jpg', 'jpeg')):
            output_path = os.path.join(output_folder, filename)
            resize_and_add_canvas(input_path, output_path)
            print(f"Processed: {filename}")

# Example usage
input_folder = "images"  # Replace with your folder containing images
output_folder = "resized"  # Folder to save resized images
process_folder(input_folder, output_folder)
