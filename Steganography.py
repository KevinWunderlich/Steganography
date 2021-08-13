import hashlib
from PIL import Image

def encode(img, msg):
	length = len(msg)
	encoded = img.copy()
	width, height = img.size
	i = 0
	
	for row in range(height):
		for col in range(width):
			r, g, b = img.getpixel((col, row))
			if row == 0 and col == 0 and i < length:
				ascii = length
			elif i <= length:
				c = msg[i-1]
				ascii = ord(c)
			else:
				ascii = r
			encoded.putpixel((col, row), (ascii, g, b))
			i += 1
	return encoded
	
def decode(img):
	width, height = img.size
	msg = ""
	i = 0
	for row in range(height):
		for col in range(width):
			r, g, b = img.getpixel((col, row))	
			if row == 0 and col == 0:
				length = r
			elif i <= length:
				msg += chr(r)
			i += 1
	return msg

def main():
	og_img = raw_input("Enter image file name, including extension: ")

	img = Image.open(og_img)

	image = open(og_img).read()
	hash = hashlib.md5(image).hexdigest()
	print "Hash value of original image is: " + hash

	message = raw_input("Enter secret message to be encoded: ")

	enc_img_file = "enc_" + og_img
	img_encoded = encode(img, message)
	img_encoded.save(enc_img_file)
	
	image2 = open(enc_img_file).read()
	hash2 = hashlib.md5(image2).hexdigest()
	print "Hash value of encoded image is: " + hash2

	ans = raw_input("Would you like to decode the message? Y/N ")

	if ans == 'Y' or ans == 'y':
		img2 = Image.open(enc_img_file)
		hidden_msg = decode(img2)
		print "The decoded message is: " + hidden_msg
	else:
		print "Goodbye!"
		
if __name__ == '__main__':
	main()

