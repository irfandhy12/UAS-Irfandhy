import stepic
from PIL import Image

print("----------------------")

text = input(" DATA ")
file = input("  PHOTO  ")

img = Image.open(file)
img_stegano = stepic.encode(img, text.encode)

img_stegano.save("stegano.png")

print("---------------")

input("  COMPLETE (press enter -> exit)")
