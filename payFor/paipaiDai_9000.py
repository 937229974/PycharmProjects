# -*- coding:utf-8 -*-
import json

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import subprocess,os,sys,time,traceback
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
                conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='python', port=3306, charset='utf8')
                # conn = pymysql.connect(host='117.34.95.100', user='python', passwd='zhishen1234', db='python1', port=3306, charset='utf8')
                cur = conn.cursor()  # 获取一个游标
                cur.execute(sql)
                data = cur.fetchall()
                conn.commit()
                cur.close()  # 关闭游标
                conn.close()  # 释放数据库资源
                return  data

            except  Exception:
                print("sql 数据库插入异常 ----",sql)




def black_list(mobile):
    black_sql = "SELECT * FROM tb_app_black_list WHERE mobile='%s'" % mobile
    if len(con_mysql(black_sql)) == 0:
        black_sql = "INSERT INTO tb_app_black_list(mobile) VALUES('%s')" % mobile
        con_mysql(black_sql)
        print('插入至黑名单')
    # 数据库驱动
    #连接手机
def login():
    try:
        sql ="select * from app_ppd_spider where url_home is  null  and platform_id ='ppd' order by grade LIMIT 40,1"
        data = con_mysql(sql)
        #获取查询到的手机号进行去重操作
        id = data[0][0]
        mobile = data[0][1].replace("#",'')
        password = data[0][ 2]
        #对一周内爬过的数据进行去重
        week_sql = "select * from app_ppd_spider  where DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(create_date) and url_home is not NULL and mobile='%s' and password = '%s'" %(mobile,password)
        week_data = con_mysql(week_sql)
        #去重sql
        repeat_sql = "SELECT * FROM app_ppd_spider  where mobile='%s' and password='%s' and url_home is not null" %(mobile,password)
        repeat_data = con_mysql(repeat_sql)
        #排除黑名单sql
        black_sql = "SELECT * from tb_app_black_list WHERE mobile ='%s'" %mobile
        black_data = con_mysql(black_sql)
        print (len(black_data))
        print('重复数据',len(repeat_data))
        print(len(data))
        sql_w = 'SELECT count(1) FROM tb_white_list t where t.mobile=%s' % data[0][1]
        data_w = con_mysql(sql_w)
        if data_w[0][0] == 0  and len(black_data)==0 and len(week_data) == 0:
            for i in range(len(data)):
             id = data[i][0]
             uname = data[i][1]
             pw = data[i][2].replace("#",'')
             source = data[i][3]

             print(id+"--------"+uname+"--------------"+pw+'-----------'+source)

             status_ppd,url_home_ppd,url_detail_ppd = req_ppd(uname,pw) #请求ppd 1
             print("状态",status_ppd,url_home_ppd,url_detail_ppd)
             flag =True
             if status_ppd ==2 or status_ppd == 3:
                 status_jjd, url_home_jjd, url_detail__jjd = req_jjd(uname, pw)

                 if status_jjd == 3 : #登录成功
                     status_ppd = 4
                     flag = False



             #'''回调白名单库'''

             if flag ==True and (status_ppd == 2 or status_ppd == 3  ):
                 try:
                     data = {
                         'mobile': uname,
                         'status': status_ppd
                     }
                     resp = requests.post('http://117.34.95.108:7072/cms/v1/api/addWhiteCustomer', data)
                     data = json.loads(resp.text)
                     code = data.get('code')
                     print("回调白名单code ---" + code)
                     if code == '1':
                         white_code = '200'
                     else:
                         white_code = '400'
                 except:
                         white_code = '400'
             else:
                 white_code = ''

            #回调
             dict = '{\
                 "mobile": "'+uname+'",\
                 "img_list": [\
                     "'+url_home_ppd+'",\
                     "'+url_detail_ppd+'"\
                 ],\
                 "other": "'+str(status_ppd)+'"\
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

                     url_2 = "http://api.gnfenqi.com/Pachong/notify_url"
                     s2 = requests.post(url_2, dict)
                     s2_code = s2.status_code
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
             elif   source == "dc":
                 print("回调平台------%s" % source)
                 try:
                     url_2 = "http://daiduoduo.zhishensoft.com/notify/creditauth/receive"
                     s2 = requests.post(url_2, dict)
                     s2_code = s2.status_code
                 except:
                     s2_code = 400

                 if s2_code == 200:
                     code = '200'
                 else:
                     code = '400'



             #不操作
             if (status_ppd == 2 or status_ppd == 3)  and flag == True:
                #先查黑名单表中是否有该条记录 如果有则不进行白名单插入操作
                black_sql = "SELECT count(1) from tb_app_black_list where mobile='%s'"%mobile
                #再查白名单表中是否有该条记录 如果有则不进行白名单插入操作
                white_sql = "SELECT count(1) from tb_app_white_list where mobile='%s'"%mobile
                #最后查spider表中是否该条记录的status=2或status=3 则进行插入
                spider_sql = "SELECT count(1) FROM app_ppd_spider WHERE mobile='%s' AND (STATUS=2 OR STATUS=3)"%mobile
                # if len(con_mysql(black_sql)) == 0 and len(con_mysql(white_sql))==0 and len(con_mysql(spider_sql))>0:
                black = con_mysql(black_sql)
                white = con_mysql(white_sql)
                if black[0][0] == 0 and white[0][0]==0 :
                    white_sql = "INSERT INTO tb_app_white_list(mobile) VALUES('%s')"%mobile
                    print("白名单操作----"+white_sql)
                    con_mysql(white_sql)

             # 黑名单操作
             elif status_ppd == 4 or flag == False :
                # 定义白名单查询sql
                white_sql = "SELECT * from tb_app_white_list where mobile='%s'" % mobile
                # 先查白名单表中是否有该条记录 如果有则进行白名单剔除操作
                if len(con_mysql(white_sql)) > 0:
                    white_sql = "DELETE  from tb_app_white_list where mobile='%s'"%mobile
                    con_mysql(white_sql)
                #黑名单操作
                black_list(mobile)

             sql = "update app_ppd_spider set url_home='" + url_home_ppd + "',url_home_jjd='"+url_home_jjd+"'" \
                    ",url_detail='" + url_detail_ppd + "',url_detail_jjd ='"+url_detail__jjd+"',back_code='" + code + "'," \
            "status='" + str(status_ppd) + "',status_jjd='"+status_jjd+"',white_code='" + white_code + "', update_date=now() where id='" + id + "'"
             print('更新数据库 %s ' % sql)
             con_mysql(sql)

        else:
            # if len(repeat_data) > 0 :
            #     pass
            # else:
            sql = "update app_ppd_spider set url_home='200',url_detail='200',back_code='200',status='0',update_date=now() where id='" + str(data[0][0]) + "'"
            print('更新数据库 %s ' % sql)
            con_mysql(sql)

    except Exception as e:
        print(' repr(e):', repr(e))
        print('e.message:',e.message)
        print("读取文件失败")
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
    #print(data)

    status = read_img_ppd(address_home, 1)
    if status == 1:
        status = read_img_ppd(address_detail, 2)

    if status == None:
        status = 5
    return status,url_home,url_detail

