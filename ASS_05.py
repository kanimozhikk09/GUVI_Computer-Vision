#write a program to convert as image into graycale
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("images.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
