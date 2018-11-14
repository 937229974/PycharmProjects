# -*- coding: utf-8 -*-
import random
import re
import pymysql
from  selenium import  webdriver
from selenium.webdriver.common.action_chains import *
import  time
from selenium.webdriver.common.keys import Keys
class YM(object):
    # 数据库连接
    def con_mysql(self,sql):
        try:
            # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            conn = pymysql.connect(host='117.34.95.100', user='python', passwd='zhishen1234', db='python', port=3306, charset='utf8')
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
        driver.maximize_window()
        driver.get('http://zzd.fanzhoutech.com')
        driver.find_element_by_xpath('//*[@id="Account"]').send_keys('12345678')
        driver.find_element_by_xpath('//*[@id="Password"]').send_keys('123qwe')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="Password"]').send_keys(Keys.ENTER)
        time.sleep(2)
        driver.get('http://zzd.fanzhoutech.com/admin/applyform/list')
        time.sleep(10)
        s = "y"
        if s == "y" :
            falg = False
            if falg:
                self.auto_pn(pn=26)
                self.get_list(pn=26)
            else:
                self.get_list(pn=1)
        else:
            driver.quit()
        time.sleep(10)

    def auto_pn(self, pn):
        for i in range(1, pn + 1):
            try:  # //*[@id="borrow-grid"]/div/a[3]/span
                driver.find_element_by_xpath('//*[@id="borrow-grid"]/div/a[3]/span').click()
                print("---------------------正在爬去%s页--------" % str(pn))
                time.sleep(3)
            except:
                print('------任务完成-----')

    def  get_list(self,pn):
        print("---------------正在爬取%s 页--------------------"%str(pn))
        trs = driver.find_elements_by_xpath('//*[@id="dategrid"]/tbody/tr')
        print(len(trs))

        for i in range(0, len(trs)):
            #/html/body/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/table/tbody/tr[1]/td[3]/br
            # no = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/table/tbody/tr[%s]/td[3]/br'%str(i+1)).text
            # print(no)
            driver.find_element_by_xpath('//*[@id="dategrid"]/tbody/tr[%s]/td[10]/a' %str(i+1)).click()
            time.sleep(2)

            #切换句柄
            driver.switch_to.window(driver.window_handles[-1])
            no = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[2]/div[4]/span[2]').text
            no = re.findall(r'\d+',no)
            id = no[0]
            try:
                self.get_info(id)
            except:
                print("当前信息异常-----")
            driver.close()#关闭当前句柄
            #移动句柄
            driver.switch_to.window(driver.window_handles[0])

        #爬虫翻页
        try:
            pn  += 1;
            print("爬虫翻页%s==================================="%str(pn))
            #
            driver.find_element_by_xpath('//*[@id="dategrid_pagination_info_next"]/span').click()
            time.sleep(3)
            self.get_list(pn)
        except:
            falg = input("爬虫终止，是否继续[y/n]")
            if falg =="y":
                self.get_list(pn)
            else:
                print('爬虫退出！！！')
                driver.quit()


    def  get_info(self,id):
        # print(id)
        # #获取基础信息

        lis = driver.find_elements_by_xpath('//*[@id="myTab"]/li')
        for i in range(0,len(lis)):#/html/body/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/ul/li
            time.sleep(2)
            try:
                title = driver.find_element_by_xpath('//*[@id="myTab"]/li[%s]/a'% str(i+1)).text
                #print(title)
            except:
                continue
            if title == "申请单详情":
                driver.find_element_by_xpath('//*[@id="myTab"]/li[%s]' % str(i+1)).click()
                time.sleep(1)
                print('===========申请单详情====================')
                self.get_base_info(id)
            elif title == "综合报告":
                driver.find_element_by_xpath('//*[@id="myTab"]/li[%s]' % str(i+1)).click()
                driver.implicitly_wait(5)
                print('===========综合报告====================')
                #通话记录获取
                try:
                    self.get_order_info(id)
                except:
                    pass
            elif title == "认证信息":
                driver.find_element_by_xpath('//*[@id="myTab"]/li[%s]' % str(i+1)).click()
                time.sleep(1)
                print('===========认证信息====================')
                self.get_contact(id)
            elif title == "详细数据清单":
                driver.find_element_by_xpath('//*[@id="myTab"]/li[%s]' % str(i+1)).click()
                time.sleep(2)
                print('===========详细数据清单====================')
                self.more_tel_record(id)
            elif title == "支付宝报告":
                driver.find_element_by_xpath('//*[@id="myTab"]/li[%s]' % str(i+1)).click()
                time.sleep(1)
                print('===========支付宝报告====================')

                #切换iframe
                driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="myTab_example10"]/iframe'))
                self.zfb_base_info(id)
                self.bank_info(id)
                #切回到住内容
                driver.switch_to.default_content()
            elif title == "淘宝数据报告":
                driver.find_element_by_xpath('//*[@id="myTab"]/li[%s]' % str(i)).click()
                time.sleep(1)
                print('===========淘宝数据报告====================')

                self.tb_address(id)
            elif title == "手机通讯录":
                driver.find_element_by_xpath('//*[@id="myTab"]/li[%s]' % str(i)).click()
                time.sleep(1)
                print('===========手机通讯录====================')
                self.contact_list(id)
            elif title == "跟踪信息":
                driver.find_element_by_xpath('//*[@id="myTab"]/li[%s]' % str(i)).click()
                time.sleep(1)
                print('===========跟踪信息====================')


    #获取基础信息
    def get_base_info(self,no):
        uname = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]').text
        zmf = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[2]/div[1]/span[2]').text
        tel = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[2]/div[2]/div[2]').text
        iCrad = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[2]/div[4]/span[2]').text
        address = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[2]/div[5]/span[2]').text
        address_detail = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[2]/div[6]/span[2]').text
        try:
            weChart = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[2]/div[7]/span[2]').text
        except:
            weChart = ''
        try:
            company_name = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[2]/div[8]/span[2]').text
        except:
            company_name = ''
        try:
            company_address = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[2]/div[9]/span[2]').text
        except:
            company_address = ''
        try:
            company_tel = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[2]/div[10]/span[2]').text
        except:
            company_tel = ''
        try:
            income = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[2]/div[11]/span[2]').text
        except:
            income = ''
        print(uname, zmf, tel, iCrad, address, address_detail, weChart, company_name, company_address, company_tel,
              income)

        imgZ = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[6]/div/div[1]/div[1]/img').get_attribute('src')
        imgF = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[6]/div/div[2]/div[1]/img').get_attribute('src')
        imgPerson = driver.find_element_by_xpath('//*[@id="myTab_example1"]/div[6]/div/div[3]/div[1]/img').get_attribute('src')

        sql ="insert into YM_CUSTOM VALUES ('"+no+"','"+uname+"','"+zmf+"','"+tel+"','"+iCrad+"'," \
             "'"+address+"','"+address_detail+"','"+weChart+"','"+company_name+"','"+company_address+"'," \
            " '"+company_tel+"','"+income+"','"+imgZ+"','"+imgF+"','"+imgPerson+"')"
        print(sql)
        self.con_mysql(sql)

    #获取紧急联系人信息
    def get_contact(self,no):
        driver.find_element_by_xpath('//*[@id="myTab"]/li[2]/a').click()
        time.sleep(1)
        #父亲                                    //*[@id="myTab_example2"]/div[2]/div[1]/span[1]
        ralation = driver.find_element_by_xpath('//*[@id="myTab_example2"]/div[2]/div[1]/span[1]').text
        ralation = ralation.replace("：","")
        tel = driver.find_element_by_xpath('//*[@id="myTab_example2"]/div[2]/div[1]/span[2]').text
        sql ="insert into YM_CONTACT VALUES ((select replace(UUID(),'-','')),'"+no+"','"+ralation+"','"+tel+"')"
        print(sql)
        self.con_mysql(sql)
        #母亲
        ralation2 = driver.find_element_by_xpath('//*[@id="myTab_example2"]/div[2]/div[2]/span[1]').text
        ralation2 = ralation2.replace("：","")
        tel2 =  driver.find_element_by_xpath('//*[@id="myTab_example2"]/div[2]/div[2]/span[2]').text
        sql2 = "insert into YM_CONTACT VALUES ((select replace(UUID(),'-','')),'" + no + "','" + ralation2 + "','" + tel2 + "')"
        print(sql2)
        self.con_mysql(sql2)
        #配偶、情侣
        ralation3 = driver.find_element_by_xpath('//*[@id="myTab_example2"]/div[2]/div[3]/span[1]').text
        ralation3 = ralation3.replace("：","")
        tel3 = driver.find_element_by_xpath('//*[@id="myTab_example2"]/div[2]/div[3]/span[2]').text
        sql3 = "insert into YM_CONTACT VALUES ((select replace(UUID(),'-','')),'" + no + "','" + ralation3 + "','" + tel3 + "')"
        print(sql3)
        self.con_mysql(sql3)
        #同事
        ralation4 = driver.find_element_by_xpath('//*[@id="myTab_example2"]/div[2]/div[4]/span[1]').text
        ralation4 = ralation4.replace("：","")
        tel4 = driver.find_element_by_xpath('//*[@id="myTab_example2"]/div[2]/div[4]/span[2]').text
        sql4 = "insert into YM_CONTACT VALUES ((select replace(UUID(),'-','')),'" + no + "','" + ralation4 + "','" + tel4 + "')"
        print(sql4)
        self.con_mysql(sql4)


    def more_tel_record(self,id):#/html/body/div[1]/div[6]/div[2]/table[1]/tbody/tr[180]/td[1]
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="myTab_example9"]/iframe'))
                                             #/html/body/div[1]/div[6]/div[2]/table[1]/tbody/tr[3]
        trs  = driver.find_elements_by_xpath('/html/body/div/div[3]/div[2]/table[1]/tbody/tr')
        # print(len(trs))                             #/html/body/div[1]/div[6]/div[2]/table[1]/tbody/tr[3]/td[1]
        for j in range(3, len(trs) + 1):

            type = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table[1]/tbody/tr[%s]/td[1]'% str(j)).text
            # 电话
            try:                                   #
                tel = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table[1]/tbody/tr[%s]/td[2]' % str(j)).text
            except:
                tel = ''
            # 通话日期
            call_date = driver.find_element_by_xpath(
                '/html/body/div/div[3]/div[2]/table[1]/tbody/tr[%s]/td[3]' % str(j)).text
            # 通话时间
            call_time = driver.find_element_by_xpath(
                '/html/body/div/div[3]/div[2]/table[1]/tbody/tr[%s]/td[4]' % str(j)).text
            belong_to_address = driver.find_element_by_xpath(
                '/html/body/div/div[3]/div[2]/table[1]/tbody/tr[%s]/td[5]' % str(j)).text

            call_cost = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table[1]/tbody/tr[%s]/td[6]'% str(j)).text
            sql = "insert into YM_MORE_TEL_RECORD VALUES  ((SELECT replace(uuid(),'-','')),'"+id+"','"+tel+"','"+type+"','"+call_date+"','"+call_time+"','"+belong_to_address+"','"+call_cost+"')"
            print(sql)
            self.con_mysql(sql)
        driver.switch_to.default_content()


    def contact_list(self,no):
        print("--------------通讯记录列表--------------")
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="myTab_example4"]/iframe'))
        divs = driver.find_elements_by_xpath('//*[@id="divAddressBook"]/div')
        for i in range(0,len(divs)):                 #//*[@id="divAddressBook"]/div[4]/ul/li //*[@id="divAddressBook"]/div[8]/ul/li
            try:
                name_tel = driver.find_element_by_xpath('//*[@id="divAddressBook"]/div[%s]'%str(i+1)).text
                if name_tel != "":
                    name, tel = name_tel.split("：")
                    sql ="insert into YM_CONTACT_LIST VALUES ((SELECT REPLACE(UUID(),'-','')),'"+no+"','"+name+"','"+tel+"')"
                    print(sql)
                    self.con_mysql(sql)
            except:
                continue
        driver.switch_to.default_content()
    def get_order_info(self,id):
            print('负债信息-----')
               #
            iframe = driver.find_element_by_css_selector('#myTab_example3 > iframe')
            driver.switch_to.frame(iframe)
       #总负债//html/body/div[1]/div[5]/div[2]/table[1]/tbody/tr[2]/td
            debt_money_amount = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/table[1]/tbody/tr[2]/td').text
            print(debt_money_amount)
            trs = driver.find_elements_by_xpath('/html/body/div[1]/div[5]/div[2]/table[1]/tbody/tr')
            for i in range(3,len(trs)):#第三行开始
                #借款金额                                     /html/body/div[1]/div[5]/div[2]/table[1]/tbody/tr[4]/td[1]
                borrow_money = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/table[1]/tbody/tr[%s]/td[1]'%str(i+1)).text
                #归还日期
                back_date  = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/table[1]/tbody/tr[%s]/td[2]'%str(i+1)).text
                #是否逾期
                is_has_overdure = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/table[1]/tbody/tr[%s]/td[3]/span'%str(i+1)).text
                #处置 状态
                dispose_status = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/table[1]/tbody/tr[%s]/td[4]/span'%str(i+1)).text

                sql = "insert into YM_YPZ_REPORT values ((select replace(uuid(),'-','')),'"+id+"','"+borrow_money+"','"+back_date+"','"+is_has_overdure+"','"+dispose_status+"','"+debt_money_amount+"')"
                print(sql)
                self.con_mysql(sql)
            driver.switch_to.default_content()


    def zfb_base_info(self,id):
        #用户名称
        uname = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[2]').text
        # 淘宝名称
        tb_name = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[4]').text
        # 淘宝身份证
        tb_icard = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[6]').text
        #电话
        tel= driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[8]').text
        #花呗信用
        hb_credited = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[8]').text
        #花呗可用
        hb_use_credited = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[4]').text
        #下个月还款
        next_month_backM = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[4]').text
        #账户余额
        account_balance=driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[8]').text
        #余额宝总额
        yeb = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[2]').text
        #余额收益
        ye_income = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[4]').text
        #注册时间
        reg_date = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[6]').text
        #安全等级
        safe_grade = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[6]').text
        sql = "insert into YM_ZFB_INFO VALUES ((select replace(uuid(),'-','')),'"+id+"','"+uname+"','"+tb_name+"'," \
            "'"+tb_icard+"','"+tel+"','"+hb_credited+"','"+hb_use_credited+"','"+next_month_backM+"','"+account_balance+"'," \
                "'"+yeb+"','"+ye_income+"','"+reg_date+"','"+safe_grade+"')"
        print(sql)
        self.con_mysql(sql)
    def bank_info(self,id):
        trs = driver.find_elements_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr')
        for i in range(0,len(trs)):
            try:
                uname = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr[%s]/td[2]' %str(i+1)).text
                open_address = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr[%s]/td[4]' %str(i+1)).text
                bank_type = driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/table/tbody/tr[%S]/td[6]" %str(i+1)).text
                tel = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr[%s]/td[8]'% str(i+1)).text
                pay_fast = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr[%s]/td[10]'%str(i+1)).text
                bank_end_four = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr[%s]/td[12]'%str(i+1)).text
                sql =" insert into YM_BANK_INFO values((select replace(uuid(),'-','')),'"+id+"','"+uname+"','"+open_address+"','"+bank_type+"','"+tel+"','"+pay_fast+"','"+bank_end_four+"')"
                print(sql)
                self.con_mysql(sql)
            except:
                continue
    def tb_address(self,id):
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="myTab_example12"]/iframe'))
                                            #/html/body/div/div[3]/div[2]/table/tbody/tr[1]
        trs = driver.find_elements_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr')
        for i in range(2,len(trs)):
                                                 #/html/body/div/div[3]/div[2]/table/tbody/tr[3]/td[1]
            uname =driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr[%s]/td[1]' %str(i +1)).text
            belong_to =driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr[%s]/td[2]' %str(i +1)).text
            address =driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr[%s]/td[3]' %str(i +1)).text
            address_no =driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr[%s]/td[4]'%str(i +1)).text
            tel =driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr[%s]/td[5]' %str(i +1)).text
            default_address =driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table/tbody/tr[%s]/td[6]' %str(i +1)).text
            sql ="insert into YM_TB_ADDRESS VALUES ((select replace(uuid(),'-','')),'"+id+"','"+uname+"'," \
                "'"+belong_to+"','"+address+"','"+address_no+"','"+tel+"','"+default_address+"')"
            print(sql)
            self.con_mysql(sql)
        driver.switch_to.default_content()
if __name__ == "__main__":
    j = YM()
    j.login()