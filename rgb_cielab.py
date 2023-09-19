import math
from PIL import Image


def convert_rgb_to_cielab(image):
    width, height = image.size
    cielab_image = Image.new('LAB', (width, height))
    for i in range(width):
        for j in range(height):
            r, g, b = image.getpixel((i, j))
            lab_L, lab_a, lab_b = rgb_to_cielab(r, g, b)

            # Scale the LAB values back to the range [0, 255]
            L = int(lab_L * 255 / 100)
            a = int(lab_a + 128)
            b = int(lab_b + 128)

            cielab_image.putpixel((i, j), (L, a, b))
    
    return cielab_image

import math

def rgb_to_cielab(r, g, b):
    r, g, b = float(r) / 255, float(g) / 255, float(b) / 255

    if r > 0.04045:
        r = ((r + 0.055) / 1.055) ** 2.4
    else:
        r = r / 12.92

    if g > 0.04045:
        g = ((g + 0.055) / 1.055) ** 2.4
    else:
        g = g / 12.92

    if b > 0.04045:
        b = ((b + 0.055) / 1.055) ** 2.4
    else:
        b = b / 12.92

    r, g, b = r * 100, g * 100, b * 100

    X = r * 0.4124 + g * 0.3576 + b * 0.1805
    Y = r * 0.2126 + g * 0.7152 + b * 0.0722
    Z = r * 0.0193 + g * 0.1192 + b * 0.9505

    X = round(X, 4)
    Y = round(Y, 4)
    Z = round(Z, 4)

    X = float(X) / 94.811
    Y = float(Y) / 100.0
    Z = float(Z) / 108.883

    if X > 0.008856:
        X = math.pow(X, 1.0 / 3)
    else:
        X = (7.787 * X) + (16 / 116)

    if Y > 0.008856:
        Y = math.pow(Y, 1.0 / 3)
    else:
        Y = (7.787 * Y) + (16 / 116)

    if Z > 0.008856:
        Z = math.pow(Z, 1.0 / 3)
    else:
        Z = (7.787 * Z) + (16 / 116)

    L = (116 * Y) - 16
    a = 500 * (X - Y)
    b = 200 * (Y - Z)

    L = round(L, 5)
    a = round(a, 5)
    b = round(b, 5)
    
    return L, a, b

def set_cielab(image, input_L=None, input_a=None, input_b=None):
    width, height = image.size
    adjusted_cielab_image = Image.new('LAB', (width, height))

    for x in range(width):
        for y in range(height):
            L, a, b = image.getpixel((x, y))

            converted_L = int(input_L * 255 / 100 if input_L is not None else L)
            converted_a = int(input_a + 128 if input_a is not None else a)
            converted_b = int(input_b + 128 if input_b is not None else b)
            
            adjusted_cielab_image.putpixel((x, y), (converted_L, converted_a, converted_b))

    return adjusted_cielab_image