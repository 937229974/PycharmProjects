# -*- coding:utf-8 -*-
import json

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import subprocess,os,sys,time
import pytesseract
from PIL import Image,ImageEnhance

import pymysql
import requests
# from PIL import Image
# from bottle import route, run

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW



    #数据库驱动
def con_mysql(sql):
            try:
                # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
                conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='python', port=3306, charset='utf8')
                cur = conn.cursor()  # 获取一个游标
                cur.execute(sql)
                data = cur.fetchall()
                cur.close()  # 关闭游标
                conn.close()  # 释放数据库资源
                return  data

            except  Exception:
                print("sql 数据库插入异常 ----",sql)




                # 数据库驱动
    #连接手机
def login():
    try:
        sql ="select t.id, t.mobile ,t.url_home,t.url_detail,t.`status`,t.source from  app_ppd_spider t where t.back_code ='400'"
        data = con_mysql(sql)
        if len(data) > 0:
            for i in range(len(data)):
                 print(data[i][0])
                 id = data[i][0]
                 uname = data[i][1]
                 url_home = data[i][2]
                 url_detail = data[i][3]
                 status = data[i][4]
                 source = data[i][5]
                 print(id+"-----------"+uname)


                 print("图片识别状态--"+str(status))
                 dict = '{\
                     "mobile": "'+uname+'",\
                     "img_list": [\
                         "'+url_home+'",\
                         "'+url_detail+'"\
                     ],\
                     "other": "'+str(status)+'"\
                 }'
                 if source == "all":
                     print("回调平台------%s" % source)
                     try:

                         url = "http://console.saas.zhishensoft.com/api/v2/OuputCusAction/ppd?sign=3ab7873060b6de9ca93b664e752bca6f"
                         s = requests.post(url, dict)
                         s1_code = s.status_code
                     except:
                         s1_code = 400

                     try:
                         # url_2 = "http://loanshop.dev.zhishensoft.com:8002/notify/Creditauth/receive"
                         url_2 = "http://daiduoduo.zhishensoft.com/notify/creditauth/receive"
                         s2 = requests.post(url_2, dict)
                         url_3 = "http://sujie.guaniu.net/notify/creditauth/receive"
                         s3 = requests.post(url_3, dict)
                         s2_code = s3.status_code

                     except:
                         s2_code=  400

                     if s1_code  == 200 and s2_code == 200:
                         code = '200'
                     elif s1_code !=  200 and s2_code == 200:
                         code = '300'
                     elif  s1_code ==  200 and s2_code != 200:
                         code = '301'
                     elif s1_code != 200 and s2_code != 200:
                         code = '400'


                 elif   source == "xdy":
                     print("回调平台------%s" % source)
                     try:
                         url = "http://console.saas.zhishensoft.com/api/v2/OuputCusAction/ppd?sign=3ab7873060b6de9ca93b664e752bca6f"
                         s = requests.post(url, dict)
                         s1_code = s.status_code
                     except:
                         s1_code = 400
                     if s1_code  == 200 :
                         code = '200'
                     else:
                         code = '400'

                 elif      source == "dc":
                     print("回调平台------%s" % source)
                     try:

                         # url_2 = "http://loanshop.dev.zhishensoft.com:8002/notify/Creditauth/receive"
                         url_2 = "http://daiduoduo.zhishensoft.com/notify/creditauth/receive"
                         s2 = requests.post(url_2, dict)
                         url_3 = "http://sujie.guaniu.net/notify/creditauth/receive"
                         s3 = requests.post(url_3, dict)
                         s2_code = s3.status_code
                     except:
                         s2_code =  400

                     if  s2_code == 200:
                         code = '200'
                     else:
                         code = '400'
                 sql = "update app_ppd_spider set back_code='" + code + "' where id='" + id + "'"
                 print('更新数据库 %s ' % sql)
                 con_mysql(sql)


    except:
        print("读取文件失败")




if __name__  == "__main__":
    login()

