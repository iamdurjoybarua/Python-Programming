from PIL import Image

def resize_image(input_path, output_path, new_size):
    try:
        with Image.open(input_path) as img:
            # Resize the image using the ANTIALIAS filter for quality
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
            resized_img.save(output_path)
            print(f"Image resized successfully and saved to '{output_path}'")
    except FileNotFoundError:
        print(f"Error: The file at '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: resize 'my_photo.jpg' to 300x200 and save it as 'my_photo_resized.jpg'
input_file = "my_photo.jpg"  # Make sure this file exists in the same directory
output_file = "my_photo_resized.jpg"
new_dimensions = (300, 200)

resize_image(input_file, output_file, new_dimensions)