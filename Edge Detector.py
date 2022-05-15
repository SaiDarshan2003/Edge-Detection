#import all necessary modules
import cv2
import numpy as np
import matplotlib.pyplot as plt
#Loading the image
image1=cv2.imread('1.png',0)
#Convert to grayscale
img= cv2.GaussianBlur(image1,(3,3),0)
plt.imshow(img)
#SOBEL EDGE DETECTOR
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobelxy= cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)
plt.imshow(sobelx,cmap='gray')
plt.imshow(sobely,cmap='gray')
plt.imshow(sobelxy,cmap='gray')
# LAPLACIAN EDGE DETECTOR
dst = cv2.Laplacian(img,cv2.CV_16S,ksize=3)
plt.imshow(dst,cmap='gray')
abs_dst = cv2.convertScaleAbs(dst)
plt.imshow(abs_dst,cmap='gray')
# CANNY EDGE DETECTOR
edges = cv2.Canny(img,100,200)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()