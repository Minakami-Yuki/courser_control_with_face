# -*- coding: cp936 -*-
import cv2
import pyautogui
import time
import types
face_cascade=cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
############################################################
size = (int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
############################################################
print "camara is open:"
print capture.isOpened()
print "it's time to initialize coordinate"
print "put your face to left-up,left-down,right-up,right-down in turn"
print "press 'a' to get coordinate"
print "when main process is running ,press 'q' to quit"
print "program begin in 10seconds"
time.sleep(10)
#x=list(range(0,4))
#y=[6,6,6,6]

flag=True
#TypeError: 'numpy.int32' object does not support item assignment
while flag:
    success, img = capture.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    #cv2.imshow('face',faces)#似乎不能直接输出
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)  #五个参数，图片名称、两个对角点坐标、颜色数组、线宽
    cv2.imshow('face_detect', img)
    key = cv2.waitKey(1)
    if key == ord('a'):
        for (xx,yy,w,h) in faces:
            print xx
            xa=xx
            #print type(xx)
            #xtest = xx.astype(int)
            #print type(xtest)
            #x[i]=xtest
            print yy
            #y[i]=yy
            ya=yy
            print w
            print h
            #print i
            print "-----------------------------------"
        flag = False

flag=True
while flag:
    success, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)
    cv2.imshow('face_detect', img)
    key = cv2.waitKey(1)
    if key == ord('a'):
        for (xx, yy, w, h) in faces:
            print xx
            xb = xx
            print yy
            yb = yy
            print w
            print h
            print "-----------------------------------"
        flag = False

flag=True
while flag:
    success, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)
    cv2.imshow('face_detect', img)
    key = cv2.waitKey(1)
    if key == ord('a'):
        for (xx, yy, w, h) in faces:
            print xx
            xc = xx
            print yy
            yc = yy
            print w
            print h
            print "-----------------------------------"
        flag = False

flag=True
while flag:
    success, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)
    cv2.imshow('face_detect', img)
    key = cv2.waitKey(1)
    if key == ord('a'):
        for (xx, yy, w, h) in faces:
            print xx
            xd = xx
            print yy
            yd = yy
            print w
            print h
            print "-----------------------------------"
        flag = False

#for s in range(0,3):
 #   print x[s]
  #  print y[s]
   # print "------------------------"

cv2.destroyAllWindows()
temp=cv2.imread('pass1.png')
cv2.imshow('success,press any key to continue',temp)
cv2.waitKey()
#time.sleep(2)
cv2.destroyAllWindows()

left_x=(xa+xb)/2
right_x=(xc+xd)/2
up_y=(ya+yc)/2
down_y=(yb+yd)/2

print left_x
print right_x
print up_y
print down_y

while True:
    success, img = capture.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for (x, y, w, h) in faces:
        center_x = (1360 - 5) * (left_x - x) / (left_x - right_x) + 5
        center_y = (763 - 5) * (y - up_y) / (down_y - up_y) + 5

    pyautogui.moveTo(center_x, center_y)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

capture.release()