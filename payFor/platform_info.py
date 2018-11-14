import json

import pymysql
import requests
    #数据库驱动
def con_mysql(sql):
            try:
                # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
                conn = pymysql.connect(host='117.34.95.100', user='python', passwd='zhishen1234', db='python', port=3306, charset='utf8')
                cur = conn.cursor()  # 获取一个游标
                cur.execute(sql)
                conn.commit()
                cur.close()  # 关闭游标

            except  Exception:

                print("sql 数据库插入异常 ----",sql)
                conn.rollback()
            conn.close()  # 释放数据库资源

def get_info():
    url = "http://console.saas.zhishensoft.com/api/v2/OuputCusAction/ecology_pass"
    data = {'sign': '3ab7873060b6de9ca93b664e752bca6f',
            'search_type':'stq',
            'search_id': 10005,
            'user_status': -97
            }
    r = requests.post(url,  data = data)
    info = json.loads(r.text)
    flag = info.get('success')
    if flag == True:
        print("信息请求成功！")
        datas =  info['data']
        # print(datas)
        for i in range(len(datas)):

            mobile = datas[i]['mobile']
            list  = datas[i]['password']
            # print(mobile +" ---" +datas[i]['password'])

            for  i in range(len(list)) :
                 pid = list[i]
                 sql ="insert into app_ppd_spider (id,mobile,password)VALUES ((select replace(uuid(),'-','')),'"+mobile+"','"+pid+"')"
                 print(sql)
                 con_mysql(sql)
if __name__ =="__main__":
    get_info()


