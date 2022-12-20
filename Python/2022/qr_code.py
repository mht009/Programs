import os
import qrcode
# from PIL import Image

img = qrcode.make("https://www.geeksforgeeks.org/program-to-find-root-of-an-equations-using-secant-method/")
img.save("qr.png", "PNG")

flags = os.O_RDWR | os.O_CREAT
# os.open("qr.png", flags)
os.system("qr.png")

# image = Image.open(r"qr.png")
# image.show()
