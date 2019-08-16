# -*- coding: utf-8 -*-  
import cv2  
import numpy as np
cam = cv2.VideoCapture(0)
while (1):
	ret,frame = cam.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  
	
	circles1 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,  
	600,param1=100,param2=30,minRadius=80,maxRadius=200)  
	circles = circles1[0,:,:]  
	circles = np.uint16(np.around(circles))  
	for i in circles[:]:   
		cv2.circle(frame,(i[0],i[1]),i[2],(255,0,0),5)  
		cv2.circle(frame,(i[0],i[1]),2,(255,0,255),10)  
		cv2.rectangle(frame,(i[0]-i[2],i[1]+i[2]),(i[0]+i[2],i[1]-i[2]),(255,255,0),5)  
		
	print("圆心坐标",i[0],i[1]) 
	cv2.imshow("frame",frame) 
	