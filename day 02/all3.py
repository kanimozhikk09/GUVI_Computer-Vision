import cv2
import matplotlib.pyplot as plt
img=cv2.imread("1.jpg")
gaussian =cv2.GaussianBlur(img,(5,5),0)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,100)
threshold,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
plt.imshow(cv2.cvtColor(edges,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()