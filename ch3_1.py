# -*- coding:utf-8 -*-

import sys
import numpy as np
from skimage import io
from skimage import transform
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# (1)
# コマンドライン引数受け取り
template_path = sys.argv[1]
target_path = sys.argv[2]

# (2)
# テンプレート、対象画像の読み込み（グレースケール）
template = io.imread(template_path, as_gray = True)
target = io.imread(target_path, as_gray = True)
th, tw = template.shape

# (3)
score_map = np.zeros( shape = (target.shape[0]-th, target.shape[1]-tw))

# (4) 画像全体を走査してSSD(差の二乗和)を計算
for y in range(score_map.shape[0]):
    for x in range(score_map.shape[1]):
        diff = target[y:y + th, x:x + tw] - template
        score_map[y, x] = np.squre(diff).sum()

# (5) SSD(差の二乗和)が最小の座標を取得
x, y = np.unravel_index(np.argmin(score_map), socre_map.shape)

# (6) 結果を可視化
