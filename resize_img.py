from PIL import Image

def resize_image(input_path, output_path, width=500, height=600):
    # Open an image file
    with Image.open(input_path) as img:
        # Resize the image
        resized_img = img.resize((width, height))
        # Save the resized image
        resized_img.save(output_path)
        print(f"Image resized to {width}x{height} and saved as {output_path}")

# Example usage:
input_path = 'img/team-TaqiyaEhsan.jpg'  # Replace with your input image path
output_path = 'img/team-TaqiyaEhsan.jpg'  # Replace with your desired output image path
resize_image(input_path, output_path)
