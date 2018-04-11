# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO  
import time  
import signal  
import atexit  
  
atexit.register(GPIO.cleanup)    
  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(18, GPIO.OUT, initial=False)  
p = GPIO.PWM(18,50) #50HZ  
p.start(0)  
time.sleep(2)  

up = 9
down = 10.7

def press(s):
    p.ChangeDutyCycle(down)
    time.sleep(0.08)
    p.ChangeDutyCycle(0)
    time.sleep(s)
    p.ChangeDutyCycle(up)
    time.sleep(0.08)
    p.ChangeDutyCycle(0)
    time.sleep(1)

p.ChangeDutyCycle(up)
time.sleep(0.1)
p.ChangeDutyCycle(0)
time.sleep(1)
while(True):
   print("preparing")
   time.sleep(3)
   press(float(274.776915*3.08/1000))

#  for i in range(0,181,10):  
#    p.ChangeDutyCycle(2.5 + 10 * i / 180) #设置转动角度  
#    time.sleep(0.02)                      #等该20ms周期结束  
#    p.ChangeDutyCycle(0)                  #归零信号  
#    time.sleep(0.01)  
#  time.sleep(0.5)
#  for i in range(181,0,-10):  
#    p.ChangeDutyCycle(2.5 + 10 * i / 180)  
#    time.sleep(0.02)  
#    p.ChangeDutyCycle(0)  
#    time.sleep(0.01)
#   p.ChangeDutyCycle(2.5)
#   time.sleep(0.5)
#   p.ChangeDutyCycle(0)
#   time.sleep(0.5)
#   p.ChangeDutyCycle(5)
#   time.sleep(0.5)
#   p.ChangeDutyCycle(0)
#   time.sleep(0.5)
#   p.ChangeDutyCycle(7.5)
#   time.sleep(0.5)
#   p.ChangeDutyCycle(0)
#   time.sleep(0.5)
#   p.ChangeDutyCycle(10)
#   time.sleep(0.5)
#   p.ChangeDutyCycle(0)
#   time.sleep(0.5)
#   p.ChangeDutyCycle(12.5)
#   time.sleep(0.5)
#   p.ChangeDutyCycle(0)
#   time.sleep(0.5)

