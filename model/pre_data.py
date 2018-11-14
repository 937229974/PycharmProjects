import datetime

import pymysql
import time


def con_mysql(sql):
    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='admin', db='test_model', port=3306, charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return data

    except  Exception:
        print("sql 数据库插入异常 ----", sql)
def pre_data():
    #查询sql
    sql_0 = '''
        SELECT
            t.`身份证证`,
            t.`手机号`,
            t.`借款金额额`,
            t.`借款期数`,
            t.`借款时间`,
            t.`还款时间`,
            t.`逾期天数`,
            t.`通讯录数量`,
            t.`通话记录数量`,
            t.`年龄验证`,
            t.`平台数`,
            t.`ip注册次数`,
            t.`手机与以往联系人比对`,
            t.`设备注册次数`,
            t.`手机是否实名`,
            t.`是否呼叫借款平台`,
            t.`是否呼叫亲属联系人`,
            t.`是否呼叫非亲属联系人`,
            t.`是否长时间关机`,
            t.`运营商-APP比对联系人`,
            t.`通讯录中通话时长在2分钟以上的人数`,
            t.`通话人数`
        FROM
            `sheet1` t 
    '''

    sql_1 ='''
        SELECT
            t.`身份证`,
            t.`手机号`,
            t.`借款金额`,
            t.`借款期数`,
            t.`借款时间`,
            t.`借款时间`,
            t.`逾期天数`,
            t.`通讯录数量`,
            t.`通话记录数量`,
            t.`年龄验证`,
            t.`平台注册数`,
            t.`ip注册次数`,
            t.`手机与以往联系人比对`,
            t.`设备注册次数`,
            t.`手机是否实名`,
            t.`是否呼叫借款平台`,
            t.`是否呼叫亲属联系人`,
            t.`是否呼叫非亲属联系人`,
            t.`是否长时间关机`,
            t.`运营商-APP比对联系人`,
            t.`通讯录中通话时长在2分钟以上的人数`,
            t.`通话人数`
        FROM
            `逾期未还款有数据客户(1)` t;
    '''
    sql_predict = '''
    SELECT
        t.`身份证`,
        t.`手机号`,
        t.`借款金额`,
        t.`借款期数`,
        t.`借款时间`,
        t.`借款时间`,
        t.`逾期天数`,
        t.`通讯录数量`,
        t.`通话记录数量`,
        t.`年龄验证`,
        t.`平台注册数`,
        t.`ip注册次数`,
        t.`手机与以往联系人比对`,
        t.`设备注册次数`,
        t.`手机是否实名`,
        t.`是否呼叫借款平台`,
        t.`是否呼叫亲属联系人`,
        t.`是否呼叫非亲属联系人`,
        t.`是否长时间关机`,
        t.`运营商-APP比对联系人`,
        t.`通讯录中通话时长在2分钟以上的人数`,
        t.`通话人数`
    FROM
         `逾期还款有数据客户1` t;
        -- `逾期未还款有数据客户(1)` t
    '''

    predict_overdue ='''
    SELECT
        t.`身份证`,
        t.`手机号`,
        t.`借款金额`,
        t.`借款期数`,
        t.`借款时间`,
        t.`借款时间`,
        t.`借款时间`,
        t.`通讯录数量`,
        t.`通话记录数量`,
        t.`年龄验证`,
        t.`借款时间`,
        t.`ip注册次数`,
        t.`手机与以往联系人比对`,
        t.`设备注册次数`,
        t.`手机是否实名`,
        t.`是否呼叫借款平台`,
        t.`是否呼叫亲属联系人`,
        t.`是否呼叫非亲属联系人`,
        t.`是否长时间关机`,
        t.`运营商-APP比对联系人`,
        t.`通讯录中通话时长在2分钟以上的人数`,
        t.`通话人数`
    FROM
        `sheet24` t
    '''
    datas = con_mysql(predict_overdue)
    # print(datas)
    tab = '1'  # 0 是还了  1 未还的
    for i in range(0,len(datas)):
        iCard = datas[i][0]
        iCard_ength = len(iCard)

        #判断性别
        if iCard_ength == 15:
            flag = iCard[-1:]
        elif iCard_ength == 18:
            flag = iCard[-2:-1]
            year = iCard[6:10]
            #print('-----'+year)

        if int(flag)%2 == 0:
            sex = '1'#女
        else:
            sex = '0'#男
        tel = datas[i][1]  #电话
        loan_moeny = datas[i][2] #借款金额
        loan_periods = datas[i][3] #借款期数
        loan_date = datas[i][4].replace('/','-')
        back_date = datas[i][5].replace('/','-')

        # 处理借款日期
        # loan_date  = to_date(loan_date)
        # back_date  = to_date(back_date)

        overdue_day = datas[i][6]

        contact_num = datas[i][7]
        call_rec_num  =datas[i][8]

        #处理年龄
        # agestr = datas[i][9]
        age = to_age(year)

        platform_num = datas[i][10]
        if platform_num.count('#N/A') >0 or platform_num.count('') >0 :
            platform_num = "0"

        ip = datas[i][11]
        if ip.count("#N/A") or ip.count("")>0:
            ip = '0'
        elif ip =="白名单用户":
            ip = '20'
        elif int(ip) > 100:
            ip = '40'


        compar_his_contacts =datas[i][12]
        if  compar_his_contacts.count("无重复") >0 or compar_his_contacts.count("#N/A") >0 or  compar_his_contacts.count("") >0:
            compar_his_contacts = '0'

        devices_num = datas[i][13]
        if  devices_num.count("#N/A")>0  or devices_num.count("")>0 :
            devices_num = '0'



        tel_realy = datas[i][14]
        if tel_realy.count("#N/A") >0 or tel_realy.count("否") >0 or tel_realy == '' or tel_realy == "0":
            tel_realy = '0'
        elif tel_realy.count("真实") >0 or tel_realy.count("是")>0 or tel_realy.count("*")>0 or tel_realy.count("实名认证"):
            tel_realy = '1'
        else:
            tel_realy = '1'

        is_has_call_platform = datas[i][15]
        if is_has_call_platform.count("未呼叫") >0 or is_has_call_platform.count("#N/A") > 0 or is_has_call_platform == '' :
            is_has_call_platform ='0'

        is_has_call_famliy =datas[i][16]
        if is_has_call_famliy.count("#N/A") >0 or is_has_call_famliy.count("无") >0 or is_has_call_famliy.count('未呼叫') >0 or is_has_call_famliy == '':
            is_has_call_famliy = '0'
            #'2.68231587239071' sheet1
            #112.177125193199   未还
        elif is_has_call_famliy.count("有") > 0:
            is_has_call_famliy = '1'

        is_has_call_not_family = datas[i][17]
        if is_has_call_not_family.count("#N/A") > 0 or is_has_call_not_family.count('未呼叫') >0 or is_has_call_not_family== '':
            is_has_call_not_family = '0'
        elif is_has_call_not_family.count("有") > 0:
            is_has_call_not_family = '1'

        is_tel_shutdown = datas[i][18]
        if is_tel_shutdown.count("#N/A")>0 or is_tel_shutdown.count("未出现")>0 or is_tel_shutdown == '':
            is_tel_shutdown = '0'

        compar_to_app = datas[i][19]
        if compar_to_app.count("#N/A")>0 or compar_to_app == '' :
            compar_to_app = '56.3253855773239'

        two_minute =datas[i][20]
        if two_minute.count("#N/A")>0 or two_minute == '' :
            two_minute = '62.5916103744475'

        call_num = datas[i][21]
        if call_num.count("#N/A")>0 or call_num == '':
            call_num ='242.649383127709'

        insert_sql="\
           insert into test_model_predict(id,tab,iCard,tel,sex,loan_money,loan_periods,\
           overdue_day,contact_num,call_rec_num,age,paltform_num,ip_reg_num,compar_histroy_contacts,device_num,tel_realy,\
            is_has_call_platfrom,is_has_call_family,is_has_call_not_family,is_tel_shutdown,compar_to_app,two_minute,call_num)VALUES (\
            null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')\
        "%(tab,iCard,tel,sex,loan_moeny,loan_periods,overdue_day,contact_num,call_rec_num,
             age,platform_num,ip,compar_his_contacts,devices_num,tel_realy,is_has_call_platform,is_has_call_famliy,
             is_has_call_not_family,is_tel_shutdown,compar_to_app,two_minute,call_num)
        print("============")
        print(insert_sql)
        con_mysql(insert_sql)




#处理年龄
def to_age(agestr):
    age_old = int(agestr)
    year = int(datetime.datetime.now().year)
    age = year - age_old
    return str(age)

#日期处理函数        
def  to_date(date):
    date += " 00:00:00"
    #转换成时间数组
    timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    date , nm = str(timestamp).split(".")
    return date


if  __name__ == "__main__":
    pre_data()
    # test()

