from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import glob

print('--------------------------------------------'+
	'\nHello this program is desgined to help the user modify images.'+
	' \nSave and run this program in the same directory as your images\nand enjoy '+
	'the options provided')

image_name = input('--------------------------------------------\n'+
	'To get started enter full image name along with extension: ')
image_info = Image.open(image_name)
print('Image info\nsize: {}'.format(image_info.size)+
	'\nformat: {}'.format(image_info.format)+
	'\nmode: {}'.format(image_info.mode)+
	'\n--------------------------------------------')


print('\nThese are the modification options and acronyms to call during'+
	' the selection process.\n\nAcronym to call: chfm, rsz, rot, mr, fl, bn, flt, bw'+
	'\n\nFull option name: change image format, resize, rotate, '+
	'mirror, flip, brightness, filter and'+
	' \nchange to black and white')
n = 0

option = input('\nwhat do you want to do with the image chosen? to exit enter anything: '+'\n')
if option not in {'chfm', 'rsz', 'rot', 'mr', 'fl', 'bn', 'flt', 'bw'}:
		exit()
while n == 0:

	if option == 'chfm':
		print("Please wait...")
		image = Image.open(image_name)
		new_save = input('Enter the image name with new extension ')
		image.save(new_save) 
		print('Successful!\n')

	elif option == 'rsz':
		image = Image.open(image_name)
		a,b = input('Enter a new pixel size for image separated by a single space i.e. 600,600 ').split()
		resized = Image.open(image_name).resize((int(a),int(b)))
		resized.save('{}{}'.format('resized',image_name))
		print('Successful!\n')
		resized.show()

	elif option == 'rot':
		image = Image.open(image_name)
		d = input('Enter the degrees you\'d like to rotate it by: ')
		print("Please wait...")
		rotated = image.rotate(int(d))
		rotated.save('{}{}'.format('rotated',image_name))
		print('Successful!\n')
		rotated.show()

	elif option == 'fl':
		print("Please wait...")
		image = Image.open(image_name)
		flipped = ImageOps.flip(image)
		flipped.save('{}{}'.format('flipped',image_name))
		print('Successful!\n')
		flipped.show()
		

	elif option == 'mr':
		print("Please wait...")
		image = Image.open(image_name)
		mirrored = ImageOps.mirror(image)
		mirrored.save('{}{}'.format('mirrored',image_name))
		print('Successful!\n')
		mirrored.show()

	elif option == 'bn':
		print("Please wait...")
		b = input('Enter the brightness value you\'d like to add (1 is stock I am float friendly)')
		image = Image.open(image_name)
		brightened = ImageEnhance.Brightness(image).enhance(float(b))
		brightened.save('{}{}'.format('brightened',image_name))
		print('Successful!\n')
		brightened.show()

	elif option == 'bw':
		print("Please wait...")
		image = Image.open(image_name)
		bw = image.convert('L')
		bw.save('{}{}'.format('bw',image_name))
		print('Successful!\n')
		bw.show()

	elif option == 'flt':
		image = Image.open(image_name)
		choice = input('Choose a filter from the given options: blur, contour, edge enhance '+
			'emboss, smooth, sharpen')
		if choice == 'blur':
			print("Please wait...")
			blur = image.filter(ImageFilter.BLUR)
			blur.save('{}{}'.format('blur',image_name))
			print('Successful!\n')
			blur.show()

		elif choice == 'contour':
			print("Please wait...")
			contour = image.filter(ImageFilter.CONTOUR)
			contour.save('{}{}'.format('contoured',image_name))
			print('Successful!\n')
			contour.show()

		elif choice == 'edge enhance':
			print("Please wait...")
			edge = image.filter(ImageFilter.EDGE_ENHANCE)
			edge.save('{}{}'.format('edge',image_name))
			print('Successful!\n')
			edge.show()

		elif choice == 'emboss':
			print("Please wait...")
			emboss = image.filter(ImageFilter.EMBOSS)
			emboss.show('{}{}'.format('edge',image_name))
			print('Successful!\n')
			emboss.show()

		elif choice == 'smooth':
			print("Please wait...")
			smooth = image.filter(ImageFilter.SMOOTH)
			smooth.save('{}{}'.format('smooth',image_name))
			print('Successful!\n')
			smooth.show()

		elif choice == 'sharpen':
			print("Please wait...")
			sharpen = image.filter(ImageFilter.SHARPEN)
			sharpen.save('{}{}'.format('sharpen',image_name))
			print('Successful!\n')
			sharpen.show()

	option = input('Enter another acronym for a new modification. to exit enter anything else: ')
	if option not in {'chfm', 'rsz', 'rot', 'mr', 'fl', 'bn', 'flt', 'bw'}:
		n = 1
		




