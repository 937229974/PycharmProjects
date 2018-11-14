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
        sql ="select * from app_ppd_spider where url_home is  null  and platform_id ='ppd' order by grade LIMIT 20,1"
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

             status_jjd = 0
             url_home_jjd = ""
             url_detail__jjd = ""

             # if status_ppd ==2 or status_ppd == 3:
             #     status_jjd, url_home_jjd, url_detail__jjd = req_jjd(uname, pw)
             #
             #     if status_jjd == 3  or status_jjd == 4 : #登录成功
             #         status_ppd = 4
             #         flag = False



             # #'''回调白名单库'''
             #
             # if flag ==True and (status_ppd == 2 or status_ppd == 3  ):
             #     try:
             #         data = {
             #             'mobile': uname,
             #             'status': status_ppd
             #         }
             #         resp = requests.post('http://117.34.95.108:7072/cms/v1/api/addWhiteCustomer', data)
             #         data = json.loads(resp.text)
             #         code = data.get('code')
             #         print("回调白名单code ---" + code)
             #         if code == '1':
             #             white_code = '200'
             #         else:
             #             white_code = '400'
             #     except:
             #             white_code = '400'
             # else:
             #     white_code = ''
             loan_money =""
             loan_start_date=""
             loan_last_date=""
             # if status_ppd == 3:
             #     loan_money,loan_start_date,loan_last_date = ocr_api(url_detail_ppd)

            #回调
             dict = '{\
                 "mobile": "'+uname+'",\
                 "img_list": [\
                     "'+url_home_ppd+'",\
                     "'+url_detail_ppd+'"\
                 ],\
                 "loan_money": "'+loan_money+'",\
                 "loan_start_date": "' + loan_start_date + '",\
                 "loan_last_date": "' + loan_last_date + '",\
                 "other": "'+str(status_ppd)+'"\
             }'
             print(dict)



             # if source == "all":
             #     print("回调平台------%s" % source)
             #     try:
             #         url = "http://console.saas.zhishensoft.com/api/v2/OuputCusAction/ppd?sign=3ab7873060b6de9ca93b664e752bca6f"
             #         s = requests.post(url, dict)
             #         s1_code = s.status_code
             #     except:
             #         s1_code = 400
             #
             #     try:
             #         # url_2 = "http://loanshop.dev.zhishensoft.com:8002/notify/Creditauth/receive"
             #         url_2 = "http://daiduoduo.zhishensoft.com/notify/creditauth/receive"
             #         s2 = requests.post(url_2, dict)
             #
             #         url_3 = "http://sujie.guaniu.net/notify/creditauth/receive"
             #         s3 = requests.post(url_3, dict)
             #
             #         url_2 = "http://api.gnfenqi.com/Pachong/notify_url"
             #         s2 = requests.post(url_2, dict)
             #         s2_code = s2.status_code
             #     except:
             #         s2_code=  400
             #
             #     if s1_code  == 200 and s2_code == 200:
             #         code = '200'
             #     elif s1_code !=  200 and s2_code == 200:
             #         code = '300'
             #     elif  s1_code ==  200 and s2_code != 200:
             #         code = '301'
             #     elif s1_code != 200 and s2_code != 200:
             #         code = '400'
             #
             # elif   source == "xdy":
             #     print("回调平台------%s" % source)
             #     try:
             #         url = "http://console.saas.zhishensoft.com/api/v2/OuputCusAction/ppd?sign=3ab7873060b6de9ca93b664e752bca6f"
             #         s = requests.post(url, dict)
             #         s1_code = s.status_code
             #     except:
             #         s1_code = 400
             #     if s1_code  == 200 :
             #         code = '200'
             #     else:
             #         code = '400'
             #
             # elif      source == "dc":
             #     print("回调平台------%s" % source)
             #     try:
             #
             #         # url_2 = "http://loanshop.dev.zhishensoft.com:8002/notify/Creditauth/receive"
             #         url_2 = "http://daiduoduo.zhishensoft.com/notify/creditauth/receive"
             #         s2 = requests.post(url_2, dict)
             #         url_3 = "http://sujie.guaniu.net/notify/creditauth/receive"
             #         s3 = requests.post(url_3, dict)
             #         s2_code = s3.status_code
             #
             #     except:
             #         s2_code =  400
             #
             #     if  s2_code == 200:
             #         code = '200'
             #     else:
             #         code = '400'
             # elif   source == "dc":
             #     print("回调平台------%s" % source)
             #     try:
             #         url_2 = "http://daiduoduo.zhishensoft.com/notify/creditauth/receive"
             #         s2 = requests.post(url_2, dict)
             #         s2_code = s2.status_code
             #     except:
             #         s2_code = 400
             #
             #     if s2_code == 200:
             #         code = '200'
             #     else:
             #         code = '400'



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

             white_code ="2000"
             code = '2000'
             sql = "update app_ppd_spider set url_home='" + url_home_ppd + "',url_home_jjd='"+url_home_jjd+"'" \
                    ",url_detail='" + url_detail_ppd + "',url_detail_jjd ='"+url_detail__jjd+"',back_code='" + code + "'," \
            "status='" + str(status_ppd) + "',status_jjd='"+ str(status_jjd) +"',white_code='" + white_code + "',loan_money='" + loan_money + "'" \
            ",loan_start_date='" + loan_start_date + "',loan_last_date='" + loan_last_date + "', update_date=now() where id='" + id + "'"
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
        login = line.count("欢迎回来")  # 登录失败
        login1 = line.count("欢迎使用")  # 登录失败
        home = line.count("提醒")  # 登录成功
        overdue1 = line.count('已')
        overdue2 = line.count('已逾期')
        backDay = line.count('立即还款')
        xinyongdu = line.count('可借额度')
        xinyongdu1 = line.count('可借额虔')
        success = line.count("不向学生三借款")
        if overdue1 > 0 or overdue2 >0 :
            return 4
        if login > 0 or login1 > 0:
            return 0
        if home > 0 or backDay > 0 or success > 0:
            return 1
        if xinyongdu > 0 or xinyongdu1 > 0:
            return 1


    elif flag == 2:
        rec = line.count("待还")  # 还款完成的
        no_rec = line.count("暂无待还列表")  # 还款完成的
        plan = line.count('还声欠计划')  # 正在还款
        plan2 = line.count('还款计划')  # 正在还款
        plan3 = line.count('己还清')  # 正在还款
        reg = line.count("欢迎使用")
        if no_rec > 0:
            return 2
        if rec > 0 or plan > 0 or plan2 >0 or plan3  >0  :
            return 3
        if reg > 0:
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
    print('今借到 图片识别 code-----',status)
    return status, url_home, url_detail

