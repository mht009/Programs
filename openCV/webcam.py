# changing resolution of web cam
import cv2 as cv

def changeRes(width, height, capture):
    capture.set(3, width)
    capture.set(4, height)

# reading video
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    # isTrue, resframe = changeRes(0.5, 0.5, frame)
    cv.imshow('Live', frame)
    # cv.imshow('Res Live', resframe)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
    
