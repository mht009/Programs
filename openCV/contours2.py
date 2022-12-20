# contours2.py using threshold
import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.50):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

# opening original image
imgOrg = cv.imread('Photos\grid_1.png')

# rescaling the image as it is much bigger
img = rescaleFrame(imgOrg, 0.50)
# img = imgOrg

# showing the image
cv.imshow('Image', img)


# creating a blank image
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)


# Converting the image to gray in order to use the threshold
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# getting threshold
ret, thresh = cv.threshold(gray, 50, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# finding contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} this many contours found')

# drawing contours
cv.drawContours(img, contours, -1, (0, 255, 0), 1)
cv.imshow('Contours drawn', img)

for i in contours:
    print(i)

cv.waitKey(0)