def read_img_jjd(img_path,flag):
    #
    print(img_path)

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    print('--------------')
    print(line)
    if flag == 1:
        login = line.count("今借到借款攻胳")  # 登录失败
        login1 = line.count("已阅读并同意 《今借到用户协议》")  # 登录失败
        login2 = line.count("登录脏册")  # 登录失败
        login3 = line.count("手机号或密码错误")  #

        loan = line.count("求借款") # 登录成功 求借款
        iou = line.count("补借条")  #登录成功  补借条
        auth = line.count("您的信用撮告已失效")  #登录成功  补借条
        friend = line.count("老乡")  #登录成功  补借条
        #home = line.count("这皇您便用今借到的第")  # 登录成功

        if login > 0 or login1 > 0 or login2 > 0 or login3 >0:
            return 0
        elif loan > 0 or iou > 0 or auth>0 or friend >0:
            return 1

    else:
        no_bill = line.count("待还总额 7夹待还 30夹待还")  # 登录成功
        no_bill_detail = line.count("0 0 0")  # 登录成功
        no_bill_2 = line.count("暂时还没有借入待还")
        shengyu = line.count("剩余")  # 登录成功
        shengyu_1 = line.count("剩佘")
        back_money = line.count("元")
        overdure = line.count("逾期")
        if no_bill > 0 and no_bill_detail > 0 :
            return 2
        elif no_bill_2 >0 :
            return 2
        elif shengyu > 0 or shengyu_1 >0 or back_money >0:
            return 3
        elif overdure > 0:
            return 4
