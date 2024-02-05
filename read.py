import cv2 as cv
import numpy as np

# img = cv.imread('Image/Cat.jpg')

# cv.imshow('Cat', img)

# grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('grey', grey)

# cv.waitKey(0)

video = cv.VideoCapture(0)

while True:
    isTrue, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Live Video', gray)

    if cv.waitKey(20) & 0XFF==ord('d'):
        break

video.release()
cv.destroyAllWindows

# video = cv.VideoCapture(0)

# while True:
#     isTrue, frame = video.read()
#     cv.imshow('WebCam', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# video.release()
# cv.destroyAllWindows()


# blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
# cv.imshow('Rectangle', blank)

# cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (0,250,0), thickness=-1)
# cv.imshow('Circle', blank)

# cv.putText(blank, "Hello World", (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,123,0), thickness=2)
# cv.imshow('Text', blank)
# cv.waitKey(0)