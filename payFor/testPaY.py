# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import subprocess,os,sys,time
globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
from bottle import route, run


class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        # print('click', event)
        # print('【button=%d, x=%d, y=%d, xdata=%f, ydata=%f】' %
        #       (event.button, event.x, event.y, event.xdata, event.ydata))
        print(event.xdata, event.ydata)
        # fig.canvas.mpl_disconnect(self.cid) #停止鼠标响应事件
        x = str(event.xdata)
        y = str(event.ydata)
        x, dx = x.split(".")
        y, dy = y.split(".")
        print('------------')
        print(x, y)
        plt.close()
        cli = 'adb  -s ' + xuliehao + '  shell input tap '+x+' '+y
        print(cli)
        runCmd(cli)
        auto_xy()

def runCmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd(), shell=False, startupinfo=globalStartupInfo)
    p.wait()
    re=p.stdout.read().decode()
    return re
def conn_phone():
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
    uname = '15070489984'
    pid = 'hui1126'
    if xuliehao:
        #保存到本地电脑的图片路径

        imgs = ""
        # 操作手机
        s = runCmd('adb  -s ' + xuliehao + '  shell am start com.ppdai.loan/com.ppdai.loan.business.LoadAcitivty')
        time.sleep(2)
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 182 1202')
        # print(s)
        time.sleep(6)
        # 账户

        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 357 1228')
        time.sleep(2)
        #     #设置
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 629 167')
        time.sleep(1)

        # 文本输入
        s = runCmd('adb  -s ' + xuliehao + '  shell input text %s' % uname)
        time.sleep(1)
        # # 下一步
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 331 554')
        time.sleep(3)
        # # 密码输入

        s = runCmd('adb  -s ' + xuliehao + '  shell input text  %s' % pid)
        time.sleep(2)
        # 登录
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 297 600')

        time.sleep(3)
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 182 1202')
        time.sleep(2)
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 182 1202')
        time.sleep(1)
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 182 1202')
        time.sleep(1)
        # 借款
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 113 1219')
        time.sleep(3)
        # 路径

        jietupath1 = auto_img(xuliehao)

        imgs += jietupath1 + "&"
        # 账户
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 362 1219')
        time.sleep(3)
        # 待还款
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 103 399')

        # 还款明细
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 594 336')
        time.sleep(3)

        imgPlan = auto_img(xuliehao)

        imgs += imgPlan
        # 返回
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 65 90')
        time.sleep(1)
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 65 90')

        # 设置
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 629 167')
        time.sleep(1)
        # 退出
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 269 939')
        time.sleep(2)
        # 确认
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 536 707')
        time.sleep(2)
        s = runCmd('adb  -s ' + xuliehao + '  shell pm clear com.ppdai.loan')

        # start = auto_img()
        # #点击红包

    else:
        print('no device!')

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

def auto_xy():
        time.sleep(5)
        end_path = auto_img()
        image_file = cbook.get_sample_data(end_path)
        image = plt.imread(image_file)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.imshow(image)
        line, = ax.plot([0], [0])  # empty line
        xy = LineBuilder(line)
        plt.show()
if __name__ =="__main__":
    conn_phone()

# #支付二维码：
# def test():
#     imgSuccess = 'adb - s'+ xuliehao +'shell rm '
# @route('/test')#word简历搜索的关键字
# def index():
#     conn_phone()
# run(port=8080, host='localhost')
