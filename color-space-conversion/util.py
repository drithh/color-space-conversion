from math import sqrt
from PIL import Image

def display_image(images, columns=None, rows=None):
    image_width, image_height = images[0].size
    columns = columns or int(sqrt(len(images)))
    rows = rows or columns
    
    # Create a new image that will contain the images side by side
    combined_image = Image.new("RGB", (image_width * columns, image_height * rows))
    x_offset = 0
    y_offset = 0
    for i, result in enumerate(images):
        combined_image.paste(result, (x_offset, y_offset))

        x_offset += image_width
        if (i + 1) % columns == 0:
            x_offset = 0
            y_offset += + image_height
    # Save or display the combined image
    return combined_image
  
  