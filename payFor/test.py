import threading
import subprocess,os,sys,time
import multiprocessing

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

lock=multiprocessing.Lock()#一个锁
def conn_phone2():
    lock.acquire()

    print("1222")
    uname = '15070489984'
    pid = 'hui1126'
    xuliehao = "bb744b3a"
    if xuliehao == "bb744b3a":
        s = runCmd2(
            'adb  -s ' + xuliehao + '  shell am start com.ppdai.loan/com.ppdai.loan.business.LoadAcitivty')
        # print(s)
        time.sleep(4)

        # 账户539 1839
        s = runCmd2('adb  -s ' + xuliehao + '  shell input tap 538 1836')
        time.sleep(1)
        #     #设置
        s = runCmd2('adb  -s ' + xuliehao + '  shell input tap 957 227')
        time.sleep(1)

        # 文本输入
        s = runCmd2('adb  -s ' + xuliehao + '  shell input text %s' % uname)
        time.sleep(1)
        # # 下一步
        s = runCmd2('adb  -s ' + xuliehao + '  shell input tap 575 749')
        time.sleep(3)
        # # 密码输入
        s = runCmd2('adb  -s ' + xuliehao + '  shell input text  %s' % pid)
        time.sleep(4)
        # 登录
        s = runCmd2('adb  -s ' + xuliehao + '  shell input tap 492 791')
        time.sleep(4)
        # 首页
        s = runCmd2('adb  -s ' + xuliehao + '  shell input tap 170 1824')
        time.sleep(1)
        # # 路径
        jietupath = auto_img(xuliehao)
        # 账户
        s = runCmd2('adb  -s ' + xuliehao + '  shell input tap 538 1836')
        # 待还款
        s = runCmd2('adb  -s ' + xuliehao + '  shell input tap 196 624')

        # 还款明细
        s = runCmd2('adb  -s ' + xuliehao + '  shell input tap 914 493')
        time.sleep(4)
        imgPlan = auto_img(xuliehao)
        s = runCmd2('adb  -s ' + xuliehao + '  shell input tap 93 115')
        s = runCmd2('adb  -s ' + xuliehao + '  shell input tap 93 115')

    lock.release()
def conn_phone1():
    lock.acquire()
    print('1111')
    uname = '13668033445'
    pid = 'ycq15836'
    xuliehao = "a60a4750"
    if xuliehao == "a60a4750":
        # #有手机连接上就截图
        # if xuliehao:
        #     #保存到本地电脑的图片路径
        #
        s = runCmd('adb  -s ' + xuliehao + '  shell am start com.ppdai.loan/com.ppdai.loan.business.LoadAcitivty')
        # print(s)
        time.sleep(4)

        # 账户
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 538 1836')
        time.sleep(1)
        #     #设置
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 957 227')
        time.sleep(1)

        # 文本输入
        s = runCmd('adb  -s ' + xuliehao + '  shell input text %s' % uname)
        time.sleep(1)
        # # 下一步
        s = runCmd('adb   -s ' + xuliehao + '  shell input tap 575 749')
        time.sleep(3)
        # # 密码输入
        s = runCmd('adb  -s ' + xuliehao + '  shell input text  %s' % pid)
        time.sleep(2)
        # 登录
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 492 791')
        time.sleep(2)

        s = ('adb  -s ' + xuliehao + '  shell input tap 165 1861')
        time.sleep(3)
        # 路径
        jietupath = auto_img(xuliehao)
        # 账户
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 538 1836')
        # 待还款
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 196 624')

        # 还款明细
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 934 450')
        time.sleep(3)
        imgPlan = auto_img(xuliehao)
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 93 115')
        # im = Image.open(jietupath)
        # im.show()
    lock.release()
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


def runCmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd(), shell=False,
                         startupinfo=globalStartupInfo)
    p.wait()
    re = p.stdout.read().decode()
    return re

def runCmd2(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd(), shell=False,
                         startupinfo=globalStartupInfo)
    p.wait()
    re = p.stdout.read().decode()
    return re


threads=[]
for x in range(2):
        t=threading.Thread(target=conn_phone1(),args=(5,))
        threads.append(t)

for thr in threads:
    thr.start()
time.sleep(500)
# for thr in threads:
#
#     if thr.isAlive():
#         thr.join()
