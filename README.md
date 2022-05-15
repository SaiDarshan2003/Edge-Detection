# Edge-Detection
## Aim:
To perform edge detection using Sobel, Laplacian, and Canny edge detectors.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import all the necessary modules for the program.
### Step2:
Load a image using imread() from cv2 module.
### Step3:
Convert the image to grayscale.
### Step4:
Using Sobel operator from cv2,detect the edges of the image.
### Step5:
Using Laplacian operator from cv2,detect the edges of the image.
### Step6:
Using Canny  operator from cv2,detect the edges of the image.
## Program:

``` Python
# Import the packages
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image, Convert to grayscale and remove noise
image1=cv2.imread('1.png',0)
plt.imshow(image1)
# SOBEL EDGE DETECTOR
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
```
## Output:
### SOBEL EDGE DETECTOR
![inp](1.png)
### LAPLACIAN EDGE DETECTOR
![inp](2.png)
### CANNY EDGE DETECTOR
![inp](3.png)
## Result:
Thus the edges are detected using Sobel, Laplacian, and Canny edge detectors.
