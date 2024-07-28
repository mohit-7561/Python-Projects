import os
from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    try:
        # Load the input image
        input_image = Image.open(input_path)

        # Remove the background
        output_image = remove(input_image)

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the output image
        output_image.save(output_path)
        print(f"Output saved at {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_image_path = 'BG Remover/images/animal.jpg'
output_image_path = 'BG Remover/output/bg_removed.png'
remove_background(input_image_path, output_image_path)
