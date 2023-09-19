from PIL import Image

def operate_logical_operation(first_image, second_image, operator):
    # Ensure that both images have the same size
    if first_image.size != second_image.size:
        raise ValueError("Images must have the same dimensions")

    # Create a new blank image with the same size
    result_image = Image.new("RGB", first_image.size)
    # Check if the operator is valid
    operators = {
        'AND': logical_and,
        'OR': logical_or,
        'XOR': logical_xor,
    }

    if operator not in operators:
        raise ValueError("Invalid operator. Supported operators are: 'AND', 'OR', 'XOR'")

    # Perform the specified logical operation
    operation_func = operators[operator]

    for x in range(first_image.width):
        for y in range(first_image.height):
            # Get the pixel values at the current position
            triangle_pixel = first_image.getpixel((x, y))
            circle_pixel = second_image.getpixel((x, y))

            # Perform the logical operation on the RGB channels
            result_pixel = operation_func(triangle_pixel, circle_pixel)

            # Set the result pixel in the new image
            result_image.putpixel((x, y), result_pixel)

    return result_image

def operate_logical_not(image):
    # Create a new blank image with the same size
    result_image = Image.new("RGB", image.size)

    for x in range(image.width):
        for y in range(image.height):
            # Get the pixel values at the current position
            pixel = image.getpixel((x, y))

            # Perform the logical operation on the RGB channels
            result_pixel = logical_not(pixel)

            # Set the result pixel in the new image
            result_image.putpixel((x, y), result_pixel)

    return result_image

# Define functions for the logical operators
def logical_and(x, y):
    return (x[0] & y[0], x[1] & y[1], x[2] & y[2])

def logical_or(x, y):
    return (x[0] | y[0], x[1] | y[1], x[2] | y[2])

def logical_xor(x, y):
    return (x[0] ^ y[0], x[1] ^ y[1], x[2] ^ y[2])

def logical_not(x):
    return (255 - x[0], 255 - x[1], 255 - x[2])