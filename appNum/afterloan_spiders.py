#coding=utf-8

from selenium import webdriver
import threading
from selenium.webdriver.common.keys import Keys
import  time,os,pymysql,uuid
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re

def afterloan_spiders(userName,password):
    # try:
    print("加载jdbc。。。。")
    try:
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'db': 'test',  # 数据库名
            'user': 'root',
            'passwd': 'admin',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor
        }
        conn = pymysql.connect(**config)
        conn.autocommit(1)
        cursor = conn.cursor()
    except:
        print("数据库连接发生异常-------------------------------")
    print("数据库连接成功！")
    driver=webdriver.Firefox()
    # driver=webdriver.PhantomJS(executable_path="D:\\Python34\\Scripts\\phantomjs\\bin\\phantomjs.exe")
    global url
    url="http://afterloan.91naxia.com/afterloan/auth/login"
    driver.get(url)

    # ##账号
    driver.find_element_by_id("login_name").send_keys(userName)
    # ##密码
    driver.find_element_by_id("login_password").send_keys(password)
    # ##登录
    print("请手动输入验证码，将在10秒之后自动登录。")
    time.sleep(10)
    try:
        driver.find_element_by_id("submit1").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="menu"]').click()  # 单击我的工作台
    except:
        print("登录发生异常，请检查账号密码是否正确！")
        return
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="workList"]/li[2]/a/span').click()#单击我的案件
    time.sleep(5)

    #跳转
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="main"]'))
    #获取数据
    time.sleep(2)
    last_page = driver.find_element_by_css_selector('#pagination1 > li.last').get_attribute("jp-data")

    time.sleep(1)
    driver.find_element_by_id("jumpNum").send_keys(1856)
    time.sleep(1)
    driver.find_element_by_link_text("跳转").click()  # 单击跳转，翻页链接

    print("共有%s页。。。。。。" % last_page)
    for page in range(int(last_page)):
        page+=1
        print("当前位于第%d页。。。。。。"%page)
        if page>=1856:
            if page < 2:
                driver.find_element_by_xpath('//*[@id="pagination1"]/li[1]/a').click()  # 单击首页
            elif page < int(last_page):
                try:
                    driver.find_element_by_link_text("下一页").click()  # 单击下一页
                except:
                    driver.find_element_by_xpath('//*[@id="pagination1"]/li[13]/a').click()
                    # print("单击下一页发生异常-----------------------")
                    # print("当前页位于：%d页发生了异常，即将退出浏览器。重新登录，从当前页继续任务.异常1----------------" % page)
                    # driver.quit()
                    # time.sleep(3)
                    # repeat_firefox(driver, conn, cursor, userName, password, page)
                    # continue
                time.sleep(3)
            try:
                skip_page(driver, conn, cursor, userName, password, page)
            except:
                print("当前页位于：%d页发生了异常，即将退出浏览器。重新登录，从当前页继续任务.异常2----------------"%page)
                driver.quit()
                time.sleep(3)
                repeat_firefox(driver, conn, cursor, userName, password, page)


    # except:
    #     print("还没开始程序就出错了，赶紧检查代码。。。。。。。。")
    # finally:
    #     print("此账号抓取结束。。。。。。。")
    cursor.close()
    conn.close()
    driver.quit()

