from  lxml import html
import pymysql

    #数据库驱动
import requests


def con_mysql(sql):
    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='admin', db='test', port=3306, charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return  data

    except  Exception:
        print("sql 数据库插入异常 ----",sql)
def coding():
     sql ='''
            select column_name,data_type from information_schema.columns 
            where table_name='app_spider_test' and table_schema='test'
     '''
     data = con_mysql(sql)
     for i in range(0,len(data)):
          print(data[i][0]+'---------'+data[i][1])

def test():
    res = requests.get('http://m.xinshubao.net/0/158/9222373.html')
    # print(res.text)
    response = html.fromstring(res.text)
    texts = response.xpath('.//*[@id="nr1"]/text()')
    for i in range (0,len(texts)):
        print(texts[i])
    #//*[@id="nr_body"]/div[8]/a[3]
    href =response.xpath('.//*[@id="nr_body"]/div[8]/a[3]/text()')
    print(href)


def auto_conding():
    pass




if __name__ =="__main__":
    coding()
    # test()