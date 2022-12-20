import cv2 as cv

# Reading Images
# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)

# Reading videos
# capture = cv.VideoCapture('Videos/dog.mp4')
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()