#重新打开搜狐浏览器 跳转页码
def repeat_firefox(driver, conn, cursor, userName, password, page):
    time.sleep(1)
    driver = webdriver.Firefox()
    # driver = webdriver.PhantomJS(executable_path="D:\\Python34\\Scripts\\phantomjs\\bin\\phantomjs.exe")
    driver.get(url)
    time.sleep(3)
    # ##账号
    driver.find_element_by_id("login_name").send_keys(userName)
    # ##密码
    driver.find_element_by_id("login_password").send_keys(password)
    # ##登录
    print("请手动输入验证码，将在10秒之后自动登录。")
    time.sleep(10)
    try:
        driver.find_element_by_id("submit1").click()  # 单击登录
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="menu"]').click()  # 单击我的工作台
    except:
        print("登录发生异常，请检查账号密码是否正确！")
        driver.quit()
        time.sleep(3)
        repeat_firefox(driver, conn, cursor, userName, password, page)
        return
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="workList"]/li[2]/a/span').click()  # 单击我的案件
    time.sleep(5)
    # 获取右侧iframe(我的案件)数据
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="main"]'))
    time.sleep(1)
    driver.find_element_by_id("jumpNum").send_keys(page)
    time.sleep(1)
    driver.find_element_by_link_text("跳转").click()  # 单击跳转，翻页链接
    time.sleep(3)
    skip_page(driver, conn, cursor, userName, password, page)

#跳转 页码
def skip_page(driver, conn, cursor, userName, password,page):
    #
    # #获取 列表数据
    present_handle = driver.current_window_handle  # 获得当前窗口的句柄 (第一个)
    length = driver.find_elements_by_css_selector('#common_list > table > tbody > tr')
    print("我的案件列表总数%s" % len(length))
    for i in range((len(length) - 1)):
        i += 2
        # 单击（处理）操作，弹出新窗口
        print("第%d页<<<<<<<<<<<<<<<<<<<<<<<<<<<单击第%d条数据" % (page, i))
        name = driver.find_element_by_xpath('//*[@id="common_list"]/table/tbody/tr[%d]/td[3]' % i).text
        print("第%d页<<<<<<<<<<<<<<<<<<<<<<<<<<<单击姓名为：%s的处理" % (page, name))
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="common_list"]/table/tbody/tr[%d]/td[14]/a[1]' % i).click()
        time.sleep(5)
        windows = driver.window_handles  # 获得所有的窗口句柄
        driver.switch_to.window(windows[-1])  # 获得当前窗口的句柄（第二个）
        time.sleep(1)
        try:
            dispose_info(driver, conn, cursor)  # 获取 处理信息
        except:
            print("获取处理信息：异常————————————————————")
            try:
                time.sleep(1)
                driver.close()  # 关闭当前窗口
                time.sleep(1)
                driver.switch_to.window(present_handle)  # 返回第一个窗口
                continue
            except:
                print("当前页位于：%d页发生了异常，即将退出浏览器。重新登录，从当前页继续任务.异常3----------------"%page)
                # driver.context
                #
                driver.quit()
                time.sleep(3)
                repeat_firefox(driver, conn, cursor, userName, password, page)
                continue
                return

        time.sleep(1)
        driver.close()  # 关闭当前窗口
        driver.switch_to.window(present_handle)  # 返回第一个窗口


