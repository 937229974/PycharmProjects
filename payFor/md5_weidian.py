

import hashlib
import json
import  time

import pymysql
import requests

    #数据库驱动
def con_mysql(sql):
        try:
            # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn = pymysql.connect(host='localhost', user='root', passwd='admin', db='test', port=3306, charset='utf8')
            # conn = pymysql.connect(host='117.34.95.100', user='python', passwd='zhishen1234', db='python1', port=3306, charset='utf8')
            cur = conn.cursor()  # 获取一个游标
            cur.execute(sql)
            conn.commit()
            data = cur.fetchall()
            cur.close()  # 关闭游标
            conn.close()  # 释放数据库资源
            return  data

        except  Exception:
            print("sql 数据库插入异常 ----",sql)
def post_data():
    sql ="SELECT * FROM `mk-001`"
    data = con_mysql(sql)
    for i in  range(0,len(data)):
        mobile = data[i][0]

        str_time = time.time()
        str_time1 = str(str_time).split(".")
        key = "liweimin"
        auth_key = "%s%s%s" % (mobile, str_time1[0], key)
        # 创建md5对象
        hl = hashlib.md5()
        hl.update(auth_key.encode(encoding='utf-8'))
        # print('MD5加密前为 ：' + auth_key)
        # print('MD5加密后为 ：' + hl.hexdigest()[5:15])

        dict = {
            'authkey': hl.hexdigest()[5:15],
            'mobile': mobile,
            'timestamp': str_time1[0]
        }

        url = 'http://serv.weidab.com/rest/helper/search'
        html = requests.post(url, dict)
        data_resp = json.loads(html.text)
        # print("===============================")
        # print(data_resp)
        sql_up = 'update `mk-001` SET json = "%s" where mobile="%s";'%(data_resp,mobile)
        print(sql_up)
        con_mysql(sql_up)

if __name__ =="__main__":
    post_data()