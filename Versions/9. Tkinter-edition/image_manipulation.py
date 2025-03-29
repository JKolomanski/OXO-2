from PIL import Image


def color_symbol_image(symbol: str, color: str) -> Image:
    """
    Get the image for the given symbol in a given color

    :param symbol: The symbol of the image to convert X/O
    :param color: The hex value of the needed color

    :returns: An Image object of the correct color
    """
    color = hex_to_rgb(color)
    image = Image.open(f'Assets/{symbol}_symbol_grayscale.png')
    imagedata = list(image.getdata())
    new_imagedata = []
    for i in range(len(imagedata)):
        new_imagedata.append((color[0], color[1], color[2], imagedata[i][3]))

    colored_image = Image.new('RGBA', (image.width, image.height))
    colored_image.putdata(new_imagedata)
    return colored_image


def hex_to_rgb(hex_val: str) -> tuple:
    """
    Convert a hex color value to rgb

    :param hex_val: The hex color value
    :returns: A tuple of 3 RGB color values
    """
    hex_val = hex_val.lstrip('#')
    return tuple(int((hex_val[i:i+2]), 16) for i in (0, 2, 4))