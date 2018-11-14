import requests
import pymysql

def test_model_data():
    sql ="SELECT t.mobile,t.idCard ,t.uname FROM `test_01` t  "
    data = con_mysql(sql)
    for i in range(0,len(data)):

        print(data[i][0]+'-----------'+data[i][1])
        # print(d)

        header={
            "Content-Type" : "charset=UTF-8"
        }
        # url = "http://test.tianxingshuke.com/api/rest/riskTip/blackV2?account=test_ejprv&accessToken=f65ce0dff4fe4bae8e204f2610b9fb59&mobile=%s"%str(data[i][0])
        url ='http://test.tianxingshuke.com/api/rest/riskTip/blackInfo?account=test_ejprv&accessToken=f65ce0dff4fe4bae8e204f2610b9fb59&idCard=%s&name=%s'%(str(data[i][1]),str(data[i][2]))
        resp = requests.get(url,headers=header)
        respon_data = resp.text
        # upSql = "UPDATE test_01 set datas ='%s' where mobile='%s' and  idCard='%s'  "%(respon_data,str(data[i][0]),str(data[i][1]))
        upSql = "UPDATE test_01 set dataA ='%s' where mobile='%s' and  idCard='%s'  "%(respon_data,str(data[i][0]),str(data[i][1]))
        print("=========更新数据==========")
        print(upSql)
        con_mysql(upSql)


def con_mysql(sql):
    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='admin', db='test_model', port=3306, charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        # conn.commit()
        return data

    except  Exception:
        print("sql 数据库插入异常 ----", sql)


if __name__ == "__main__":
    test_model_data()
