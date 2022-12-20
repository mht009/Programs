import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('Blank Image', blank)

# img = cv.imread('Photos\cat.jpg')
# cv.imshow('Cat', img)

# painting the image with certain color
blank[100:400, 300:400] = 0, 255, 0
cv.imshow("Green", blank)

# drawing rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=-1)
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
# cv.rectangle(blank, (0, 0), (blank.shape[1]//5, blank.shape[0]//2), (0, 255, 0), thickness=2)
# cv.imshow('Rectangle', blank)


# # drawing circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
# cv.imshow('Circle', blank)

# # drawing line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=4)
# cv.imshow('Line',  blank)

# writing text on an image
cv.putText(blank, "Mohit", (225, 255), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (125, 125, 125))
cv.imshow('Mohit', blank)

cv.waitKey(0)