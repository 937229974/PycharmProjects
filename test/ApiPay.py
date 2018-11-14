# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import subprocess,os,sys,time
globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW



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
    if xuliehao:
        #保存到本地电脑的图片路径

        s = runCmd('adb  -s '+xuliehao+'  shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI')
        print(s)
        time.sleep(2)
        #我的
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 965 1841')
        #钱包按钮
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 175 578')  # adb shell input text hello
        #收付款
        s = runCmd('adb  -s ' + xuliehao + '  shell input tap 175 578')  # adb shell input text hello
        time.sleep(1)
        #滑动
        s = runCmd('adb  -s ' + xuliehao + '  shell input swipe 900 1500 900 600')  # adb shell input text hello
        time.sleep(1)
        #转账到银行卡
        # time.sleep(1)
        #测试支付
        banK_pay(xuliehao)
        #二维码
        # test_shou(xuliehao)
        start = auto_img()
        auto_xy()
    else:
        print('no device!')
def test_shou(xuliehao):
    # 收款码设置
    s = runCmd('adb  -s ' + xuliehao + '  shell input tap 290 1217')
    time.sleep(1)
    s = runCmd('adb  -s ' + xuliehao + '  shell input tap 560 1108')
    s = runCmd('adb  -s ' + xuliehao + '  shell input tap 378 1123')

    time.sleep(0.3)
    s = runCmd('adb  -s ' + xuliehao + '  shell input text 100')
    time.sleep(0.3)
    s = runCmd('adb  -s ' + xuliehao + '  shell input tap 539 811')
def banK_pay(xuliehao):
    #点击银行卡
    s = runCmd('adb  -s ' + xuliehao + '  shell input tap 435 1830')
    # # #获取焦点 姓名
    time.sleep(1)
    #姓名
    s = runCmd('adb  -s ' + xuliehao + '  shell am broadcast -a ADB_INPUT_TEXT --es msg "王博"')


    # 卡号
    s = runCmd('adb  -s ' + xuliehao + '  shell input tap 451 479')  # adb shell input text hello
    s = runCmd('adb  -s ' + xuliehao + '  shell input text 6214680120977275')

    # # 银行坐标
    s = runCmd('adb  -s ' + xuliehao + '  shell input tap 456 640')  # adb shell input text hello
     # adb shell input text hello
    # time.sleep(0.3)
    # # 下一步
    # s = runCmd('adb  -s ' + xuliehao + '  shell input tap 503 1024')
    #
    # time.sleep(0.3)
    # s = runCmd('adb  -s ' + xuliehao + '  shell input text 1')
    # s = runCmd('adb  -s ' + xuliehao + '  shell input swipe 500 947 500 500')
    # s = runCmd('adb  -s ' + xuliehao + '  shell input tap 643 1056')
    # time.sleep(0.2)
    # s = runCmd('adb  -s ' + xuliehao + '  shell input keyevent 7')

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
def num_input():
    nums = '0123456'
    print( len(nums))
    for i in range(0,len(nums)):
        key = "key" + nums[i]
        print(key)



if __name__ == "__main__":
    # conn_phone()
    num_input()

