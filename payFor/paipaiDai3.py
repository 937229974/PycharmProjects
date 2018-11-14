# -*- coding:utf-8 -*-
import threading

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import subprocess,os,sys,time

import pymysql
from PIL import Image
from bottle import route, run

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

lock = threading.Lock()


# class PDD(object):
    # def __init__(:
        # global L
        # L = threading.Lock()  # 引入锁


def runCmd(cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd(), shell=False, startupinfo=globalStartupInfo)
        p.wait()
        re=p.stdout.read().decode()
        return re

    #数据库驱动
def con_mysql(sql):
            try:
                # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
                conn = pymysql.connect(host='117.34.95.100', user='python', passwd='zhishen1234', db='python1', port=3306, charset='utf8')
                cur = conn.cursor()  # 获取一个游标
                cur.execute(sql)
                data = cur.fetchone()
                cur.close()  # 关闭游标
                conn.close()  # 释放数据库资源
                return  data

            except  Exception:
                print("sql 数据库插入异常 ----",sql)
    #连接手机
def conn_phone1():
        print('1111')
        uname = '13668033445'
        pid = 'ycq15836'
        xuliehao ="a60a4750"
        if xuliehao == "a60a4750":

        # #有手机连接上就截图
        # if xuliehao:
        #     #保存到本地电脑的图片路径
        #
            s = runCmd('adb  -s '+xuliehao+'  shell am start com.ppdai.loan/com.ppdai.loan.business.LoadAcitivty')
            # print(s)
            time.sleep(4)

            #账户
            s =  runCmd('adb  -s ' + xuliehao + '  shell input tap 538 1836')
            time.sleep(1)
            #     #设置
            s =  runCmd('adb  -s ' + xuliehao + '  shell input tap 957 227')
            time.sleep(1)

            # 文本输入
            s =  runCmd('adb  -s ' + xuliehao + '  shell input text %s' % uname)
            time.sleep(1)
            # # 下一步
            s =  runCmd('adb  -s ' + xuliehao + '  shell input tap 575 749')
            time.sleep(3)
            # # 密码输入
            s =  runCmd('adb  -s ' + xuliehao + '  shell input text  %s' % pid)
            time.sleep(2)
            #登录
            s =  runCmd('adb  -s ' + xuliehao + '  shell input tap 492 791')
            time.sleep(2)

            s =  ('adb  -s ' + xuliehao + '  shell input tap 165 1861')
            time.sleep(3)
            # 路径
            jietupath = auto_img(xuliehao)
            # 账户
            s =  runCmd('adb  -s ' + xuliehao + '  shell input tap 538 1836')
            #待还款
            s =  runCmd('adb  -s ' + xuliehao + '  shell input tap 196 624')

            # 还款明细
            s =  runCmd('adb  -s ' + xuliehao + '  shell input tap 934 450')
            time.sleep(3)
            imgPlan = auto_img(xuliehao)
            s =  runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')
            s =  runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')

        #设置
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 957 227')
        #退出
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 258 1279')
        #确认
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 752 1061')
            # im = Image.open(jietupath)
            # im.show()

def conn_phone2():

        print("1222")
        uname = '15070489984'
        pid = 'hui1126'
        xuliehao = "bb744b3a"
        if  xuliehao =="bb744b3a":
            s = runCmd(
                'adb  -s ' + xuliehao + '  shell am start com.ppdai.loan/com.ppdai.loan.business.LoadAcitivty')
            # print(s)
            time.sleep(4)

            # 账户539 1839
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 538 1836')
            time.sleep(1)
            #     #设置
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 957 227')
            time.sleep(1)

            # 文本输入
            s = runCmd('adb  -s ' + xuliehao + '  shell input text %s' % uname)
            time.sleep(1)
            # # 下一步
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 575 749')
            time.sleep(3)
            # # 密码输入
            s = runCmd('adb  -s ' + xuliehao + '  shell input text  %s' % pid)
            time.sleep(4)
            # 登录
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 492 791')
            time.sleep(4)
            #首页
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 170 1824')
            time.sleep(1)
            # # 路径
            jietupath = auto_img(xuliehao)
            # 账户
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 538 1836')
            # 待还款
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 196 624')

            # 还款明细
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 914 493')
            time.sleep(4)
            imgPlan = auto_img(xuliehao)
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')

def auto_img(xuliehao):
        timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        jietupath = 'F://pics'
        sdcardpath = '/sdcard/screenshot-' + timestamp + '.png'
        if not os.path.exists(jietupath):
            os.makedirs(jietupath)
        jietupath += '/screenshot-' + timestamp + '.png'
        # os.remove(jietupath)
        print('it is screenshoting to mobile.....')
        jtcmd = 'adb   -s ' + xuliehao + ' shell /system/bin/screencap -p ' + sdcardpath
        # print(jtcmd)
        result =  runCmd(jtcmd)
        print('it is screenshot success.....')
        # print(result)
        print('it is moving screenshot to pc.....')
        jtcmd = 'adb  -s  ' + xuliehao + ' pull ' + sdcardpath + ' ' + jietupath
        # print(jtcmd)
        result =  runCmd(jtcmd)

        # print(result)
        # 删除sd图片
        jtcmd = 'adb -s ' + xuliehao + ' shell rm  ' + sdcardpath
        # print(jtcmd)
        result =  runCmd(jtcmd)
        print(result)
        print('it is moved screenshot to pc success.....')
        return jietupath

L = threading.Lock()  # 引入锁
if __name__ == "__main__":

   
    # t1 = threading.Thread(target=conn_phone1(), daemon=True)  # 调换10和20，看看效果。
    #
    # t1.start()
    #
    # t2 = threading.Thread(target=conn_phone2(), daemon=False)
    #
    # t2.start()

    threads1 = []

    t1 = threading.Thread(target=conn_phone1())
    t2 = threading.Thread(target=conn_phone2())
    threads1.append(t1)
    threads1.append(t2)
    for n in range(len(threads1)):
        threads1[n].start()
    for i in range(len(threads1)):
        threads1[i].join()






