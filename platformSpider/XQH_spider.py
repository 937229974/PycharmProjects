# -*- coding: utf-8 -*-
import random
import re
import pymysql
from  selenium import  webdriver
from selenium.webdriver.common.action_chains import *
import  time
class xqh(object):
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
        driver.get('http://hua.xiangqianhua.com/xqh/Admin/')
        driver.find_element_by_xpath('//*[@id="Username"]').send_keys('cuishou666')
        driver.find_element_by_xpath('//*[@id="Password"]').send_keys('aa123aa456')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@class="button-1 login-button"]').click()
        driver.get('http://hua.xiangqianhua.com/xqh/Admin/Borrow/List')
        falg = True
        if falg :
            self.auto_pn(pn=26)
            self.get_order_info(pn=26)
        else:
            self.get_order_info(pn = 1)



    def get_order_info(self,pn):
        time.sleep(2)
        trs = driver.find_elements_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr')
        print(len(trs))
        for i in  range(0,len(trs)):
            #任务单编号
            orderNo = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[1]' %str(i+1)).text
            #代理商
            dl = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[2]' % str(i+1)).text
            #用户编号
            customNo = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[3]/span' % str(i+1)).text
            # 姓名
            uname = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[4]' % str(i+1)).text
            #备注
            remarks = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[5]' % str(i+1)).text
            #借款金额
            money = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[6]' % str(i+1)).text
            #借款类型
            type= driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[7]' % str(i+1)).text
            #逾期金额
            overdure_money = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[8]' % str(i+1)).text
            #滞纳金
            over_money = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[9]' % str(i+1)).text
            #逾期天数
            over_day = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[10]' % str(i+1)).text
            #申请状态
            apply_status = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[11]' % str(i+1)).text
            #审核状态#
            Audit_status = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[12]' % str(i+1)).text

            time.sleep(1)
            #获取任务单详细页面      #http://hua.xiangqianhua.com/xqh/Admin/Borrow/Edit/34123
            # new_window = 'http://hua.xiangqianhua.com/xqh/Admin/Borrow/'
            new_window = driver.find_element_by_xpath('//*[@id="borrow-grid"]/table/tbody/tr[%s]/td[13]/a'% str(i+1)).get_attribute('href')
            # time.sleep(2)
            print(new_window)
            #获取订单时间
            newhref = 'window.open("'+new_window+'")'
            driver.execute_script(newhref)
            driver.switch_to_window(driver.window_handles[-1])
            time.sleep(2)

            # #申请时间
            apply_date = driver.find_element_by_xpath('//*[@id="tab-info"]/div/div/div/div[18]/div[2]/div').text
            # print(apply_date)
            # #审核时间
            audit_date = driver.find_element_by_xpath('//*[@id="tab-info"]/div/div/div/div[18]/div[2]/div').text
            #放款时间
            loan_date = driver.find_element_by_xpath('//*[@id="tab-info"]/div/div/div/div[18]/div[2]/div').text
            #放款截止时间
            loan_end_date = driver.find_element_by_xpath('//*[@id="tab-info"]/div/div/div/div[18]/div[2]/div').text
            #借款天数
            brrow_day = driver.find_element_by_xpath('//*[@id="tab-info"]/div/div/div/div[7]/div[2]/div').text
            #服务费用
            service_cost = driver.find_element_by_xpath('//*[@id="tab-info"]/div/div/div/div[8]/div[2]/div').text
            #续借手续费
            procedures_cost = driver.find_element_by_xpath('//*[@id="tab-info"]/div/div/div/div[9]/div[2]/div').text
            sql = "insert into xqh_order values ('" + orderNo + "','" + dl + "','" + customNo + "','" + uname + "','" + remarks + "','" + money + "','" + type + "'," \
                        "'" + overdure_money + "','" + over_money + "','" + over_day + "','" + apply_status + "','" + Audit_status + "'" \
                        ",'"+apply_date+"','"+audit_date+"','"+loan_date+"','"+loan_end_date+"','"+brrow_day+"','"+service_cost+"','"+procedures_cost+"')"
            print(sql)
            flag = self.con_mysql(sql)
            #任务单编号是否存在
            if flag :
                self.get_detail_info(uname, customNo)
            time.sleep(1)


            #关闭当前窗口
            driver.close()
            #返回起始窗口
            driver.switch_to_window(driver.window_handles[0])
            time.sleep(2)

         #翻页
        try:#                             //*[@id="borrow-grid"]/div/a[3]
            driver.find_element_by_xpath('//*[@id="borrow-grid"]/div/a[3]/span').click()
            pn += 1
            print("---------------------正在爬去%s页--------" % str(pn))
            time.sleep(3)
            if pn < 28:
                self.get_order_info(pn=pn)
            else:

                print('-----------任务完成-------')

        except:
             print('------任务完成-----')
    def get_detail_info(self,uname,customNo):
        #历史借款
        self.brrow_history(uname)
        #个人信息
        self.peroson_info(customNo)
        #紧急联系人
        self.contact_person(customNo)
        #淘宝
        self.tao_bao(customNo)
        #通讯录
        self.more_tel(customNo)
        #银行卡
        self.bank_info(customNo)
        #融360
        self.rong_360(customNo)
        #黑名单信息
        self.blacklist(customNo)



    def blacklist(self,customNo):
        driver.find_element_by_xpath('//*[@id="borrow-edit"]/ul/li[10]/a').click()
        trs = driver.find_elements_by_xpath('//*[@id="creditwatch-grid"]/table/tbody/tr')
        for i in range(0,len(trs)):
            profession_type = driver.find_element_by_xpath('//*[@id="creditwatch-grid"]/table/tbody/tr/td[1]').text
            risk_type = driver.find_element_by_xpath('//*[@id="creditwatch-grid"]/table/tbody/tr/td[2]').text
            risk = driver.find_element_by_xpath('//*[@id="creditwatch-grid"]/table/tbody/tr/td[3]').text
            risk_grad= driver.find_element_by_xpath('//*[@id="creditwatch-grid"]/table/tbody/tr/td[4]').text
            date = driver.find_element_by_xpath('//*[@id="creditwatch-grid"]/table/tbody/tr/td[5]').text
            status = driver.find_element_by_xpath('//*[@id="creditwatch-grid"]/table/tbody/tr/td[6]').text
            zy_status = driver.find_element_by_xpath('//*[@id="creditwatch-grid"]/table/tbody/tr/td[7]').text
            yy_declare = driver.find_element_by_xpath('//*[@id="creditwatch-grid"]/table/tbody/tr/td[8]').text
            remarks = driver.find_element_by_xpath('//*[@id="creditwatch-grid"]/table/tbody/tr/td[9]').text
            sql = "insert into xqh_blacklist VALUES ((select replace(UUID(),'-',''))," \
                  "'"+customNo+"','"+profession_type+"','"+risk_type+"','"+risk+"','"+risk_grad+"','"+date+"'," \
                    "'"+status+"','"+zy_status+"','"+yy_declare+"','"+remarks+"')"
            print(sql)
            self.con_mysql(sql)


    def rong_360(self,customNo):#/xqh/Admin/Certifications/Rong360Report/19527
                                     #//*[@id="borrow-edit"]/ul/li[15]/a
        driver.find_element_by_xpath('//*[@id="borrow-edit"]/ul/li[15]/a').click()
        #风控分数
        score = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[1]/div[2]/div').text
        #报告连接
        try:
            href = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[2]/div/button').get_attribute('onclick')
            href = href[13:-2]
            url ="http://hua.xiangqianhua.com"+href
        except:
            url = ""
        try:
            #号码类型
            tel_type = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[3]/div[2]/div').text
            #身份证号码
            iCard = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[4]/div[2]/div').text
            #地址
            address = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[5]/div[2]/div').text
            #姓名
            uname = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[6]/div[2]/div').text
            #当前账户余额
            surplus = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[7]/div[2]/div').text
            #电话号码
            tel = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[8]/div[2]/div').text
            #入网时间
            reg_date = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[9]/div[2]/div').text
            #更新时间
            update_date = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[10]/div[2]/div').text
            #用户基本
            user_base = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[11]/div[2]/div').text
            #其他联系人号码
            other_tel = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[12]/div[2]/div').text
            #用户星级
            grap = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[13]/div[2]/div').text
            #用户实名状态
            realy_name_status = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[13]/div[2]/div').text
            #客户状态
            user_status = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[15]/div[2]/div').text
            #套餐名称
            set_meal = driver.find_element_by_xpath('//*[@id="tab-rong360Info"]/div/div/div/div[16]/div[2]/div').text
        except:
            tel_type=''
            iCard=''
            address=''
            uname = ''
            # 当前账户余额
            surplus = ''
            # 电话号码
            tel = ''
            # 入网时间
            reg_date = ''
            # 更新时间
            update_date = ''
            # 用户基本
            user_base = ''
            # 其他联系人号码
            other_tel = ''
            # 用户星级
            grap = ''
            # 用户实名状态
            realy_name_status = ""
            # 客户状态
            user_status = ''
            # 套餐名称
            set_meal = ''

        driver.find_element_by_xpath('//*[@id="borrow-edit"]/ul/li[9]/a').click()
        #芝麻分
        zmf = driver.find_element_by_xpath('//*[@id="tab-zhima"]/div/div/div/div/div[2]/div').text
        driver.find_element_by_xpath('//*[@id="borrow-edit"]/ul/li[11]/a').click()
        #反欺诈
        fanqz = driver.find_element_by_xpath('//*[@id="tab-antifraudsocre"]/div/div/div/div/div[2]/div').text

        sql ="insert into xqh_rong_360 VALUES ((select replace(UUID(),'-',''))," \
             "'"+customNo+"','"+score+"','"+url+"','"+tel_type+"','"+iCard+"','"+address+"','"+uname+"'," \
                "'"+surplus+"','"+tel+"','"+reg_date+"','"+update_date+"','"+user_base+"','"+other_tel+"'," \
                "'"+grap+"','"+realy_name_status+"','"+user_status+"','"+set_meal+"','"+zmf+"','"+fanqz+"')"
        print(sql)
        self.con_mysql(sql)



    def bank_info(self,customNo):
        driver.find_element_by_xpath('//*[@id="borrow-edit"]/ul/li[8]/a').click()
        bank_no = driver.find_element_by_xpath('//*[@id="tab-bankcard"]/div/div/div/div[1]/div[2]/div').text
        tel = driver.find_element_by_xpath('//*[@id="tab-bankcard"]/div/div/div/div[2]/div[2]/div').text
        bank_name = driver.find_element_by_xpath('//*[@id="tab-bankcard"]/div/div/div/div[3]/div[2]/div').text
        userName =driver.find_element_by_xpath('//*[@id="tab-bankcard"]/div/div/div/div[4]/div[2]/div').text
        iCrad =driver.find_element_by_xpath('//*[@id="tab-bankcard"]/div/div/div/div[5]/div[2]/div').text
        sql = "insert into xqh_bank VALUES(" \
              "(select replace(UUID(),'-','')),'" + customNo + "','" + bank_no + "','" + tel + "'," \
                "'"+bank_name+"','"+userName+"','"+iCrad+"')"
        print(sql)
        self.con_mysql(sql)

    def more_tel(self,customNo):
        driver.find_element_by_xpath('//*[@id="borrow-edit"]/ul/li[7]/a').click()
        trs = driver.find_elements_by_xpath('//*[@id="contacts-grid"]/table/tbody/tr')
        for i in range(0,len(trs)):
            uname = driver.find_element_by_xpath('//*[@id="contacts-grid"]/table/tbody/tr[%s]/td[1]'%str(i+1)).text
            tel = driver.find_element_by_xpath('//*[@id="contacts-grid"]/table/tbody/tr[%s]/td[2]'%str(i+1)).text
            sql = "insert into xqh_more_tel VALUES(" \
                  "(select replace(UUID(),'-','')),'"+customNo+"','"+uname+"','"+tel+"')"
            print(sql)
            self.con_mysql(sql)

    def tao_bao(self,customNo):
        driver.find_element_by_xpath('//*[@id="borrow-edit"]/ul/li[6]/a').click()
        #用户名称
        useName = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[1]/div[2]/div').text
        #昵称
        nickname  = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[2]/div[2]/div').text
        #性别
        sex = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[3]/div[2]/div').text
        #生日
        brithday = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[4]/div[2]/div').text
        #真实姓名
        realy_name = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[5]/div[2]/div').text
        #身份证号码
        iCrad = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[6]/div[2]/div').text
        #渠道
        channle = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[7]/div[2]/div').text
        #是否实名认证
        isHasRealyName = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[8]/div[2]/div').text
        #登录邮箱
        Email = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[9]/div[2]/div').text
        #绑定手机
        binding_tel = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[10]/div[2]/div').text
        #会员等级
        grade = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[10]/div[2]/div').text
        #成长值
        grow_vlaue = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[10]/div[2]/div').text
        #好评率
        review = driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[14]/div[2]/div').text
        #安全等级
        safety_factor =driver.find_element_by_xpath('//*[@id="tab-taobao"]/div/div/div/div[15]/div[2]/div').text
        sql = "insert into xqh_tao_bao value((SELECT  replace(UUID(),'-',''))," \
              "'"+customNo+"','"+useName+"','"+nickname+"','"+sex+"','"+brithday+"','"+realy_name+"','"+iCrad+"'," \
                "'"+channle+"','"+isHasRealyName+"','"+Email+"','"+binding_tel+"','"+grade+"','"+grow_vlaue+"','"+review+"','"+safety_factor+"')"
        print(sql)
        self.con_mysql(sql)


    def contact_person(self,customNo):
        driver.find_element_by_xpath('//*[@id="borrow-edit"]/ul/li[4]/a').click()
        uname = driver.find_element_by_xpath('//*[@id="tab-urgentcotactor"]/div/div/div/div[1]/div[2]/div').text
        relation = driver.find_element_by_xpath('//*[@id="tab-urgentcotactor"]/div/div/div/div[2]/div[2]/div').text
        tel = driver.find_element_by_xpath('//*[@id="tab-urgentcotactor"]/div/div/div/div[3]/div[2]/div').text
        sql = "insert into xqh_contact values(\
                  (select replace(UUID(),'-','')),'"+customNo+"','"+uname+"','"+relation+"','"+tel+"')"

        print(sql)
        self.con_mysql(sql)

        uname2 = driver.find_element_by_xpath('//*[@id="tab-urgentcotactor"]/div/div/div/div[10]/div[2]/div').text
        relation2 = driver.find_element_by_xpath('//*[@id="tab-urgentcotactor"]/div/div/div/div[11]/div[2]/div').text
        tel2 = driver.find_element_by_xpath('//*[@id="tab-urgentcotactor"]/div/div/div/div[12]/div[2]/div').text
        sql2 = "insert into xqh_contact values(\
                          (select replace(UUID(),'-','')),'" + customNo + "','" + uname2 + "','" + relation2 + "','" + tel2 + "')"
        print(sql2)
        self.con_mysql(sql2)

    def peroson_info(self,customNo):
        driver.find_element_by_xpath('//*[@id="borrow-edit"]/ul/li[3]/a').click()

        uname = driver.find_element_by_xpath('//*[@id="lblName"]/div').text     #姓名
        iCard = driver.find_element_by_xpath('//*[@id="lblIdcard"]/div').text   #身份证号码
        iCradimgz = driver.find_element_by_xpath('//*[@id="tab-personalinfo"]/div/div/div/div[3]/div[2]/img').get_attribute("src")  #身份证正面照片
        iCradimgf = driver.find_element_by_xpath('//*[@id="tab-personalinfo"]/div/div/div/div[4]/div[2]/img').get_attribute("src")  #身份证反面照片
        personImg = driver.find_element_by_xpath('//*[@id="tab-personalinfo"]/div/div/div/div[5]/div[2]/img').get_attribute("src")  #个人照片
        edu = driver.find_element_by_xpath('//*[@id="tab-personalinfo"]/div/div/div/div[6]/div[2]/div').text    #教育程度
        city = driver.find_element_by_xpath('//*[@id="tab-personalinfo"]/div/div/div/div[7]/div[2]/div').text   #居住城市
        job_city = driver.find_element_by_xpath('//*[@id="tab-personalinfo"]/div/div/div/div[8]/div[2]/div').text   #工作城市
        company = driver.find_element_by_xpath('//*[@id="tab-personalinfo"]/div/div/div/div[9]/div[2]/div').text    #公司地址
        mobile = driver.find_element_by_xpath('//*[@id="tab-personalinfo"]/div/div/div/div[10]/div[2]/div').text #固定电话
        marriage = driver.find_element_by_xpath('//*[@id="tab-personalinfo"]/div/div/div/div[13]/div[2]/div').text  #婚姻状况
        wechart = driver.find_element_by_xpath('//*[@id="tab-personalinfo"]/div/div/div/div[14]/div[2]/div').text   #微信号
        sql = "insert into xqh_custom VALUES ('"+customNo+"','"+uname+"','"+iCard+"','"+iCradimgz+"','"+iCradimgf+"','"+personImg+"','"+edu+"'," \
                                "'"+city+"','"+job_city+"','"+company+"','"+mobile+"','"+marriage+"','"+wechart+"')"
        print(sql)
        self.con_mysql(sql)

    def brrow_history(self,uname):
        driver.find_element_by_xpath('//*[@id="borrow-edit"]/ul/li[2]/a').click()
        trs = driver.find_elements_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr')
        for i in range(1,len(trs)):
            orderNo = driver.find_element_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr[%s]/td[1]' % str(i+1)).text
            applyDate = driver.find_element_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr[%s]/td[2]' % str(i+1)).text
            customNo = driver.find_element_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr[%s]/td[3]' % str(i+1)).text
            brrow_money = driver.find_element_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr[%s]/td[4]' % str(i+1)).text
            borrow_type = driver.find_element_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr[%s]/td[5]' % str(i+1)).text
            borrow_day = driver.find_element_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr[%s]/td[6]' % str(i+1)).text
            service_cost =driver.find_element_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr[%s]/td[8]'% str(i+1)).text
            procedures_cost =driver.find_element_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr[%s]/td[9]'% str(i+1)).text
            overdure_money =driver.find_element_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr[%s]/td[10]'% str(i+1)).text
            over_day = driver.find_element_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr[%s]/td[11]'% str(i+1)).text
            apply_status =driver.find_element_by_xpath('//*[@id="borrows-grid"]/table/tbody/tr[%s]/td[13]/span'% str(i+1)).text

            sql = "insert into xqh_order (id,customNo,brrow_money,type,brrow_day,service_cost,procedures_cost,over_money,over_day,apply_status,uname,apply_date)" \
                  "values ('" + orderNo + "','" + customNo + "','" + brrow_money + "','" + borrow_type + "','" + borrow_day + "','" + service_cost + "'," \
                     "'" + procedures_cost + "','" + overdure_money + "','" + over_day + "','" + apply_status + "','"+uname+"','"+applyDate+"')"
            print(sql)
            self.con_mysql(sql)
    def auto_pn(self,pn):
        for i in range(1,pn+1):
            try:                              #//*[@id="borrow-grid"]/div/a[3]/span
                driver.find_element_by_xpath('//*[@id="borrow-grid"]/div/a[3]/span').click()
                print("---------------------正在爬去%s页--------" % str(pn))
                time.sleep(3)
            except:
                print('------任务完成-----')

if __name__ == "__main__":
    x= xqh()
    x.login()

