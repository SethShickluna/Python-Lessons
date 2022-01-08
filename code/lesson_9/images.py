from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw

import random

my_image = Image.open("C:/Users/seths/Documents/tutoring/Python-Lessons/code/lesson_9/newimage.jpg")
#my_image = Image.new(mode="RGB", size=(600, 400), color=(40, 70, 190))


def image_stuff():
    # filtering images
    filtered = ImageFilter.MaxFilter(my_image)
    # call filtered.show() to see our image

    # enhancing images
    enhancer = ImageEnhance.Color(my_image)
    enhancer.enhance(1.5).show()


def pixel_stuff():
    pixels = my_image.load()
    width, height = my_image.size

    for i in range(width):
        for j in range(height):
            r, g, b = my_image.getpixel((i, j))

            grayscale = (0.299 * r + 0.587 * g + 0.114 * b)
            pixels[i, j] = (int(grayscale), int(grayscale), int(grayscale))

    my_image.show()


def draw_image():
    width, height = my_image.size

    drawer = ImageDraw.Draw(my_image)
    # there are lots of different shapes available
    drawer.ellipse((25, 25, 100, 100), fill="yellow", outline=None)

    drawer.rectangle((0, height - 100, width, height), fill="green")

    my_image.show()


pixel_stuff()

