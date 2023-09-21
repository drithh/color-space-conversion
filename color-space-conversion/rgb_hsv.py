from PIL import Image

def convert_rgb_to_hsv(image):
    width, height = image.size
    hsv_image = Image.new('HSV', (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            h, s, v = rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
            # Convert values to 0-255 range for HSV
            h = int(h * 255)
            s = int(s * 255)
            v = int(v * 255)
            hsv_image.putpixel((x, y), (h, s, v))
    
    return hsv_image

def rgb_to_hsv(r, g, b):
    # Find the maximum, minimum, and range of RGB values
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    range_value = max_value - min_value
    
    # Calculate the value component (V) of HSV
    v = max_value
    
    # Check if it's a grayscale color (no saturation)
    if min_value == max_value:
        return 0.0, 0.0, v
    
    # Calculate the saturation component (S) of HSV
    s = range_value / max_value
    
    # Calculate the hue component (H) of HSV
    rc = (max_value - r) / range_value
    gc = (max_value - g) / range_value
    bc = (max_value - b) / range_value
    
    if r == max_value:
        h = bc - gc
    elif g == max_value:
        h = 2.0 + rc - bc
    else:
        h = 4.0 + gc - rc
    
    # Normalize the hue to be in the range [0, 1]
    h = (h / 6.0) % 1.0
    
    return h, s, v


def adjust_hsv(image, delta_h=0, delta_s=0, delta_v=0):
    width, height = image.size
    adjusted_hsv_image = Image.new('HSV', (width, height))

    for x in range(width):
        for y in range(height):
            h, s, v = image.getpixel((x, y))

            converted_delta_h = int(delta_h * 255 / 360)
            converted_delta_s = int(delta_s * 255 / 100)
            converted_delta_v = int(delta_v * 255 / 100)
            
            h = (h + converted_delta_h) % 256
            s = max(0, min(255, s + converted_delta_s))
            v = max(0, min(255, v + converted_delta_v))

            adjusted_hsv_image.putpixel((x, y), (h, s, v))

    return adjusted_hsv_image

def set_hsv(image, input_h=None, input_s=None, input_v=None):
    width, height = image.size
    adjusted_hsv_image = Image.new('HSV', (width, height))

    for x in range(width):
        for y in range(height):
            h, s, v = image.getpixel((x, y))

            converted_h = int(input_h if input_h is not None else h* 255 / 360)
            converted_s = int(input_s if input_s is not None else s * 255 / 100)
            converted_v = int(input_v if input_v is not None else v * 255 / 100)
            
            h = converted_h % 256
            s = max(0, min(255, converted_s))
            v = max(0, min(255, converted_v))

            adjusted_hsv_image.putpixel((x, y), (h, s, v))

    return adjusted_hsv_image