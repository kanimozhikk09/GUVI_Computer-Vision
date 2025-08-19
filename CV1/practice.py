import cv2
import matplotlib.pyplot as plt

img=cv2.imread("images.jfif")
print(img.shape)

cv2.rectangle(img,(50,50),(100,100),(0,0,255),2)
cv2.line(img,(50,50),(100,100),(255,0,0),2)
resize=cv2.resize(img,(200,200))
plt.imshow(cv2.cvtColor(resize,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()
cv2.imwrite("output.jpeg")