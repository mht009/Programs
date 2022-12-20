import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# plt.imshow(img)
# plt.show()

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# converting to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV_FULL)
# cv.imshow('HSV', hsv)

# converting to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()
cv.imshow("RGB", rgb)


cv.waitKey(0)