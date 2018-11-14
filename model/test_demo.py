from sklearn import svm
from sklearn.svm import SVC
import numpy as np
from numpy import *
import itertools
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
import datetime
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

starttime = datetime.datetime.now()

# 准备训练样本
print("正在读入数据")
data = np.loadtxt(open("F:/model/test_model.csvDemo"), delimiter=',', skiprows=1)
col_x = data.shape[1]
X = data[:, 1:col_x]
print("读入数据完成")

y = data[:, 0]
classname = np.array(['Low-Risk', 'High_Risk'])
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

print("开始训练")
rf = RandomForestClassifier(n_estimators=60, max_depth=13, min_samples_split=120,
                            min_samples_leaf=20, max_features=10, oob_score=True, random_state=10)
# n_estimators：弱学习器的最大迭代次数
# max_depth：决策树最大深度
# min_samples_split：内部节点再划分所需最小样本数
# min_samples_leaf：叶子节点所需最少样本数
# max_features：最大特征数
# oob_score：是否采用袋外样本来评估模型好坏
rf.fit(X_train, y_train)
print("训练完成")
# 保存模型
print("保存模型")
joblib.dump(rf, "F:/model/rf_model.m")
print("保存模型结束")

print("正在预测...")
y_pred = rf.predict(X_test)

print("预测精度为：", rf.score(X_test, y_test))
cnf_matrix = confusion_matrix(y_pred, y_test, labels=None, sample_weight=None)

endtime = datetime.datetime.now()
print("此次运行耗时：", endtime - starttime)


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