import requests
from  selenium import  webdriver
import pymysql
import  time

def con_mysql(sql):
    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='python', port=3306, charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
        return data
    except  Exception:
        print("sql 数据库插入异常 ----", sql)
def login_rrd():
    url="https://www.loanrenrendai.com/loginPage.action"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="j_username"]').send_keys()
    driver.find_element_by_xpath('//*[@id="J_pass_input"]').send_keys()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="login_btn"]').click()
    time.sleep(10)
    path = "F:/pics/"

    driver.save_screenshot()
def save_images():
    for i in range(1,4001):
        respon = requests.get('https://www.loanrenrendai.com/image.jsp?0.5716016776094472')
        path="F:/pics/%s.png"%str(i)
        with open(path,'wb') as f:
            print("保存图片---")
            print("保存路径======》》》"+path)
            f.write(respon.content)

if __name__ == "__main__":
    # login_rrd()
    save_images()