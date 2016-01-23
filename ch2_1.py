# -*- coding:utf-8 -*-
# centos7
# yum install libtiff-devel libjpeg-devel libzip-devel freetype-devel lcms2-devel libwebp-devel tcl-devel tk-devel
# pip install --user numpy scikit-learn scikit-image matplotlib


import sys
import numpy as np
from skimage import io

image = io.imread('mandrill.png')	# (1)
io.imsave('mandrill2.png', image) 	# (2)
io.imshow(image)					# (3)
io.show()