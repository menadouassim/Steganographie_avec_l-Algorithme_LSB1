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

#function to to turn each pixel value in a picture into even value
def convert_image_values_to_even_numbers(image):
    pixels = image.load()
    width, height = image.size
    for y_position in range(height):
        for x_position in range(width):
            red_value, green_value, blue_value = pixels[x_position, y_position]

            # Convert each color to an even value
            red_value = red_value if red_value % 2 == 0 else red_value - 1
            green_value = green_value if green_value % 2 == 0 else green_value - 1
            blue_value = blue_value if blue_value % 2 == 0 else blue_value - 1
            pixels[x_position, y_position] = (red_value, green_value, blue_value)

            modified_image=image.save("even_image.png")
    return modified_image

convert_image_values_to_even_numbers(test_image)