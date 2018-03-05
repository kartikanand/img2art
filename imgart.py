from PIL import Image

im = Image.open('sample.bmp')
im = im.resize((32, 32))

width, height = im.size

for y in range(height):
	for x in range(width):
		if im.getpixel((x, y)) < 15:
			print('# ', end='')
		else:
			print('. ', end='')
	print()
