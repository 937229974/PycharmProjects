# -*- coding:utf-8 -*-
import os
import uuid

import datetime
from flask import Flask, request, Response
import face_recognition
import json
import PIL.Image as img
import base64


app = Flask(__name__)

@app.route('/img', methods=['POST'])
def index():
   try:
      data = request.form['data']

      type ,imgStr = data.split(",")
      # print(imgStr)
      imgdata = base64.b64decode(imgStr)

      imgName = str(uuid.uuid1())
      path = '/face-api/images/'
      path += str(datetime.date.today()) + '/'
      if not os.path.exists(path):
         os.makedirs(path)
      path += imgName + '.png'
      file = open(path, 'wb')
      file.write(imgdata)
      file.close()
      # img_gyrate(path)
      flag = face(path)
      s = 1
      while flag == 2:
         img_gyrate(path)
         flag = face(path)
         s += 1
         if s == 4 :
            break
      img_url = "http://113.134.212.85:8002/images/"+str(datetime.date.today()) + '/' + imgName + '.png'
      dict = {
         "code": flag,
         "data": "",
         "img_url": img_url,
         "msg": "true",
      }

      return Response(json.dumps(dict),mimetype='application/json')
   except:

      dict = {
         "code": 400,
         "data": "检查参数是否有误！",
         "img_url" :"",
         "msg": "false",
      }

      return Response(json.dumps(dict), mimetype='application/json')


def img_gyrate(path):
   im = img.open(path)
   ng = im.rotate(90)  # 逆时针旋转 45 度角。
   ng.save(path)

def face(path):
   face_image = face_recognition.load_image_file(path)
   face_encodings = face_recognition.face_encodings(face_image)
   face_locations = face_recognition.face_locations(face_image)
   n = len(face_encodings)
   if n > 2:
      # sys.exit()
      return 3
   try:
      face1 = face_encodings[0]
      face2 = face_encodings[1]
   except:
      print("2")
      # sys.exit()
      return 2

   results = face_recognition.compare_faces([face1], face2, tolerance=0.5)

   if results == [True]:
      print("0")
      return 0
   else:
      print("1")
      return 1


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8786)