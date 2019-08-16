import cv2  
import numpy as np   
import time  
  
  
img=cv2.imread("C:\\Users\\sirei\\Pictures\\Saved Pictures\\1.png") #读取图片作为背景  
  
#定义画圆事件，如果事件双击左键发生  
#则以此时双击的点为原点画一个半径为100px BGR为(255,255,0)粗细为3px的圆圈  
def draw_circle(event,x,y,flags,param):     
	if event==cv2.EVENT_LBUTTONDBLCLK:  
		cv2.circle(img,(x,y),100,(255,255,0),3)  
          
# 创建图像与窗口并将窗口与回调函数绑定  
cv2.namedWindow("image")   
cv2.setMouseCallback("image",draw_circle)  
  
  
while(1):  
	cv2.imshow("image",img)  
	if cv2.waitKey(100) == ord('q'):    #等待100毫秒 刷新一次显示图像  
		break  
cv2.destroyAllWindows()