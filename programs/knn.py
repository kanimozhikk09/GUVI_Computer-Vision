import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
#load digits dataset ###PS C:\Users\student\Desktop\programs> pip install scikit-learn   **

digits=datasets.load_digits()
#FEATURES and Labels(8*8 grayscale images)
X=digits.images
y=digits.target
#Flatten images(8*8-64 features)
n_samples=len(X)
X=X.reshape((n_samples,-1))
#Train-test split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5,shuffle=False)
#Create and train KNN model(k=5)
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

y_pred=knn.predict(X_test)
print("KNN Accuracy:",metrics.accuracy_score(y_test,y_pred))
images_and_predictions=list(zip(digits.images[n_samples//2:],y_pred))
for index,(image,prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(1,4,index+1)
    plt.axis("off")
    plt.imshow(image,cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title(f'Pred:{prediction}')

plt.show()

