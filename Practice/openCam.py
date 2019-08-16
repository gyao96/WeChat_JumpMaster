# import cv2
# import numpy as np#添加模块和矩阵模块
# cap=cv2.VideoCapture(0)
# # 打开摄像头，若打开本地视频，同opencv一样，只需将０换成("×××.avi")
# while(1):    # get a frame   
#     ret, frame = cap.read()    # show a frame   
#     cv2.imshow("capture", frame)   
#     if cv2.waitKey(1) & 0xFF == ord('q'):        
#         break
# cap.release()
# cv2.destroyAllWindows()
# #释放并销毁窗口

import cv2 
import numpy as np 
  
img = cv2.imread('C:\\Users\\sirei\\Documents\\GIT_SYNC\\TYT\\learn\\twins0.png')  
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
ret,thresh=cv2.threshold(imgray,127,255,0)  
image,cnts,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
cv2.namedWindow("imageshow", cv2.WINDOW_NORMAL); 
cv2.imshow('imageshow',image)  # 显示返回值image，其实与输入参数的thresh原图没啥区别  
cv2.waitKey()  
print(np.size(cnts))  #   得到该图中总的轮廓数量  
print(cnts[0])   #  打印出第一个轮廓的所有点的坐标， 更改此处的0，为0--（总轮廓数-1），可打印出相应轮廓所有点的坐标  
print(hierarchy) #打印出相应轮廓之间的关系  
img=cv2.drawCountours(img,[cnts[0]],-1,(0,255,0),10)  #标记处编号为0的轮廓  
cv2.namedWindow("img", cv2.WINDOW_NORMAL);
cv2.imshow("img",img) 
cv2.waitKey() 