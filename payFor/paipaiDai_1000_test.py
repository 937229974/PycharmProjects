# -*- coding:utf-8 -*-
import json

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import subprocess,os,sys,time
import pytesseract
from PIL import Image,ImageEnhance

import pymysql
import requests
import  json
# from PIL import Image
# from bottle import route, run

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW



    #数据库驱动
def con_mysql(sql):
            try:
                # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
                # conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='python', port=3306, charset='utf8')
                conn = pymysql.connect(host='117.34.95.100', user='python', passwd='zhishen1234', db='python1', port=3306, charset='utf8')
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
    # try:
        sql ="SELECT * FROM `app_ppd_spider` t where t.`status`='2' or t.`status`='3' LIMIT 1,100;"
        data = con_mysql(sql)
        print(len(data))
        sql_w = 'SELECT count(1) FROM tb_white_list t where t.mobile=%s' % data[0][1]
        data_w = con_mysql(sql_w)
        if data_w[0][0] == 0:
            for i in range(len(data)):
             print(data[i][0])
             id = data[i][0]
             uname = data[i][1]
             pw = data[i][2]
             source = data[i][3]

             print(id+"--------"+uname+"--------------"+pw+'-----------')
             status = 0
             flag=True

             # status,url_home,url_detail = req_ppd(uname,pw) #请求ppd 1
             # print(status,url_home,url_detail)
             # if status !='0' or status != '5':
            #
            #
            #
            #      if status == 0 or status == 5:  # 请求 玖富  2
            #          print("玖富-----------")
            #          status, url_home, url_detail = req_jf(uname, pw)
            #          if status !='0' or status != '5':
            #              flag =False
            # if flag ==False:
            #



             # if status == 0 or status == 5:#你我贷    3
             #
             #     print("你我贷-----------")
             #     status, url_home, url_detail = req_nwd(uname, pw)
                 #
             #用钱宝4
             # if status == 0 or status == 5:  # 请求用钱宝4
             #     print("用钱宝-----------")
             #     status, url_home, url_detail = req_yqb(uname, pw)


             if status == 0 or status == 5:   #请求 信而富  5
                 print("信而富-----------")
                 status, url_home, url_detail = req_xef(uname, pw)

                 # '''回调白名单库'''
                 # if status == 2 or status == 3:
                 #     data = {
                 #         'mobile': uname,
                 #         'status': status
                 #     }
                 #     resp = requests.post('http://117.34.95.108:7072/cms/v1/api/addWhiteCustomer', data)
                 #     data = json.loads(resp.text)
                 #     code = data.get('code')
                 #     print("回调白名单code ---" + code)
                 #     if code == '1':
                 #         white_code = '200'
                 #     else:
                 #         white_code = '400'
                 # else:
                 #     white_code = ''


                 print("图片识别状态--"+str(status))
                 dict = '{\
                     "mobile": "'+uname+'",\
                     "img_list": [\
                         "'+url_home+'",\
                         "'+url_detail+'"\
                     ],\
                     "other": "'+str(status)+'"\
                 }'

                 white_code = '200'
                 code= '200'
                 sql = "insert into app_ppd_spider_copy (id,mobile,password,url_home,url_detail,status,platform_id,create_date)VALUES ((select replace(uuid(),'-','')),'" + uname + "','" + pw + "','" + url_home + "','" + url_detail + "','" + str(status) + "','yqb',now())"
                 print('更新数据库 %s ' % sql)
                 con_mysql(sql)

        else:
            # sql = "insert into app_ppd_spider_copy (id,mobile,password,url_home,url_detail,status,platform_id,create_date)VALUES ((select replace(uuid(),'-','')),'" + uname + "','" + pw + "','" + url_home + "','" + url_detail + "','" + status + "','jf',now())"
            print('更新数据库 %s ' % sql)
            # con_mysql(sql)

    # except:
    #     print("读取文件失败")
