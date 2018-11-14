import subprocess, os, sys, time
from tkinter import *

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

class WIN_GUI():
    def __init__(self,window_name):
        self.init_window_name = window_name

    def set_window(self):
        self.init_window_name.title("iFeng  v1.0  by: 宇风-飞扬")
        self.init_window_name.geometry('1068x681+10+10')

        for m in mobiles:
            # butt_name = "butt_%S"%str(m)
            butt_name = Checkbutton(self.init_window_name)


        #标签
        self.uname_label = Label(self.init_window_name,text="你是不是傻逼！ :",width= 30 ,height = 5)
        self.uname_label.grid(row= 6,column = 5)


        self.serach_button = Button(self.init_window_name,text='是',command=self.login, width= 10 ,height = 1)
        self.serach_button.grid(row =7 ,column =5)

        self.serach_button = Button(self.init_window_name, text='否', command=self.login, width=10, height=1)
        self.serach_button.grid(row=7, column=6)


    def login(self):
        uname = self.uname_text.get(1.0, END).strip().replace("\n", "").encode()
        pid = self.pass_text.get(1.0, END).strip().replace("\n", "").encode()
        print('-----------------')
        print(uname,pid)
        if uname == '1' and pid =='2':
            self.result_text.delete(1.0,END)
            self.result_text.insert(1.0,'该用户 查询成功！！！')
        else:
            self.result_text.delete(1.0, END)
            self.result_text.insert(1.0, '该用户 查询失败')

def cmd_execute(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd(), shell=False,
                         startupinfo=globalStartupInfo)
    p.wait()
    re = p.stdout.read().decode()
    return re

def driver():
     global  mobiles
     mobiles = []
     cmd = ['adb', 'devices']
     mobilelist = cmd_execute(cmd)
     mobilelist = mobilelist.split('\r\n')[1:]
     # print(mobilelist)
     for x in mobilelist:
         if x:
             mobiles.append(x)
def gui_start():
    driver()
    window = Tk()
    project  = WIN_GUI(window)
    project.set_window()
    window.mainloop()
gui_start()
