from sklearn.svm import SVC
from sklearn.svm import  LinearSVC
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

data = pd.read_csv("F:/model/gn.csvDemo",)
ncol = data.shape[1]
X = data.iloc[:,1:ncol]
y = data.iloc[:,0]
print(X.shape)


clf = ExtraTreesClassifier()
clf = clf.fit(X, y)
imp = clf.feature_importances_
print(imp)
name_list = X.columns
num_list = imp

'''
importance = np.concatenate(([name_list],[num_list]),axis=0)
importance = importance.T
importance.columns = ['Features','Importance']
importance_s = sorted(importance, key = 'Importance')
print(importance)
'''
plt.barh(range(len(num_list)), num_list,tick_label = name_list)
plt.show()