#百度api  图片识别
def ocr_api(image_url):
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Accept':'*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Referer': 'http://ai.baidu.com/tech/ocr/webimage',
        'Cookie':'BAIDUID=370AF38E7427C681843F149494AF060B:FG=1; PSTM=1528362814; BIDUPSID=BACEFC98B946F48FA72A49C0FDDEBE97; BDUSS=paTDdUTTFkeWNycjJKaTBlVlpyWlFoMXJlR2RvNFZ6a1lZfmJCSmJXQ01kMXBiQUFBQUFBJCQAAAAAAAAAAAEAAAA2Dh1YRUFfTlVYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIzqMluM6jJbcn; docVersion=0; BDSFRCVID=JJAsJeC62ui8C_57-wQ6hBRZqesuoSRTH6aop4inACXZ6ifS7zhmEG0PDM8g0Ku-LKeRogKKy2OTH9jP; H_BDCLCKID_SF=tJPJVI82tCD3fP36qRbsMJ8thl63-4oX2TTKWjrJaDvPOMJRy4oTj6DDMbQvKbKfHR582nnPLfcaeJOuXT7-3MvB-fn-aJ3k3IcL-p7RfRbFEJ7oQft20M0EeMtjBbQaBGvILR7jWhvBhl72y5r805TXDNKqt58etn3Q0Rjebn7oD-8kbn5HK-LSMqO8etJya4o2WDvoLUJ5OR5Jj65TDlki5UPfe6c83IbGbfch5lvGO-J43MA--tR3DlQNe4kLbG7y-K-EQx7Ssq0x0MOWe-bQypoa5xbvJKOMahvXtq7xOKTF05CaeP_tqx5Ka43tHD7yWCkE-KJ5OR5JLn7nDn-9hMIfe6FjLNv3ohja-CbtbfbO-lnK-4TyyGCqJ68fJRPqV-t2-POqHtonMKIaj6vbqxby26n-Q2JeaJ5nJDohjDnJBT_bqjFyyx7GQqTD567tWMO4QpP-HJ7xj-r_LftRWGj0KqtfMDbLKl0MLpbYbb0xyn_VXMP80xnMBMn8teOnaIT_LIF-hDt6jj8-enO3Khb-5Rj22P_D_DPyHJOoDDv_yxQ5y4LdjG5ta6vmXbIfs43lJJnIVxclbJbhhptw3-Aq54RjJI5X5lO9yDQEex86247VQfbQ0-OuqP-jW5IL2pvHLJ7JOpvwDxnxy5Fq0a62btt_JnPH_CQP; Hm_lvt_fdad4351b2e90e0f489d7fbfc47c8acf=1530063720,1530063793,1530063978,1530071067; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; PSINO=1; seccode=fc4b186e650d26c86a684a0b61754fc6; Hm_lpvt_fdad4351b2e90e0f489d7fbfc47c8acf=1530083170'
    }
    url = 'http://ai.baidu.com/aidemo'
    dict ={'type': 'webimage',
           'image_url': image_url,
           }
    res = requests.post(url=url,data=dict,headers=headers)
    datas =json.loads(res.text)

    word_result= datas["data"]["words_result"]
    word_length = len(word_result)
    #借款金额  期数计算
    for i in range(0, word_length):
        word = str(word_result[i]["words"])
        if word == "已还总期数":
            qishu = str(word_result[i + 3]["words"])
            loan_money = word_result[i + 2]["words"]
            qs = int(qishu.split("/")[0])
            print("------------"+qishu)
            print("借款金额-----" + loan_money)

    loan_start_date =""
    loan_last_date  =""
    for i in range(0,word_length):
        word1 = str(word_result[i]["words"])
        if word1 == "已还清":
            print("第一期期还款时间 =====" + word_result[i - 1]["words"])
            dateStr = word_result[i - 1]["words"]
            if dateStr.count(".") > 0:
                string , date = dateStr.split("日")
                loan_start_date, loan_last_date = get_date(date, qs)
            print("开始借款时间-----" + loan_start_date)
            print("最后一期还款时间------" + loan_last_date)

            return loan_money, loan_start_date, loan_last_date
#推算时间
def get_date(date,qs):
    year, month, day = date.split(".")
    month = int(month)
    start_month = month - 1
    back_month = month + qs -2
    if start_month == 0:
        year = int(year) - 1
        start_date = str(year) + "-12-" + str(day)
    elif start_month < 10:
        start_date = str(year) + "-0" + str(start_month) + "-" + str(day)
    else:
        start_date = str(year) + "-" + str(start_month) + "-" + str(day)
    if back_month >12 :
        year =int(year) +1
        new_month = back_month -13
        if new_month > 9:
            last_date =str(year) + "-" + str(new_month) + "-" + str(day)
        else:
            last_date = str(year) + "-0" + str(new_month) + "-" + str(day)
    elif  back_month > 9:
        last_date = str(year) + "-" + str(back_month) + "-" + str(day)
    else:
        last_date = str(year) + "-0" + str(back_month) + "-" + str(day)
    return   start_date,last_date

if __name__  == "__main__":
    while True:
        try:
            login()
            time.sleep(1)
        except:
            print("--------------------------发生异常了：paipaiDai_1000" )
            traceback.print_exc()
            continue
