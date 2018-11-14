# -*- coding:utf-8 -*-
from flask import Flask, request, Response,jsonify
import json
import numpy as np
from sklearn.externals import joblib
import hashlib

app = Flask(__name__)

@app.route('/predictModel', methods=['POST'])
def index():

   try:
      data = request.form['data']
      token = request.form['token']
      model_type = request.form['model']
      print (data)
      list = data.split(",")
      print(list)
      #加密监测
      md5_str = "preModel"+ list[0]+list[len(list)-1]
      #print "md50----%s"%md5_str
      sign = hashlib.md5(md5_str.encode(encoding='UTF-8')).hexdigest()
      if token == sign:
         print("-----------签名效验成功 ---------")
         data1 = np.array(list, dtype=float)
         print("加载模型......")
         if model_type == "gn":
            model = joblib.load("/python-api/gn_model.m")
         elif model_type == "xhb":
            model =joblib.load("/python-api/xhb_model.m")

         print("加载模型完成.")

         print("客户识别......")
         iden_y = model.predict([data1])
         print("================")
         print(iden_y[0])
         dict = {
            "code": "200",
            "data": float(iden_y[0]),
            "msg": "true",
         }
      else:
         dict = {
            "code": "300",
            "data": "签名失败",
            "msg": "false",
         }
      return  Response(json.dumps(dict),mimetype='application/json')

   except:
      dict = {
         "code": "400",
         "data": "",
         "msg": "false",
      }
      return Response(json.dumps(dict),mimetype='application/json')



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8787)