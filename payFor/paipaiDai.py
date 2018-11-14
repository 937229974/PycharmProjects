# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import subprocess,os,sys,time

from PIL import Image
from bottle import route, run

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW




def runCmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd(), shell=False, startupinfo=globalStartupInfo)
    p.wait()
    re=p.stdout.read().decode()
    return re
def conn_phone(uname,pid):
    #连接的手机列表
    mobiles=[]
    cmd=['adb','devices']
    mobilelist=runCmd(cmd)
    mobilelist=mobilelist.split('\r\n')[1:]
    # print(mobilelist)
    for x in mobilelist:
        if x:
            mobiles.append(x)
    if mobiles:
        print(mobiles)
    else:
        print(['no devices\t no devices'])
    #取第一个手机的序列号
    global xuliehao
    if mobiles:
        #取第一个手机设备
        device=mobiles[0].split('\t')
        xuliehao=device[0]
        print(device)
    #有手机连接上就截图
    if xuliehao:
        #保存到本地电脑的图片路径

        s = runCmd('adb  -s '+xuliehao+'  shell am start com.ppdai.loan/com.ppdai.loan.business.LoadAcitivty')
        # print(s)
        time.sleep(4)

        #账户
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
        time.sleep(2)
        #登录
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 492 791')
        time.sleep(2)

        s =  ('adb  -s ' + xuliehao + '  shell input tap 165 1861')
        time.sleep(3)
        # 路径
        jietupath = auto_img()
        # 账户
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 538 1836')
        #待还款
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 196 624')

        # 还款明细
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 934 450')
        time.sleep(3)
        imgPlan = auto_img()
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')
        # im = Image.open(jietupath)
        # im.show()
        return  jietupath


def auto_img():
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
    result = runCmd(jtcmd)
    print('it is screenshot success.....')
    # print(result)
    print('it is moving screenshot to pc.....')
    jtcmd = 'adb  -s  ' + xuliehao + ' pull ' + sdcardpath + ' ' + jietupath
    # print(jtcmd)
    result = runCmd(jtcmd)

    # print(result)
    # 删除sd图片
    jtcmd = 'adb -s ' + xuliehao + ' shell rm  ' + sdcardpath
    # print(jtcmd)
    result = runCmd(jtcmd)
    print(result)
    print('it is moved screenshot to pc success.....')
    return jietupath

@route('/PPD/<uname>/<pid>')#word简历搜索的关键字
def index(uname,pid):
     print(uname , "----"+pid)
     conn_phone(uname,pid)
run(port=6666, host='localhost')