#
#


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

def req_jjd(uname,pw):

    url = "http://127.0.0.1:8000/loginApp/?uname=%s&pid=%s&platform=%s" % (uname, pw, 'jjd')
    print("请求地址为url----------" + url)
    html = requests.get(url)

    data = json.loads(html.text)

    url_home = data.get('url_home')
    url_detail = data.get('url_details')
    address_home = data.get('physics_home')
    address_detail = data.get('physics_details')
    status = read_img_jjd(address_home, 1)
    if status == 1:
        status = read_img_jjd(address_detail, 2)
    if status == None:
        status = 5
    return status, url_home, url_detail

def read_img_jjd(img_path,flag):
    #
    # img_path = "F:/今借到测试数据/20180608/登录成功/有逾期记录.png"

    print(img_path)

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    print('--------------')
    #print(line)
    if flag == 1:
        login = line.count("今借到借款攻胳")  # 登录失败
        login1 = line.count("已阅读并同意 《今借到用户协议》")  # 登录失败
        login2 = line.count("登录脏册")  # 登录失败
        login3 = line.count("手机号或密码错误")  #

        loan = line.count("求借款") # 登录成功 求借款
        iou = line.count("补借条")  #登录成功  补借条
        #home = line.count("这皇您便用今借到的第")  # 登录成功

        if login > 0 or login1 > 0 or login2 > 0 or login3 >0:
            return 0
        elif loan > 0 and iou > 0:
            return 1

    else:
        no_bill = line.count("待还总额 7夹待还 30夹待还")  # 登录成功
        no_bill_detail = line.count("0 0 0")  # 登录成功
        shengyu = line.count("剩余")  # 登录成功
        if no_bill > 0 and no_bill_detail > 0 :
            return 2
        elif shengyu > 0:
            return 3
if __name__  == "__main__":
    while True:
        try:
            login()
            time.sleep(1)
        except:
            print("--------------------------发生异常了：paipaiDai_1000" )
            traceback.print_exc()
            continue
