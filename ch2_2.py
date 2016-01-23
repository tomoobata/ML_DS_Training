# -*- coding:utf-8 -*-

from skimage import io

image = io.imread('mandrill.png')

print '(1)', type(image)	# iamgeの型名
print '(2)', image.shape	# 各次元の大きさ
print '(3)', image[300,400]	# 座標(300,400)の画素値
