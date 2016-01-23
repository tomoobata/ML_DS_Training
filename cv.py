# -*- coding:utf-8 -*-
# centos7
# yum install -y opencv opencv-python

import cv2, sys

#顔検出器をロード
face_cascade = cv2.CascadeClassifier('/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
 
#入力画像の読み込み
target_path = sys.argv[1]
img = cv2.imread(target_path)
 
#gray scaleヘ変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
#顔検出
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
#枠
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
 
#結果の表示
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()