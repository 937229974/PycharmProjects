# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import subprocess,os,sys,time

import pymysql
from PIL import Image
from bottle import route, run

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW




class PDD(object):
    '''
    设备列表加载
    '''
    def loading_mobiles(self):
        self.con_mysql("DELETE from tb_mobiles")  # 清空数据库表
        cmd = ['adb', 'devices']
        mobilelist = self.runCmd(cmd)
        mobilelist = mobilelist.split('\r\n')[1:]
        for x in mobilelist:
            if x:
                mobiles = x.split('\t')
                sql = "insert into tb_mobiles VALUES ('%s','0')" % (mobiles[0])
                self.con_mysql(sql)


    def runCmd(self,cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd(), shell=False, startupinfo=globalStartupInfo)
        p.wait()
        re=p.stdout.read().decode()
        return re

    #数据库驱动
    def con_mysql(self,sql):
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
    def conn_phone(self,uname,pid):
        global xuliehao

        sql = "SELECT t.id FROM `tb_mobiles`  t where t.`status`='0' LIMIT 1"
        result  = self.con_mysql(sql)
        xuliehao = result[0]
        upSql  = "update tb_mobiles set status='1' where id='%s'" % xuliehao
        self.con_mysql(upSql)
        if xuliehao == "a60a4750":

        # #有手机连接上就截图
        # if xuliehao:
        #     #保存到本地电脑的图片路径
        #
            s = self.runCmd('adb  -s '+xuliehao+'  shell am start com.ppdai.loan/com.ppdai.loan.business.LoadAcitivty')
            # print(s)
            time.sleep(4)

            #账户
            s =  self.runCmd('adb  -s ' + xuliehao + '  shell input tap 538 1836')
            time.sleep(1)
            #     #设置
            s =  self.runCmd('adb  -s ' + xuliehao + '  shell input tap 957 227')
            time.sleep(1)

            # 文本输入
            s =  self.runCmd('adb  -s ' + xuliehao + '  shell input text %s' % uname)
            time.sleep(1)
            # # 下一步
            s =  self.runCmd('adb  -s ' + xuliehao + '  shell input tap 575 749')
            time.sleep(3)
            # # 密码输入
            s =  self.runCmd('adb  -s ' + xuliehao + '  shell input text  %s' % pid)
            time.sleep(2)
            #登录
            s =  self.runCmd('adb  -s ' + xuliehao + '  shell input tap 492 791')
            time.sleep(2)

            s =  ('adb  -s ' + xuliehao + '  shell input tap 165 1861')
            time.sleep(3)
            # 路径
            jietupath = self.auto_img()
            # 账户
            s =  self.runCmd('adb  -s ' + xuliehao + '  shell input tap 538 1836')
            #待还款
            s =  self.runCmd('adb  -s ' + xuliehao + '  shell input tap 196 624')

            # 还款明细
            s =  self.runCmd('adb  -s ' + xuliehao + '  shell input tap 934 450')
            time.sleep(3)
            imgPlan = self.auto_img()
            s =  self.runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')
            s =  self.runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')
            # im = Image.open(jietupath)
            # im.show()
        if  xuliehao =="bb744b3a":
            s = self.runCmd(
                'adb  -s ' + xuliehao + '  shell am start com.ppdai.loan/com.ppdai.loan.business.LoadAcitivty')
            # print(s)
            time.sleep(4)

            # 账户539 1839
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input tap 538 1836')
            time.sleep(1)
            #     #设置
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input tap 957 227')
            time.sleep(1)

            # 文本输入
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input text %s' % uname)
            time.sleep(1)
            # # 下一步
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input tap 575 749')
            time.sleep(3)
            # # 密码输入
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input text  %s' % pid)
            time.sleep(4)
            # 登录
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input tap 492 791')
            time.sleep(4)
            #首页
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input tap 170 1824')
            time.sleep(1)
            # # 路径
            jietupath = self.auto_img()
            # 账户
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input tap 538 1836')
            # 待还款
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input tap 196 624')

            # 还款明细
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input tap 914 493')
            time.sleep(4)
            imgPlan = self.auto_img()
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')
            s = self.runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')


    def auto_img(self):
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
        result =  self.runCmd(jtcmd)
        print('it is screenshot success.....')
        # print(result)
        print('it is moving screenshot to pc.....')
        jtcmd = 'adb  -s  ' + xuliehao + ' pull ' + sdcardpath + ' ' + jietupath
        # print(jtcmd)
        result =  self.runCmd(jtcmd)

        # print(result)
        # 删除sd图片
        jtcmd = 'adb -s ' + xuliehao + ' shell rm  ' + sdcardpath
        # print(jtcmd)
        result =  self.runCmd(jtcmd)
        print(result)
        print('it is moved screenshot to pc success.....')
        return jietupath

s = 1 #第一次默认加载
@route('/PPD/<uname>/<pid>')# 拍拍贷 账号 ，密码
def index(uname,pid):
     global  s

     p = PDD()
     if s == 1:
        p.loading_mobiles()
        s +=1
     p.conn_phone(uname,pid)
run(port=6666, host='0.0.0.0')


