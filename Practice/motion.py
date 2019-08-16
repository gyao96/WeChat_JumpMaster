# -*- coding: utf-8 -*-  
import cv2  
import numpy as np  
import matplotlib.pyplot as plt  
  
img = cv2.imread("C:\\Users\\sirei\\Documents\\GIT_SYNC\\TYT\\learn\\twins0.png")  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
  
  
circles1 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,  
600,param1=100,param2=20,minRadius=65,maxRadius=80)  
circles = circles1[0,:,:]  
circles = np.uint16(np.around(circles))  
for i in circles[:]:   
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),5)  
    cv2.circle(img,(i[0],i[1]),2,(255,0,255),10)  
    cv2.rectangle(img,(i[0]-i[2],i[1]+i[2]),(i[0]+i[2],i[1]-i[2]),(255,255,0),5)  
      
print("圆心坐标",i[0],i[1]) 
cv2.namedWindow("img", cv2.WINDOW_NORMAL);
cv2.imshow("img",img) 
cv2.waitKey(0)