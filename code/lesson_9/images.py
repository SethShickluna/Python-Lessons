from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw

import random

# my_image = Image.open("C:/Users/seths/Documents/tutoring/Python-Lessons/code/lesson_9/newimage.jpg")
my_image = Image.new(mode="RGB", size=(600, 400), color=(40, 70, 190))


def image_stuff():
    # filtering images
    filtered = ImageFilter.MaxFilter(my_image)
    # call filtered.show() to see our image

    # enhancing images
    enhancer = ImageEnhance.Color(my_image)
    enhancer.enhance(1.5).show()


def pixel_stuff():
    pixels = my_image.load()
    width, height = my_image.size  # this is important so we dont access pixels that dont exist

    for i in range(width):  # integer division (//) so it is an int, not a float
        for j in range(height):
            # getting the rgb value of a pixel image.getpixel((x, y))
            r, g, b, a = my_image.getpixel((i, j))  # a is opacity (transparency), dont worry about it
            # you can use these r, g, b values as the color of the current pixel

            x = width - i - 1
            y = j

            pixels[x, y] = pixels[i, j]

    my_image.show()


def draw_image():
    width, height = my_image.size

    drawer = ImageDraw.Draw(my_image)
    # there are lots of different shapes available
    drawer.ellipse((25, 25, 100, 100), fill="yellow", outline=None)

    drawer.rectangle((0, height - 100, width, height), fill="green")

    my_image.show()




