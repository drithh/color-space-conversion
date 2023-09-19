
from PIL import Image

def convert_rgb_to_grayscale(image):
    # Create a new image in grayscale mode
    grayscale_image = Image.new("L", image.size)

    # Convert each pixel to grayscale using the luminance formula
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            # Calculate grayscale value
            gray_value = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            grayscale_image.putpixel((x, y), gray_value)

    return grayscale_image
  
  
def convert_grayscale_to_binary(image):
    # Create a new image in binary mode (1-bit)
    binary_image = Image.new("1", image.size)

    # Iterate through each pixel and apply the threshold (128)
    for x in range(image.width):
        for y in range(image.height):
            pixel_value = image.getpixel((x, y))
            if pixel_value >= 128:
                binary_image.putpixel((x, y), 1)  # White
            else:
                binary_image.putpixel((x, y), 0)  # Black

    return binary_image