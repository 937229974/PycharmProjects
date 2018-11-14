# -*- coding: utf-8 -*-
import pymysql
from flask import Flask, request, jsonify

app = Flask(__name__)


# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )


@app.route('/addTaskQueue', methods=['POST'])
def register():
    mobile = request.form["mobile"]
    pid = request.form["password"]
    platform = request.form["platform"]
    grade = request.form["grade"]
    print(mobile)
    print(pid)
    print(platform)
    print(grade)
    source = "all"
    if request.form["source"] != None:
        req = request.form["source"]

        if req == "xdy":
            source = "xdy"
        elif req == "dc":
            source = "dc"
        elif req == "gn":
            source = "gn"
        elif req == "all":
            source = "all"

    sql = "insert into app_ppd_spider (id,mobile,password,source,platform_id,grade)VALUES ((select replace(uuid(),'-','')),'" + mobile + "','" + pid + "','" + source + "','" + platform + "','" + grade + "')"
    print(sql)
    flag = con_mysql_python(sql)
    if flag == True:

        dict = {"success": "true",
                "code": 200,
                "msg": "成功"}
    else:
        dict = {"success": "false",
                "code": 400,
                "msg": "失败"}



    return jsonify(dict)

def con_mysql_python(sql):
        try:
            # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn = pymysql.connect(host='117.34.95.100', user='python', passwd='zhishen1234', db='python', port=3306,
                                   charset='utf8')
            # conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='python', port=3306,
            #                        charset='utf8')
            cur = conn.cursor()  # 获取一个游标
            cur.execute(sql)
            data = cur.fetchone()
            cur.close()  # 关闭游标
            conn.close()  # 释放数据库资源
            return True

        except  Exception:
            return False


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')