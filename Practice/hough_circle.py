# -*- coding: utf-8 -*-  
import cv2
import numpy as np  
#载入并显示图片
img=cv2.imread("C:\\Users\\sirei\\Documents\\GIT_SYNC\\TYT\\learn\\twins0.png")

#灰度化
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#输出图像大小，方便根据图像大小调节minRadius和maxRadius
print(img.shape)
#霍夫变换圆检测
circles= cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=60,maxRadius=100)
#输出返回值，方便查看类型
print(circles)
#输出检测到圆的个数
print(len(circles[0]))

print('-------------我是条分割线-----------------')
#根据检测到圆的信息，画出每一个圆
for circle in circles[0]:
    #圆的基本信息
    print(circle[2])
    #坐标行列
    x=int(circle[0])
    y=int(circle[1])
    #半径
    r=int(circle[2])
    #在原图用指定颜色标记出圆的位置
    img=cv2.circle(img,(x,y),5,(0,0,255),-1)
#显示新图像
cv2.namedWindow("res", cv2.WINDOW_NORMAL)
cv2.imshow('res',img)

#按任意键退出
cv2.waitKey(0)
cv2.destroyAllWindows()