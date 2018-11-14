# # -*- coding:utf-8 -*-
# from flask import Flask, request, Response
# import json
# import numpy as np
# from sklearn.externals import joblib
# import hashlib
#
# app = Flask(__name__)
#
# @app.route('/predictModel', methods=['POST'])
# def index():
#
#    try:
#       data = request.form['data']
#       token = request.form['token']
#       print data
#       list = data.split(",")
#       #加密监测
#       md5_str = "preModel"+ list[0]+list[len(list)-1]
#       #print "md50----%s"%md5_str
#       sign = hashlib.md5(md5_str.encode(encoding='UTF-8')).hexdigest()
#       if token == sign:
#          print "-----------签名效验成功 ---------"
#          data1 = np.array(list, dtype=float)
#          print "加载模型......"
#          model = joblib.load("F:/test_model/rf_model.m")
#          print "加载模型完成."
#
#          print "客户识别......"
#          iden_y = model.predict([data1])
#          print "============预测结果为======="
#          print iden_y
#          dict = {
#             "code": "200",
#             "data": iden_y,
#             "msg": "true",
#          }
#
#       else:
#          dict = {
#             "code": "400",
#             "data": "",
#             "msg": "false",
#          }
#       print dict
#       return  Response(json.dumps(dict))
#    except:
#       dict = {
#          "code": "400",
#          "data": "",
#          "msg": "false",
#       }
#       return Response(json.dumps(dict))
#
#
#
# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=8787)