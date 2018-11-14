import numpy as np
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

print("加载模型......")
model = joblib.load("F:/model/rf_model.m")
print("加载模型完成.")

print("加载数据......")
data = np.loadtxt(open("F:/model/predict.csvDemo"), delimiter=',')
id = data[:,0]
ncol = data.shape[1]
org_data = data[:,1:ncol]
print("加载数据结束.")

print("客户识别......")
iden_y = model.predict(org_data)
iden_y_prob = model.predict_proba(org_data)[:,1]
print("识别结果写出......")
result = np.concatenate(([id],[iden_y],[iden_y_prob]),axis=0)
np.savetxt("F:/model/result.csvDemo", result.T, delimiter=',')
print("写出完成！")