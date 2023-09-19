from PIL import Image

def rgb_to_yiq(r, g, b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    i = 0.596 * r - 0.274 * g - 0.322 * b
    q = 0.211 * r - 0.523 * g + 0.312 * b
    return y, i, q

def yiq_to_rgb(y, i, q):
    r = y + 0.956 * i + 0.621 * q
    g = y - 0.272 * i - 0.647 * q
    b = y - 1.106 * i + 1.703 * q

    return r, g, b


def convert_rgb_to_yiq(image):
    width, height = image.size
    yiq_image = Image.new('RGB', (width, height))

    for x in range(width):
        for z in range(height):
            r, g, b = image.getpixel((x, z))
            y, i, q = rgb_to_yiq(r, g, b)
            
            
            # Convert Y, I, Q values so it can display on the image
            r, g, b = (yiq_to_rgb(y, i, q))
            # Set the RGB values as pixel values in the new image
            yiq_image.putpixel((x, z), (int(r), int(g), int(b)))

    return yiq_image

def remove_yiq_attributes(image, input_y=False, input_i=False, input_q=False):
    width, height = image.size
    yiq_image = Image.new('RGB', (width, height))

    for x in range(width):
        for z in range(height):
            r, g, b = image.getpixel((x, z))
            y, i, q = rgb_to_yiq(r, g, b)
            
            y = y if input_y else 0
            i = i if input_i else 0
            q = q if input_q else 0
            
            # Convert Y, I, Q values so it can display on the image
            r, g, b = (yiq_to_rgb(y, i, q))
            # Set the RGB values as pixel values in the new image
            yiq_image.putpixel((x, z), (int(r), int(g), int(b)))

    return yiq_image