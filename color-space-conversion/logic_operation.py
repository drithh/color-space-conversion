from PIL import Image
from rgb_grayscale_binary import convert_rgb_to_grayscale

def operate_logical_operation(first_image, second_image, operator):
    # Ensure that both images have the same size
    if first_image.size != second_image.size:
        raise ValueError("Images must have the same dimensions")

    # Create a new blank image with the same size
    result_image = Image.new("1", first_image.size)
    # Check if the operator is valid
    operators = {
        'AND': logical_and,
        'OR': logical_or,
        'XOR': logical_xor,
        'NAND': logical_nand,
        'NOR': logical_nor,
        'XNOR': logical_xnor
    }

    if operator not in operators:
        raise ValueError("Invalid operator. Supported operators are: 'AND', 'OR', 'XOR'")

    # Perform the specified logical operation
    operation_func = operators[operator]
    
    grayscale_first_image = convert_rgb_to_grayscale(first_image)
    grayscale_second_image = convert_rgb_to_grayscale(second_image)

    for x in range(grayscale_first_image.width):
        for y in range(grayscale_second_image.height):
            # Get the pixel values at the current position
            triangle_pixel = grayscale_first_image.getpixel((x, y))
            circle_pixel = grayscale_second_image.getpixel((x, y))

            # Perform the logical operation on the RGB channels
            # convert to binary
            triangle_pixel = 0 if triangle_pixel > 128 else 1
            circle_pixel = 0 if circle_pixel else 1
            
            # perform the logical operation
            result_pixel = operation_func(triangle_pixel, circle_pixel)

            # Set the result pixel in the new image
            result_image.putpixel((x, y), result_pixel)

    return result_image

def operate_logical_not(image):
    # Create a new blank image with the same size
    result_image = Image.new("1", image.size)

    grayscale_image = convert_rgb_to_grayscale(image)
    
    for x in range(grayscale_image.width):
        for y in range(grayscale_image.height):
            # Get the pixel values at the current position
            pixel = grayscale_image.getpixel((x, y))

            pixel = 0 if pixel > 128 else 1
            
            # Perform the logical operation on the RGB channels
            result_pixel = logical_not(pixel)

            # Set the result pixel in the new image
            result_image.putpixel((x, y), result_pixel)

    return result_image

# Define functions for the logical operators
def logical_and(x, y):
    return 0 if (x & y == 1) else 1

def logical_or(x, y):
    return 0 if (x | y == 1) else 1

def logical_xor(x, y):
    return 0 if (x ^ y == 1) else 1

def logical_not(x):
    return 0 if (x == 0) else 1

def logical_nand(x, y):
    return 0 if logical_not(logical_and(x, y)) else 1

def logical_nor(x, y):
    return 0 if logical_not(logical_or(x, y)) else 1

def logical_xnor(x, y):
    return 0 if logical_not(logical_xor(x, y)) else 1



