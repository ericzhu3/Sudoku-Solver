import cv2 as cv

# img = cv.imread('Image/Cat.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)

video = cv.VideoCapture(0)

while True:
    isTrue, frame = video.read()
    cv.imshow('WebCam', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()
cv.waitKey(0)