# -*- coding: utf-8 -*-
import pymysql
from  selenium import  webdriver
import  time



class liantong(object):
    # 规则获取
    def conn_mysql(self):
        # 数据库查询操作
        try:
            # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn = pymysql.connect(host='47.93.218.144', user='wangbo', passwd='123456', db='wangbo', port=3306,
                                   charset='utf8')
            cur = conn.cursor()  # 获取一个游标
            cur.execute('select count(1) from tb_custom  t where t.uname="admin" and pass ="123456"')
            result = cur.fetchall()
            rule = result[0][0]
            cur.close()  # 关闭游标
            conn.close()  # 释放数据库资源
            return  rule
        except  Exception:
            print("发生异常")

    def login(self):
        #
        global driver
        driver = webdriver.PhantomJS(executable_path="D:\\phantomjs\\bin\\phantomjs.exe")
        # print('-------------------')
        # driver = webdriver.Firefox()
        # driver.get('https://uac.10010.com/portal/mallLogin.jsp?redirectURL=http://www.10010.com')
        driver.get('https://uac.10010.com/portal/homeLogin')

        time.sleep(5)                         #//*[@id="loginbox"]/iframe
        # ifram = driver.find_element_by_xpath('//*[@id="loginbox"]/iframe')
        # driver.switch_to.frame(ifram)
        '''
        1799182912@qq.com 741852963
        gd105@163.com liantong
        273924550@qq.com    830712553
        '''
        u = input('请输入登录用户名：')
        p = input('请输入登录密码：')
        driver.find_element_by_xpath('//*[@id="userName"]').clear()
        driver.find_element_by_xpath('//*[@id="userName"]').send_keys('1799182912@qq.com')
        driver.find_element_by_xpath('//*[@id="userPwd"]').clear()
        driver.find_element_by_xpath('//*[@id="userPwd"]').send_keys('741852963')
        time.sleep(3)
        try:
           driver.find_element_by_xpath('//*[@id="randomCKCode"]').click()
           code= input('请输入验证码：')
           driver.find_element_by_xpath('//*[@id="userCK"]').send_keys(code)
        except:
            pass
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="login1"]').click()
        time.sleep(2)
        driver.get('https://upay.10010.com/npfweb/npfcellweb/phone_recharge_fill.htm')
        time.sleep(5)
        #读取号码
        read = open("haoma.txt", 'r')  # 返回一个文件对象
        lines = read.readlines()  # 调用文件的 readline()方法
        #print(lines)
        #read.readable()
        for line in lines:
            self.atuo_info(line)

        read.close()
        print('''
                 --------程序结束-------
                 感谢使用！
              ''')
        driver.quit()


    def  atuo_info(self,num):

        driver.find_element_by_xpath('//*[@id="number"]').clear()
        driver.find_element_by_xpath('//*[@id="number"]').send_keys(num)
        driver.find_element_by_xpath('//*[@id="cellform"]/dl[1]/dd/div/input[9]').click()
        time.sleep(1)
        uname = driver.find_element_by_xpath('//*[@id="cellform"]/dl[2]/dd').text
        money = driver.find_element_by_xpath('//*[@id="cellform"]/dl[1]/dd/div/span[2]').text
        money = money.replace('欠费金额：','')
        money = money.replace('元','')
        tel = str(int(num))
        if money == '查询应交费用失败，请稍后重试！':
            info = tel
            info +='超时|超时'
        else:
            info = tel
            info += uname
            info +='|'
            info += money
        print(info)
        with open("newhaoma.txt", "w") as f:
            f.write(info)
            f.write("\n")
        f.close()
        time.sleep(1)

#主方法登录
if __name__ == "__main__":

    print(
    '''
      联系方式： QQ： 937229974
    '''
    )
    L = liantong()

    # result = L.conn_mysql()
    # if result == 1 :
    L.login()