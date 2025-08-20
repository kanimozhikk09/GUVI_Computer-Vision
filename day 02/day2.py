import cv2
import matplotlib.pyplot as plt

a=cv2.imread("1.jpg")
print(a.shape)
plt.imshow(cv2.cvtColor(a,cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()
cv2.imwrite("output.jpeg")




