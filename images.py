# from __future__ import print_function
from PIL import Image
obraz = input("Въведи име на файл. Може и биз разширението, ако го няма: ")
im = Image.open(obraz)   # obraz is foto file in current directory
print(im.format, im.size, im.mode)

im.show()
