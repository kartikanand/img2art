from PIL import Image

im = Image.open('sample.bmp')
im = im.resize((16, 16))

width, height = im.size

for y in range(height):
	for x in range(width):
		d = im.getpixel((x, y))
		print('{:2} '.format(d), end='')
		#if im.getpixel((x, y)) < 15:
		#	print('.', end='')
	print('\n')
