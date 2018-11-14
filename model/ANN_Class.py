#-*- coding: utf-8 -*-
#使用神经网络算法预f放款额度高低
 
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Activation 
from keras.layers import Dropout
import tensorflow 
import numpy as np
import matplotlib.pyplot as plt

from keras.models import load_model


#参数初始化
inputfile = 'F:/model/train.csvDemo'
data = pd.read_csv(inputfile, ) #导入数据
ncol = data.shape[1]

x = data.iloc[:, 1:ncol].as_matrix()
y = data.iloc[:, 0].as_matrix().astype(int)

data_test = pd.read_csv('F:/model/test.csvDemo', ) #导入数据
x_test = data_test.iloc[:, 1:ncol].as_matrix()
y_test = data_test.iloc[:, 0].as_matrix().astype(int)

 

 
model = Sequential() #建立模型
model.add(Dense(input_dim = 31, output_dim = 60,))
model.add(Dropout(0.5))
model.add(Activation('relu')) #由于是0-1输出，用sigmoid函数作为激活函数
model.add(Dense(input_dim = 31, output_dim = 60))
model.add(Dropout(0.5))
model.add(Activation('sigmoid')) #由于是0-1输出，用sigmoid函数作为激活函数
model.add(Dense(input_dim = 31, output_dim = 60))
model.add(Dropout(0.5))
model.add(Activation('sigmoid')) #由于是0-1输出，用sigmoid函数作为激活函数
model.add(Dense(input_dim = 31, output_dim = 60))
model.add(Dropout(0.5))
model.add(Activation('sigmoid')) #由于是0-1输出，用sigmoid函数作为激活函数
model.add(Dense(input_dim = 31, output_dim = 60))
model.add(Dropout(0.5))
model.add(Activation('sigmoid')) #由于是0-1输出，用sigmoid函数作为激活函数
model.add(Dense(input_dim = 31, output_dim = 1))
model.add(Activation('sigmoid')) #由于是0-1输出，用sigmoid函数作为激活函数 

 
 
model.compile(loss = 'binary_crossentropy', optimizer = 'rmsprop')
#编译模型。由于我们做的是二元分类，所以我们指定损失函数为binary_crossentropy，以及模式为binary
#另外常见的损失函数还有mean_squared_error、categorical_crossentropy等，请阅读帮助文件。
#求解方法我们指定用adam，还有sgd、rmsprop等可选
 
model.fit(x, y, epochs = 150, batch_size = 5) #训练模型，学习100次
#print(model.evaluate(x_test, y_test))

model.save('F:/model/ANN_model.h5')
#model = load_model('d:/my_python/CNN_model.h5')
yp = model.predict_classes(x_test).reshape(len(y_test)) #分类预测
#混淆矩阵可视化函数
def cm_plot(y_test, yp):
    from sklearn.metrics import confusion_matrix #导入混淆矩阵函数
    cm = confusion_matrix(y_test, yp) #混淆矩阵
 
    plt.matshow(cm, cmap=plt.cm.Greens) #画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
    plt.colorbar() #颜色标签
    for x_test in range(len(cm)): #数据标签
        for y_test in range(len(cm)):
            plt.annotate(cm[x_test,y_test], xy=(x_test, y_test), horizontalalignment='center', verticalalignment='center')
    plt.ylabel('True label') #坐标轴标签
    plt.xlabel('Predicted label') #坐标轴标签
    return plt
cm_plot(y_test, yp).show()