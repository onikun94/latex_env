import cv2
import matplotlib.pyplot as plt

image = cv2.imread("input.bmp",0)
img_hist = cv2.equalizeHist(image)

hist0 = cv2.calcHist(images = [image],channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.plot(hist0)
plt.savefig("histgram.png")

