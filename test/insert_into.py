import pymysql


def conn_mysql(sql):

    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='117.34.95.100', user='python', passwd='zhishen1234', db='python', port=3306, charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        cur.execute(sql)
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
    except  Exception:
        print("异常----"+sql)
def read_txt():
    with open("D:/mmmm.txt") as f:
        s = f.readlines()
        # print(s)
        for line in s:
            # print(line)
            tel ,pid = line.split("	")
            source ='all'
            platform = 'ppd'
            grade = '1'
            sql = "insert into app_ppd_spider (id,mobile,password,source,platform_id,grade)VALUES ((select replace(uuid(),'-','')),'" + tel + "','" + pid + "','" + source + "','" + platform + "','" + grade + "');"
            print(sql)
            conn_mysql(sql)
read_txt()