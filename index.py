import numpy as np
import cv2

img = cv2.imread("cat.png", 0)
  
print(img.shape)
print(img.ndim)
print(type(img))

kernel = [
	[-1, 1, 0],
	[-1, 1, 0],
	[-1, 1, 0]
]

for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		print(img[i][j])

print(kernel)