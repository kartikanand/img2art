import shutil
import sys

from PIL import Image


def get_term_width():
	""" return terminal width
		this function depends upon shutil.get_terminal_size
		this works only on Python >= 3.3
	"""

	return shutil.get_terminal_size().columns


def get_aspect_ratio(img):
	""" return the aspect ratio of given image
		ar = width//height
		return an int, we don't care about exact ratios
	"""

	width, height = img.size

	aspect_ratio = width//height
	if aspect_ratio == 0:
		aspect_ratio = 1

	return aspect_ratio


def get_height(width, aspect_ratio):
	""" return height with respect to given aspect ratio """
	
	return width//aspect_ratio


def resize_img(img):
	""" return a resized image
	    resize acc. to given terminal width
	    keeping in mind the original aspect ratio
	"""

	term_width = get_term_width()

	# divide by 2 because we use 2 characters per pixel
	width = term_width//2
	aspect_ratio = get_aspect_ratio(img)
	height = get_height(width, aspect_ratio)

	return img.resize((width, height))


def draw_ascii(img):
	""" draw ascii art from the provided image
		use # for black
		use . for white

		before drawing, convert the image to black and white
		then resize it according to terminal width
	"""

	# convert image to black and white
	img = img.convert('L')

	# resize image to match terminal width and aspect ratio
	img = resize_img(img)

	width, height = img.size
	for y in range(height):
		for x in range(width):
			if img.getpixel((x, y)) < 15:
				print('# ', end='')
			else:
				print('. ', end='')
		print()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Please enter an image name as argument')
		sys.exit(1)

	img_file = sys.argv[1]
	try:
		img = Image.open(img_file)
		draw_ascii(img)
	except IOError:
		print('Enter correct file')
		sys.exit(1)
