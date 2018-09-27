from pdf2image import convert_from_path
pages = convert_from_path('resources/test.pdf')

def convertPDF2JPG():
	counter = 0
	for page in pages:
		if counter == 0:
			page.save('images/out.jpg', 'JPEG')
			counter = 1
		else:
			break

convertPDF2JPG()

