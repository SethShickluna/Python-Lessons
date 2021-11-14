from PIL import Image, ImageFilter 


my_image = Image.open('./images/mountain.jpg')
my_image = my_image.filter(ImageFilter.CONTOUR)

my_image.show()

