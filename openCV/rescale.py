import cv2 as cv


def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Reading Image
# Original image
img = cv.imread('Photos\cat.jpg')
cv.imshow('Cat', img)

# resized img
resized_img = rescaleFrame(img, 0.25)
cv.imshow('Resized Cat', resized_img)

cv.waitKey(0)



# # Reading videos
# capture = cv.VideoCapture('Videos/dog.mp4')
# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame, 0.2)

#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized )

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()