# -*- coding: utf-8 -*-
import random
import re
import pymysql
from  selenium import  webdriver
from selenium.webdriver.common.action_chains import *
import  time
class qxb(object):
    # 数据库连接
    def con_mysql(self,sql):
        try:
            # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn = pymysql.connect(host='localhost', user='root', passwd='admin', db='test', port=3306, charset='utf8')
            cur = conn.cursor()  # 获取一个游标
            cur.execute(sql)
            cur.close()  # 关闭游标
            conn.close()  # 释放数据库资源
            return True
        except  Exception:
            print("当前信息已存在，继续下一条信息爬去 sql --------------",sql)
            return  False

    # 页面登录
    def login(self):
        global driver
        driver = webdriver.Firefox()
        driver.maximize_window()##http://www.qixin.com/search?page=1&sorter=4
        driver.get('https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=101286342&redirect_uri=http%3A%2F%2Fwww.qixin.com%2Floginsuccess.html%3Freturn_url%3D%252Fauth%252Fthird%252F%253Freturn_url%253D%25252Fsearch%25253Fpage%25253D100%252526sorter%25253D4&scope=get_user_info&response_type=code')#/auth-qq?return_url=%2Fauth%2Fthird%2F%3Freturn_url%3D%252Fsearch%253Fpage%253D100%2526sorter%253D4
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="ptlogin_iframe"]'))
        driver.find_element_by_xpath('//*[@id="img_out_937229974"]').click()
        driver.switch_to.default_content()
        s = input('是否继续：[y/n]')
        if s == "y":
            self.auto_info(pn=312)
        else:
            driver.quit()

    def auto_info(self,pn):
        driver.get('http://www.qixin.com/search?page=%s&sorter=4'%str(pn))
        divs = driver.find_elements_by_xpath('/html/body/div[5]/div/div[1]/div[3]/div[2]/div')
        print("----------------------------")
        print(len(divs))
        if len(divs) == 0 :
            s = input('是否继续：[y/n]')
            if s == 'n':
                driver.quit()
        divss = driver.find_elements_by_xpath('/html/body/div[5]/div/div[1]/div[3]/div[2]/div')
        for i in range(0, len(divss)):  # /html/body/div[5]/div/div[1]/div[3]/div[2]/div[1]
            cName = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[1]/div[3]/div[2]/div[%s]/div[2]/div[1]/div[1]/a' % str(i + 1)).text
            uName = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[1]/div[3]/div[2]/div[%s]/div[2]/div[1]/div[2]' % str(i + 1)).text
            address = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[1]/div[3]/div[2]/div[%s]/div[2]/div[1]/div[3]/span' % str(i + 1)).text
            status = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[1]/div[3]/div[2]/div[%s]/div[2]/div[1]/div[5]/span' % str(i + 1)).text
            regMoney = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[1]/div[3]/div[2]/div[%s]/div[3]/div[1]'% str(i + 1)).text
            regDate = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[1]/div[3]/div[2]/div[%s]/div[3]/div[2]'% str(i + 1)).text

           # print(cName, uName, address, status,regMoney,regDate)

            sql = "insert into qi_xin_bao VALUES (null,'"+cName+"','"+uName+"','"+address+"','"+status+"','"+regMoney+"','"+regDate+"')"
            print(sql)
            self.con_mysql(sql)



        try:
           pn += 1
           print("==正在翻页%s============ "%str(pn))
           time.sleep(random.randint(5,8))
           self.auto_info(pn)

        except:
            s = input('是否继续：[y/n]')
            if s == "y":
                self.auto_info(pn)
            else:
                 driver.quit()
if __name__ == "__main__":
    x= qxb()
    x.login()