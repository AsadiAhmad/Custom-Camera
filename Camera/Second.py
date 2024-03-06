import cv2 as cv

#cap = cv.VideoCapture('http://192.168.115.225:8080/video')
cap = cv.VideoCapture(0)
num = 0
isGray = False
isBlur = False
isCaptureing = False
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

def rotation (num, key, frame):
    if num == 4:
        num = 0
    if num == -1:
        num = 3
    if key == ord('.'):
        num += 1
    elif key == ord(','):
        num -= 1
    if num == 1:
        frame = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)
    if num == 2:
        frame = cv.rotate(frame, cv.ROTATE_180)
    if num == 3:
        frame = cv.rotate(frame, cv.ROTATE_90_COUNTERCLOCKWISE)
    return num, frame

def gray_scale (isGray, key, frame):
    if key == ord('g'):
        isGray = not isGray
    if isGray:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    return isGray,frame

def blur_picture (isBlur, key, frame):
    if key == ord('b'):
        isBlur = not isBlur
    if isBlur:
        ksize = (10,10)
        frame = cv.blur(frame, ksize)
    return isBlur,frame

def take_picture (key, frame):
    if key == ord('s'):
        cv.imwrite("1.jpg", frame)
        print("Image Saved!")

def take_video (isCaptureing, key, out, frame):
    if key == ord('c'):
        isCaptureing = True
    if isCaptureing:
        out.write(frame)
    if key == ord('e'):
        out.release()
        isCaptureing = False
    return isCaptureing

def call_functions (num, isGray, isBlur, isCaptureing, key, out, frame):
    num,frame = rotation(num, key, frame)
    isGray,frame = gray_scale(isGray, key, frame)
    isBlur,frame = blur_picture(isBlur, key, frame)
    take_picture(key, frame)
    isCaptureing = take_video(isCaptureing, key, out, frame)
    return num, isGray, isBlur, isCaptureing, frame

while True:
    flag,frame = cap.read()
    if flag is False:
        print("frame is not available")
        break
    key = cv.waitKey(10)
    num, isGray, isBlur, isCaptureing, frame = call_functions(num, isGray, isBlur, isCaptureing, key, out, frame)
    cv.imshow("frame",frame)
    if key == 27:
        break
cap.release()
cv.destroyAllWindows()
