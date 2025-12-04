from PIL import Image
import numpy



def get_even_image_array(image_array):
	return image_array - image_array % 2


def convert_text_to_binary(message):
	#return "".join([bin(ord(char))[2:].zfill(21) for char in message])
	
	list_of_bits = []
	for char in message:
		ordinal_char = ord(char)
		binary_char = bin(ordinal_char)[2:]
		binary_paded_char = binary_char.zfill(21)

		list_of_bits.append(binary_paded_char)
	
	return  "".join(list_of_bits)



def watermark_image(image_array, message):
	even_image_array = get_even_image_array(image_array)
	binary_message = convert_text_to_binary(message)

	number_rows, number_cols, number_canals = image_array.shape

	if len(binary_message) > number_rows * number_cols * number_canals:
		print("Attention le message est trop long !")

	index_bit = 0

	for row in range(0, number_rows):
		for col in range(0, number_cols):
			for canal in range(0, number_canals):
				if index_bit == len(binary_message):
					break
				else:
					even_image_array[row][col][canal] += int(binary_message[index_bit])
					index_bit += 1 


	Image.fromarray(even_image_array).save('image_watermarked.png')




def decode_watermark(image_array):
    

    image_code=image_array % 2
    string_image_code = ''.join(str(bit) for bit in image_code.flatten())

    
    chars = []
    for i in range(0, len(string_image_code), 21):
        byte_str = string_image_code[i:i+21]
        char = chr(int(byte_str, 2))  
        if char == '\x00':  # Stop at null character    
            break
        chars.append(char)
		
        message=''.join(chars)
    print("Decoded message:", message)




image = Image.open("./marvels-test-image.png").convert("RGB")
image_array = numpy.array(image)

watermark_image(image_array, message="chocolat")
image2 = Image.open("./image_watermarked.png").convert("RGB")
image_array_crypted = numpy.array(image2)
decode_watermark(image_array_crypted)

# number_rows, number_cols, number_canals = image_array.shape

# for row in range(number_rows):
# 	for col in range(number_cols):
# 		print(image_array[row][col])
