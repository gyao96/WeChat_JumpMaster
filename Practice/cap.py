# -*- coding: utf-8 -*-  
from time import sleep
from picamera import PiCamera

def capture():
    with PiCamera() as camera:
        camera.resolution = (1280, 768)
        camera.hflip = False
        camera.vflip = True

        camera.start_preview()
        time.sleep(5)
        camera.capture("img.jpg", resize=(320,240))
		
capture()