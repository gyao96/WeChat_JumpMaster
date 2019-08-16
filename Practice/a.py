import cv2
from PIL import ImageGrab
from PIL import Image
import PIL
# 使用PIL库截取Windows屏幕
def pull_screenshot():
    im = ImageGrab.grab((654, 0, 1264, 1080))
    im.save("a.png","png")

img = cv2.imread("C:\\Users\\sirei\\Pictures\\Saved Pictures\\1.png")
pull_screenshot()
cv2.imshow("Image",img)
cv2.waitKey(0)