from PIL import Image

# Open an image file
im = Image.open("marvels-test-image.png")
print(im.format, im.size, im.mode)


""" 
"""

#function to get pixel values 
def get_pixel_value(image, x, y):
    pixel_value = image.getpixel((x, y))
    return pixel_value
    
print(get_pixel_value(im, 10, 30))
"""
"""
#function to convert string to binary
def convert_to_binary(string):
    binary_equivilant = ' '.join(format(ord(char), '08b') for char in string)
    return binary_equivilant

print(convert_to_binary("Hello"))




