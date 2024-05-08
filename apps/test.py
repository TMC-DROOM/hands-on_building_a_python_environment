import cv2
import numpy as np

# 画像サイズ
size = np.array([480, 640, 3])

# 色指定 [B, G, R]
color = np.array([0, 0, 255])

# 塗りつぶし処理
img = np.full(size, color, dtype = np.uint8)

# 画像表示
cv2.imshow('fill_image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()