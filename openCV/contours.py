import cv2 as cv
import numpy as np

# contours using canny

img = cv.imread('Photos\cats.jpg')

cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} this many contours found in the image.')


cv.waitKey(0)