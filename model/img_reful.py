# -*- coding:utf-8 -*-
from flask import Flask, request, Response,jsonify
import json
import PIL.Image as img
import base64


app = Flask(__name__)

@app.route('/img', methods=['POST'])
def index():
   data = request.form['data']

   type ,imgStr = data.split(",")
   print(imgStr)
   imgdata = base64.b64decode(imgStr)
   path ='e:/pics/1.jpg'
   file = open(path, 'wb')
   file.write(imgdata)
   file.close()
   img_gyrate(path)


   dict = {
      "code": "200",
      "data": "",
      "msg": "true",
   }

   return Response(json.dumps(dict),mimetype='application/json')

def img_gyrate(path):
   im = img.open(path)
   ng = im.rotate(90)  # 逆时针旋转 45 度角。
   ng.save('e:/pics/2.png')



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8787)