#催收任务详情 获取数据
def  dispose_info(driver, conn, cursor):
    print("基本信息****************")
    try:
        name = driver.find_element_by_xpath('//*[@id="widget-main"]/div[3]/div[2]/table/tbody/tr[1]/td[2]').text  # 借款人姓名
    except:
        name=""
    try:
        mobile = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[3]/div[2]/table/tbody/tr[1]/td[4]').text  # 手机号码
    except:
        mobile = ""
    try:
        certificate_type = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[3]/div[2]/table/tbody/tr[2]/td[2]').text  # 证件类型
    except:
        certificate_type = ""
    try:
        certificate_number= driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[3]/div[2]/table/tbody/tr[2]/td[4]').text  # 证件号
    except:
        certificate_number = ""
    try:
        address = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[3]/div[2]/table/tbody/tr[3]/td[2]').text  # 户籍地址
    except:
        address = ""
    try:
        channel = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[3]/div[2]/table/tbody/tr[3]/td[4]').text  # 渠道
    except:
        channel = ""

    print("还款计划****************")

    try:
        money_repay= driver.find_element_by_xpath('//*[@id="widget-main"]/div[1]/div[2]/h5/span[1]').text  # 已还款
        money_repay = re.findall("已还款:(.*)元", money_repay)[0] #
    except:
        money_repay=0
    try:
        money_not = driver.find_element_by_xpath('//*[@id="widget-main"]/div[1]/div[2]/h5/span[2]').text  #待还总额
        money_not = re.findall("待还总额:(.*)元", money_not)[0]  #
    except:
        money_not=0
    try:
        money_delay = driver.find_element_by_xpath('//*[@id="widget-main"]/div[1]/div[2]/h5/span[3]').text  # 逾期待还总额
        money_delay = re.findall("逾期待还总额:(.*)元", money_delay)[0]  #
    except:
        money_delay=0

    print("银行卡信息****************")
    try:
        bank_number = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[6]/div[2]/table/tbody/tr/td[2]').text  # 卡号
    except:
        bank_number=""
    try:
        bank_ondoor = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[6]/div[2]/table/tbody/tr/td[3]').text  # 银行开户
    except:
        bank_ondoor=""
    try:
        ondoor_branch = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[6]/div[2]/table/tbody/tr/td[4]').text  # 开户支行
    except:
        ondoor_branch=""

    tb_customer_id = str(uuid.uuid1())
    tb_customer_id = tb_customer_id.replace('-', '')
    cursor.execute(
        'INSERT INTO tb_customer (id,name,sex,status,icrad,mobile,bankName,bankNo,weixin,qq,address,source,linkman1,address1,mobile1, linkman2, address2, mobile2, linkman3, address3, mobile3, zf, platform,member_account, user_id, bank_mobile, channel, money_repay, money_not, money_delay)values( % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s,% s, % s, % s, % s, % s, % s, % s, % s, % s, % s,% s, % s, % s, % s, % s, % s)',
        (tb_customer_id, name, '', '', certificate_number, mobile, bank_ondoor, bank_number, '', '', address, '', '', '',
        '', '', '', '', '', '', '', '', '', '', '', '', channel, money_repay, money_not, money_delay))
    # 提交sql语句
    conn.commit()

    print("贷款信息****************")

    try:
        order_code = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[4]/div[2]/table/tbody/tr[1]/td[2]').text  # 订单号
    except:
        order_code = ""
    try:
        apply_date = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[4]/div[2]/table/tbody/tr[1]/td[4]').text  # 申请时间
    except:
        apply_date = ""
    try:
        loans_product = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[4]/div[2]/table/tbody/tr[2]/td[2]').text  # 贷款产品
    except:
        loans_product = ""
    try:
        loans_money = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[4]/div[2]/table/tbody/tr[3]/td[2]').text  # 贷款金额
    except:
        loans_money = ""
    try:
        loans_time = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[4]/div[2]/table/tbody/tr[3]/td[4]').text  # 贷款期限
    except:
        loans_time = ""
    try:
        loans_rate = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[4]/div[2]/table/tbody/tr[4]/td[2]').text  # 贷款利率
    except:
        loans_rate = ""
    try:
        credit_date = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[4]/div[2]/table/tbody/tr[4]/td[4]').text  # 放款日期（起息日）
    except:
        credit_date = ""
    try:
        serve_rate = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[4]/div[2]/table/tbody/tr[5]/td[2]').text  # 服务费率
    except:
        serve_rate = ""
    try:
        refund_month = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[4]/div[2]/table/tbody/tr[6]/td[2]').text  # 每月还款
    except:
        refund_month = ""
    try:
        commodity_prices = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[4]/div[2]/table/tbody/tr[7]/td[2]').text  # 商品价格
    except:
        commodity_prices = ""
    try:
        down_payment = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[4]/div[2]/table/tbody/tr[8]/td[2]').text  # 首付金额
    except:
        down_payment = ""
    tb_order_id = str(uuid.uuid1())
    tb_order_id = tb_order_id.replace('-', '')
    cursor.execute(
        'INSERT INTO tb_order (id,cid,order_no,product,divide,order_money,brrow_date,credit_date,loans_rate,serve_rate,refund_month,commodity_prices,down_payment)values(% s,% s,% s,% s,% s,% s,% s,% s,% s,% s,% s,% s,% s)',
        (tb_order_id, tb_customer_id, order_code, loans_product, loans_time, loans_money, apply_date, credit_date,
         loans_rate,serve_rate, refund_month, commodity_prices, down_payment))
    # 提交sql语句
    conn.commit()


    print("工作信息****************")

    try:
        work_unit = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[5]/div[2]/table/tbody/tr[1]/td[2]').text  # 工作单位
    except:
        work_unit = ""
    try:
        unit_nature = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[5]/div[2]/table/tbody/tr[1]/td[4]').text  # 单位性质
    except:
        unit_nature = ""
    try:
        section = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[5]/div[2]/table/tbody/tr[2]/td[2]').text  # 部门
    except:
        section = ""
    try:
        post = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[5]/div[2]/table/tbody/tr[2]/td[4]').text  # 职位
    except:
        post = ""
    try:
        unit_phone = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[5]/div[2]/table/tbody/tr[3]/td[2]').text  # 单位座机
    except:
        unit_phone = ""
    try:
        address = driver.find_element_by_xpath(
            '//*[@id="widget-main"]/div[5]/div[2]/table/tbody/tr[3]/td[4]').text  # 地址
    except:
        address = ""
    tb_workinfo_id = str(uuid.uuid1())
    tb_workinfo_id = tb_workinfo_id.replace('-', '')
    cursor.execute(
        'INSERT INTO tb_workinfo (id,cid,work_unit,unit_nature,section,post,unit_phone,address)values(% s,% s,% s,% s,% s,% s,% s,% s)',
        (tb_workinfo_id, tb_customer_id, work_unit, unit_nature, section, post, unit_phone, address))
    # 提交sql语句
    conn.commit()

    print("社会关系****************")

    for i in range(len(driver.find_elements_by_xpath('//*[@id="widget-main"]/div[7]/div[2]/table/tbody/tr'))):
        i+=1
        try:
            relation = driver.find_element_by_xpath(
                '//*[@id="widget-main"]/div[7]/div[2]/table/tbody/tr[%d]/td[1]'%i).text  # 关系
        except:
            relation = ""

        try:
            name = driver.find_element_by_xpath(
                '//*[@id="widget-main"]/div[7]/div[2]/table/tbody/tr[%d]/td[2]'%i).text  # 姓名
        except:
            name = ""
        try:
            contact = driver.find_element_by_xpath(
                '//*[@id="widget-main"]/div[7]/div[2]/table/tbody/tr[%d]/td[3]'%i).text  # 联系方式
        except:
            contact = ""
        try:
            state = driver.find_element_by_xpath(
                '//*[@id="widget-main"]/div[7]/div[2]/table/tbody/tr[%d]/td[4]'%i).text  # 状态
        except:
            state = ""
        try:
            remark = driver.find_element_by_xpath(
                '//*[@id="widget-main"]/div[7]/div[2]/table/tbody/tr[%d]/td[5]'%i).text  # 备注
        except:
            remark = ""
        print("<<<<<<<<<<关系:%s姓名:%s状态:%s联系方式:%s备注:%s"%(relation,name,state,contact,remark))
        tb_linkman_id = str(uuid.uuid1())
        tb_linkman_id = tb_linkman_id.replace('-', '')
        cursor.execute(
            'INSERT INTO tb_linkman (id,cid,name,mobile,follow_state,remark,relation)values(% s,% s,% s,% s,% s,% s,% s)',
            (tb_linkman_id, tb_customer_id, name, mobile, state, remark, relation))
        # 提交sql语句
        conn.commit()

    print("通话记录****************")

    time.sleep(2)
    try:
        link = driver.find_element_by_xpath('//*[@id="widget-main"]/div[7]/div[1]/span[2]/button[2]')
        driver.execute_script('$(arguments[0]).click()', link)#弹出窗口
        time.sleep(4)

        for n in range(len(driver.find_elements_by_xpath('//*[@id="personage_tbody"]/tr'))):
            n+=1
            try:
                contact = driver.find_element_by_xpath('//*[@id="personage_tbody"]/tr[%d]/td[2]' % n).text  # 联系方式
            except:
                contact = ""
            try:
                contact_count = driver.find_element_by_xpath('//*[@id="personage_tbody"]/tr[%d]/td[3]' % n).text  # 通话次数
            except:
                contact_count = ""
            try:
                name = driver.find_element_by_xpath('//*[@id="personage_tbody"]/tr[%d]/td[4]' % n).text  # 姓名
            except:
                name = ""
            tb_mo_records_call_id = str(uuid.uuid1())
            tb_mo_records_call_id = tb_mo_records_call_id.replace('-', '')
            print("<<<<<<<<<<联系方式:%s姓名:%s通话次数:%s" % (contact,name,contact_count))
            cursor.execute(
                'INSERT INTO tb_mo_records_call (id,cid,name,mobile,contact_count)values(% s,% s,% s,% s,% s)',
                (tb_mo_records_call_id, tb_customer_id, name, mobile, int(contact_count)))
            # 提交sql语句
            conn.commit()
    except:
        print('无通话记录')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="personage_myModa2"]/div/div/div[1]/button').click()
    time.sleep(2)
    windows = driver.window_handles  # 获得所有的窗口句柄
    driver.switch_to.window(windows[-1])  # 获得当前窗口的句柄（第二个）
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div[1]/div/p/a[2]').click()
    time.sleep(5)

    print("材料附件****************")

    affirm_pic = ""
    for l in range(len(driver.find_elements_by_xpath('//*[@id="widget-main"]/div/div[2]/table/tbody/tr[1]/td[2]/img'))):
        l+=1
        if l < len(driver.find_elements_by_xpath('//*[@id="widget-main"]/div/div[2]/table/tbody/tr[1]/td[2]/img')):
            affirm_pic += driver.find_element_by_xpath(
                '//*[@id="widget-main"]/div/div[2]/table/tbody/tr[1]/td[2]/img[%d]' % l).get_attribute(
                'src') + ','  # 确认收货照片
        else:
            affirm_pic += driver.find_element_by_xpath(
                '//*[@id="widget-main"]/div/div[2]/table/tbody/tr[1]/td[2]/img[%d]' % l).get_attribute(
                'src')  # 确认收货照片

    id_positive = driver.find_element_by_xpath(
        '//*[@id="widget-main"]/div/div[2]/table/tbody/tr[3]/td[2]/img[1]').get_attribute('src')  # 身份证正面
    id_back = driver.find_element_by_xpath(
        '//*[@id="widget-main"]/div/div[2]/table/tbody/tr[3]/td[2]/img[2]').get_attribute('src')  # 身份证背面

    print("材料附件<<<<<<<<<<<<<<<<<<<%s" % affirm_pic)
    print("身份证正面<<<<<<<<<<<<<<<<<<<%s" % id_positive)
    print("身份证背面<<<<<<<<<<<<<<<<<<<%s" % id_back)

    tb_customer_picture_id = str(uuid.uuid1())
    tb_customer_picture_id = tb_mo_records_call_id.replace('-', '')
    cursor.execute(
        'INSERT INTO tb_customer_picture (id,cid,id_positive,id_back,face)values(% s,% s,% s,% s,% s)',
        (tb_customer_picture_id, tb_customer_id, id_positive, id_back, affirm_pic))
    # 提交sql语句
    conn.commit()




if __name__ == "__main__":
    threads = []
    data = [{"userName": "13817044255", "password": '20170707'}]
    for value in data:
        afterloan_spiders(value["userName"], value["password"])