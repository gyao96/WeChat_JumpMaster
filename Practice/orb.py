import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('burr.png',0)
img = cv2.medianBlur(img,5)
# 简单
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# 自适应
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


# cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst])

# src 为输入图像；
# maxval 为输出图像的最大值；
# adaptiveMethod 设置为cv2.ADAPTIVE_THRESH_MEAN_C表示利用算术均值法，设置为cv2.ADAPTIVE_THRESH_GAUSSIAN_C表示用高斯权重均值法；
# thresholdType: 阈值的类型；
# blockSize: b的值；
# C 为从均值中减去的常数，用于得到阈值；
# dst 为目标图像。