#ppd
def req_ppd(uname,pw):
    url = "http://127.0.0.1:8000/loginApp/?uname=%s&pid=%s&platform=%s" % (uname, pw, 'ppd')
    # url = "http://192.168.10.156:8000/loginApp/?uname=%s&pid=%s&platform=%s" % (uname, pw, 'ppd')
    print("请求地址为url----------" + url)
    html = requests.get(url)
    # print(html)

    data  = json.loads(html.text)

    url_home = data.get('url_home')
    url_detail = data.get('url_details')
    address_home = data.get('physics_home')
    address_detail = data.get('physics_details')
    # url_home, url_detail = (urls.text).split('&')
    print(data)

    status = read_img_ppd(address_home, 1)
    if status == 1:
        status = read_img_ppd(address_detail, 2)

    if status == None:
        status = 5
    return status,url_home,url_detail

#  nwd
def req_nwd(uname,pw):
    url = "http://127.0.0.1:8000/loginApp/?uname=%s&pid=%s&platform=%s" % (uname, pw, 'nwd')
    # url = "http://192.168.10.156:8000/loginApp/?uname=%s&pid=%s&platform=%s" % (uname, pw, 'nwd')
    print("请求地址为url----------" + url)
    # urls = requests.get(url)
    # url_home, url_detail = (urls.text).split('&')

    html = requests.get(url)

    data  = json.loads(html.text)

    url_home = data.get('url_home')
    url_detail = data.get('url_details')
    address_home = data.get('physics_home')
    address_detail = data.get('physics_details')
    status = read_img_nwd(address_home, 1)
    if status == 1:
        status = read_img_nwd(address_detail, 2)

    if status == None:
        status = 5
    return status,url_home,url_detail
#jiufu
def req_jf(uname,pw):
    # url = "http://192.168.10.156:8000/loginApp/?uname=%s&pid=%s&platform=%s" % (uname, pw, 'jf')
    url = "http://127.0.0.1:8000/loginApp/?uname=%s&pid=%s&platform=%s" % (uname, pw, 'jf')
    print("请求地址为url----------" + url)
    # urls = requests.get(url)
    # url_home, url_detail = (urls.text).split('&')
    html = requests.get(url)

    data  = json.loads(html.text)

    url_home = data.get('url_home')
    url_detail = data.get('url_details')
    address_home = data.get('physics_home')
    address_detail = data.get('physics_details')

    status = read_img_jf(address_home, 1)
    if status == 1:
        status = read_img_jf(address_detail, 2)

    if status == None:
        status = 5
    return status,url_home,url_detail
#信而富
def req_xef(uname,pw):
    # url = "http://192.168.10.156:8000/loginApp/?uname=%s&pid=%s&platform=%s" % (uname, pw, 'xef')
    url = "http://127.0.0.1:8000/loginApp/?uname=%s&pid=%s&platform=%s" % (uname, pw, 'xef')
    print("请求地址为url----------" + url)
    # urls = requests.get(url)
    # url_home, url_detail = (urls.text).split('&')
    html = requests.get(url)

    data  = json.loads(html.text)

    url_home = data.get('url_home')
    url_detail = data.get('url_details')
    address_home = data.get('physics_home')
    address_detail = data.get('physics_details')
    status = read_img_xef(address_home, 1)
    if status == 1:
        status = read_img_xef(address_detail, 2)

    if status == None:
        status = 5
    return status,url_home,url_detail

def req_yqb(uname,pw):

    url = "http://127.0.0.1:8000/loginApp/?uname=%s&pid=%s&platform=%s" % (uname, pw, 'yqb')
    print("请求地址为url----------" + url)
    html = requests.get(url)

    data = json.loads(html.text)

    url_home = data.get('url_home')
    url_detail = data.get('url_details')
    address_home = data.get('physics_home')
    address_detail = data.get('physics_details')
    status = read_img_xef(address_home, 1)
    if status == 1:
        status = read_img_xef(address_detail, 1)

    if status == None:
        status = 5
    return status, url_home, url_detail

