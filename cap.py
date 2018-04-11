# -*- coding: utf-8 -*-  
import time
import picamera
import picamera.array
import cv2

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.hflip = False
    camera.vflip = True
    camera.start_preview()
    time.sleep(10)
    with picamera.array.PiRGBArray(camera) as stream:
        camera.capture(stream, format='bgr')
        # 此时就可以获取到bgr的数据流了
        image = stream.array
    image = image[0:768,245:680]
    cv2.imwrite("image.jpg",image)
