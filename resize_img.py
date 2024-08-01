from PIL import Image


def crop_image_to_ratio(input_path, output_path, width_ratio = 5, height_ratio = 6):
    # Open the image
    image = Image.open(input_path)
    width, height = image.size
    
    # Calculate the new dimensions based on the specified ratio
    if width / height > width_ratio / height_ratio:
        # Image is too wide, adjust width
        new_width = int(height * (width_ratio / height_ratio))
        new_height = height
    else:
        # Image is too tall, adjust height
        new_width = width
        new_height = int(width * (height_ratio / width_ratio))
    
    # Calculate the cropping box (left, upper, right, lower)
    left = (width - new_width) // 2
    upper = (height - new_height) // 2
    right = left + new_width
    lower = upper + new_height
    
    # Crop the image
    cropped_image = image.crop((left, upper, right, lower))
    
    # Save the cropped image
    cropped_image.save(output_path)

def resize_image(input_path, output_path, width=500, height=600):
    # Open an image file
    with Image.open(input_path) as img:
        # Resize the image
        resized_img = img.resize((width, height))
        # Save the resized image
        resized_img.save(output_path)
        print(f"Image resized to {width}x{height} and saved as {output_path}")

# Example usage:
input_path = 'img/team-AdityaKesari.jpeg'  # Replace with your input image path
output_path = 'img/team-AdityaKesari.jpeg'  # Replace with your desired output image path
crop_image_to_ratio(input_path, output_path, 5, 6)
resize_image(input_path, input_path, 500, 600)
