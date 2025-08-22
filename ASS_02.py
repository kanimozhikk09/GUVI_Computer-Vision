#write a progam a draw a rectangle in an image
import cv2
import matplotlib.pyplot as plt

img =cv2.imread("images.jpg")
print(img.shape)
cv2.rectangle(img,(50,50),(100,100),(0,0,255),2)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()
cv2.imwrite("output.jpeg")