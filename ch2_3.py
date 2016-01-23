# -*- coding:utf-8 -*-

from skimage import io

image = io.imread('mandrill.png')

# (1) 中心画素(240,180)を青に
image[180,240, 0:3] = [0,0,255]
# (2) 短形領域(20,20)-(200,140)を黒に
image[20:140,20:200, 0:3] = [0,0,0]
# (3) 短形領域(50,200)-(430,300)を暗く
image[200:300,50:430, 0:3] *= 0.5

io.imshow(image)
io.show()
