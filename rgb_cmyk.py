from PIL import Image

def convert_rgb_to_cmyk(image):
    width, height = image.size
    cmyk_image = Image.new('CMYK', (width, height))
    for i in range(width):
        for j in range(height):
            r, g, b = image.getpixel((i, j))
            c, m, y, k = rgb_to_cmyk(r, g, b)

            # Scale the CMYK values back to the range [0, 255]
            c = int(c * 255 / 100)
            m = int(m * 255 / 100)
            y = int(y * 255 / 100)
            k = int(k * 255 / 100)

            cmyk_image.putpixel((i, j), (c, m, y, k))
    
    return cmyk_image

def rgb_to_cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        # black
        return 0, 0, 0, 100

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255

    # extract out k [0, 1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy

    # rescale to the range [0, 100]
    return c * 100, m * 100, y * 100, k * 100

def remove_cmyk_attribute(image, input_c=False, input_m=False, input_y=False, input_k=False):
    width, height = image.size
    cyan_image = Image.new('CMYK', (width, height))
    for i in range(width):
        for j in range(height):
            c, m, y, k = image.getpixel((i, j))
            c = 0 if input_c is not False else c
            m = 0 if input_m is not False else m
            y = 0 if input_y is not False else y
            k = 0 if input_k is not False else k
            
            cyan_image.putpixel((i, j), (c, m, y, k))
    
    return cyan_image