from PIL import Image

# Open an image file
test_image = Image.open("marvels-test-image.png").convert("RGB")
print(test_image.format, test_image.size, test_image.mode)


""" 
"""

#function to get pixel values 
def get_pixel_value(image, x, y):
    pixel_value = image.getpixel((x, y))
    return pixel_value
    
print(get_pixel_value(test_image, 10, 30))
"""
"""
#function to convert string to binary
def convert_to_binary(string):
    binary_equivilant = ' '.join(format(ord(char), '08b') for char in string)
    return binary_equivilant

print(convert_to_binary("Hello"))




"""
"""


#function to convert each pixel value to even value using a passed function

def convert_values_to_even(red_value, green_value, blue_value):
    red_value = red_value if red_value % 2 == 0 else red_value - 1
    green_value = green_value if green_value % 2 == 0 else green_value - 1
    blue_value = blue_value if blue_value % 2 == 0 else blue_value - 1
    return red_value, green_value, blue_value



    
#function to iterate over each pixel in an image and apply a function
def process_image(image):
    width, height = image.size
    for y_position in range(height):
        for x_position in range(width):
            red_value, green_value, blue_value = image.getpixel((x_position, y_position))
            
            #skip black pixels and also avoid unnecessary processing plus encodes on only colored pixels later on
            if red_value==0 and green_value==0 and blue_value==0:
                continue 
            #skip white pixels
            if red_value==255 and green_value==255 and blue_value==255:
                continue
            
            #converts the pixel values
            red_value, green_value, blue_value = convert_values_to_even(red_value, green_value, blue_value)
            
            #still deciding whether to update the image or not
            #image.putpixel((x_position, y_position), (red_value, green_value, blue_value))

            print(f"Pixel at ({x_position}, {y_position}): R={red_value}, G={green_value}, B={blue_value}")

process_image(test_image)