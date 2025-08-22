#WRITE A PROGRAM TO IMPLEMENT BASIC FILTERING USING BLURS
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("J13Wn.jpg")
blur=cv2.blur(img,(5,5))
plt.imshow(cv2.cvtColor(blur,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()