def read_img_ppd(img_path,flag):


    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()

    if flag == 1:
        login = line.count("欢迎回来") #登录失败
        home = line.count("不向学生借款") #登录成功
        jisu = line.count('极速贷')
        backDay = line.count('应还款 日')
        if login > 0:
            return 0
        if home > 0 or jisu > 0 or backDay > 0:
            return 1

    else:
        rec = line.count("待还") #还款完成的
        plan = line.count('还款计划') #正在还款
        overdue = line.count('逾') #逾期
        reg = line.count("欢迎使用")
        rec_1  = line.count("系统目前没有您的借款记")
        if rec_1 >0:
            return 2
        if rec  > 0 and overdue == 0 :
            return 2
        if plan > 0  and overdue == 0:
            return 3
        if overdue >0 and overdue > 0 :
            return 4
        if reg > 0 :
            return 0
def read_img_nwd(img_path,flag):


    print(img_path)

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    # print('--------------')
    # print(line)
    if flag == 1:
        login = line.count("协议") #登录失败
        login1 = line.count("您的登录手机号") #登录失败
        home = line.count("去借款") #登录成功
        home1 = line.count("还款日") #登录成功
        if login > 0  or login1 > 0:
            return  0
        elif home > 0 or home1 > 0 :
            return 1

    else:
        back = line.count("巳还") #
        if back >0:
            return 2
def read_img_jf(img_path,flag):


    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    # print('--------------')
    # print(line)
    if flag == 1:
        login = line.count("短信验证码登录")  # 登录失败
        login1 = line.count("去注册")  # 登录失败
        home = line.count("积分")  # 登录成功
        home1 = line.count("近真月待还")  # 登录成功
        if login > 0 or login1 > 0:
            return 0
        elif home > 0 or home1 > 0:
            return 1

    else:
        no_bill = line.count("暂时还没有账单")  #
        bill = line.count("已结")  #
        bill_2 = line.count("还款中")  #
        if no_bill > 0 or bill:
            return 2
        elif bill_2 >0 :
            return 3
def read_img_xef(img_path,flag):
    # list = url_path.split('/')
    # img_path = "E:/pics/images/"
    # img_path += list[-1]
    #
    # print(img_path)

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    # print('--------------')
    # print(line)
    if flag == 1:
        login = line.count("置 ........")  # 登录失败
        login1 = line.count("信而窨")  # 登录失败
        home = line.count("认证提额")  # 登录成功
        home1 = line.count("诚信会员")  # 登录成功
        home2 = line.count("补充资料")  # 登录成功
        if login > 0 or login1 > 0:
            return 0
        elif home > 0 or home1 > 0 or home2 > 0:
            return 1

    else:
        no_bill = line.count("您还没有苄目关记录硪")  #
        bill_3 = line.count("还款成功")  #
        bill_4 = line.count("还款失败")  #
        if no_bill > 0 :
            return 2
        elif bill_4 > 0:
            return 4
        elif bill_3 >0:
            return 3
def read_img_yqb(img_path,flag):

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()

    if flag == 1:
        login = line.count("已有 帐号去登录")  # 登录失败
        login1 = line.count("忘记密码")  # 登录失败
        home = line.count("获取额虔")  # 登录成功
        home1 = line.count("可借额")  # 登录成功
        bill_4 = line.count("冻结")  # 登录成功
        home3 = line.count("获取额度尖败")  # 登录成功
        bill_3 = line.count("囤 囤 囤 囤 囤 囤")  #
        bill_44 = line.count("请您珍惜")
        if login > 0 or login1 > 0:
            return 0
        elif bill_4 >0 or bill_44 > 0  :
            return 4
        elif home > 0 or home1 > 0 or home3 > 0:
            return 1
        elif bill_3 >0 :
            return 3
if __name__  == "__main__":
    # while True:
        login()
        # time.sleep(1)
