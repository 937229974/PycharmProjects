from sklearn import svm
from sklearn.svm import SVC
import numpy as np
from numpy import *
import itertools
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA

# 准备训练样本
data = np.loadtxt(open("C:/Users/Public/Nwt/cache/recv/PC/ionosphere.csvDemo"), delimiter=',')
col_x = data.shape[1]
X = data[:, 1:col_x]

# 进行主成分分解
pca = PCA(n_components='mle')
X = pca.fit_transform(X)
print("主成分数为：", X.shape[1])

y = data[:, 0]
classname = np.array(['Low-Risk', 'High_Risk'])
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

##开始训练
model = svm.SVC(C=1.5, kernel='rbf')  ##默认参数：kernel='rbf'
model.fit(X_train, y_train)

print("预测...")

y_pred = model.predict(X_test)

print("预测精度为：", model.score(X_test, y_test))
cnf_matrix = confusion_matrix(y_pred, y_test, labels=None, sample_weight=None)


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


plt.figure()
plot_confusion_matrix(cnf_matrix, classes=classname,
                      title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=classname, normalize=True,
                      title='Normalized confusion matrix')
plt.show()



