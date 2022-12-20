import cv2 as cv
import numpy as np

img = cv.imread('Photos\cat.jpg')

cv.imshow('Cat', img)

# Converting RGB to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (9, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Casccade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations = 1)
cv.imshow('Dilated Image', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded image', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[:, 300:]
cv.imshow('Cropped Image', cropped)

# Translation
def translation(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> Up
# x --> Right
# y --> Down

translated = translation(img, -100, -100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint= None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow('resized', resized)

# Flipping
flip = cv.flip(img, -1)
# flip = cv.flip(img, 1)
# flip = cv.flip(img, 0)
cv.imshow('flip', flip)



cv.waitKey(0)