#coding=utf-8
import subprocess, os, sys, time

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


def runCmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd(), shell=False,
                         startupinfo=globalStartupInfo)
    p.wait()
    re = p.stdout.read().decode()
    return re
#咱们这边现在主要是稳定内部，搜集证据，组织好大家，每次计划要有预案才好弄
xuliehao = 'c776849b7cf5'
#45105dfa0305
def controller_phone():
    # auto_xy()
    flag = True
    while flag :
        try:
            s = runCmd('adb  -s ' + xuliehao + '  shell am start com.creativearts.ymt/com.creativearts.ymt.activity.WelcomeActivity')
            s = runCmd('adb  -s ' + xuliehao + '  shell input swipe 400 400 400 1200')
            time.sleep(4)
            print("点击事件")
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 335 281')
            time.sleep(10)
            print("滑动事件")
            s = runCmd('adb  -s ' + xuliehao + '  shell input swipe 400 1200 400 400')
            time.sleep(1)
            s = runCmd('adb  -s ' + xuliehao + '  shell input swipe 400 1200 400 400')
            time.sleep(1)
            time.sleep(1)
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 33 73')
            time.sleep(3)

            #第二条位置 286 551
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 286 551')
            time.sleep(10)
            print("滑动事件")
            s = runCmd('adb  -s ' + xuliehao + '  shell input swipe 400 1200 400 400')
            time.sleep(2)
            s = runCmd('adb  -s ' + xuliehao + '  shell input swipe 400 1200 400 400')
            time.sleep(1)
            s = runCmd('adb  -s ' + xuliehao + '  shell input swipe 400 1200 400 400')
            time.sleep(1)
            s = runCmd('adb  -s ' + xuliehao + '  shell input tap 33 73')
            time.sleep(3)
            # auto_xy()
        except:
             flag = False

             test()



        # time.sleep(1)
        #
        # # 文本输入
        # s = runCmd('adb  -s ' + xuliehao + '  shell input text %s' % uname)
        # time.sleep(1)
        # # # 下一步
        # s = runCmd('adb  -s ' + xuliehao + '  shell input tap 331 554')
        # time.sleep(3)
        # # # 密码输入
        #
        # s = runCmd('adb  -s ' + xuliehao + '  shell input text  %s' % pid)
        # time.sleep(2)
        # # 登录
        # s = runCmd('adb  -s ' + xuliehao + '  shell input tap 297 600')
        #
        # time.sleep(3)
        # s = runCmd('adb  -s ' + xuliehao + '  shell input tap 182 1202')
        # time.sleep(2)
        # s = runCmd('adb  -s ' + xuliehao + '  shell input tap 182 1202')
        # time.sleep(1)
        # s = runCmd('adb  -s ' + xuliehao + '  shell input tap 182 1202')
        # time.sleep(1)
        # # 借款
        # s = runCmd('adb  -s ' + xuliehao + '  shell input tap 113 1219')
        # time.sleep(3)
        # # 路径
        #
        # jietupath1 = auto_img(xuliehao)
        #
        # imgs += jietupath1 + "&"
        # # 账户
        # s = runCmd('adb  -s ' + xuliehao + '  shell input tap 362 1219')
        # time.sleep(3)
        # # 待还款
    #     # s = runCmd('adb  -s ' + xuliehao + '  shell input tap 103 399')
    #
    #     # 还款明细
    #     s = runCmd('adb  -s ' + xuliehao + '  shell input tap 594 336')
    #     time.sleep(3)
    #
    #     imgPlan = auto_img(xuliehao)
    #
    #     imgs += imgPlan
    #     # 返回
    #     s = runCmd('adb  -s ' + xuliehao + '  shell input tap 65 90')
    #     time.sleep(1)
    #     s = runCmd('adb  -s ' + xuliehao + '  shell input tap 65 90')
    #
    #     # 设置
    #     s = runCmd('adb  -s ' + xuliehao + '  shell input tap 629 167')
    #     time.sleep(1)
    #     # 退出
    #     s = runCmd('adb  -s ' + xuliehao + '  shell input tap 269 939')
    #     time.sleep(2)
    #     # 确认
    #     s = runCmd('adb  -s ' + xuliehao + '  shell input tap 536 707')
    #     time.sleep(2)
    #     s = runCmd('adb  -s ' + xuliehao + '  shell pm clear com.ppdai.loan')
    #
    #     upSTATE = "update tb_mobiles set status='0' where id='%s'" % xuliehao
    #     con_mysql(upSTATE)
    #
    #     return imgs
    # except:
    #     upSTATE = "update tb_mobiles set status='0' where id='%s'" % xuliehao
    #     con_mysql(upSTATE)
    #
    #     return imgs


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
def test():
    pass
#com.creativearts.ymt.activity.WelcomeActivity

if __name__ == "__main__":#com.creativearts.ymt.activity.WelcomeActivity

    controller_phone()