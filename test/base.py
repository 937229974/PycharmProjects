from tkinter import *  # 引入Tkinter工具包

import time

'''
demo1  简单的窗体实例
'''

# def hello():
#     print("hello world")
# win  = Tk()  #定义一个窗体
# win.title("第一个python  GUI")
# win.geometry('400x200')
#
# btn = Button(win,text="点击",command=hello) #按钮属性
# btn.pack(expand=YES ,fill =BOTH)#将按钮填充在整个窗体中间
# mainloop()#进入主循环，程序运行

'''
复杂窗体，程序分开封装
'''

# class  app(object):
#     def __init__(self,master):
#         frame =Frame(master)
#         frame.pack()
#         #创建窗体按钮
#         self.button = Button(frame,text= '退出',fg="red" ,command =frame.quit())
#         self.button.pack(side =LEFT)
#         self.hi_there = Button(frame,text="你好",command = self.say_hello)
#         self.hi_there.pack(side = LEFT)
#     def say_hello(self):
#         print("hello  python  GUI")
# win = Tk()
# ap = app(win)
# win.mainloop()

'''窗体中导航栏设置 '''
# root = Tk()
#
# def hello():
#     print("hello")
# def about():
#     w = Label(root, text="开发者感谢名单\nfuyunbiyi\nfyby尚未出现的女朋友\nhttp://www.programup.com网站")
#     w.pack(side=TOP)
# menu_bar = Menu(root)
#
# #创建下拉菜单file，然后将其加入顶级菜单栏中
# filemenu = Menu(menu_bar,tearoff = 0)
# filemenu.add_command(label="Open",command=hello)
# filemenu.add_command(label="保存",command=hello)
# filemenu.add_separator()
# filemenu.add_command(label="退出",command = root.quit)
# menu_bar.add_cascade(label = 'file',menu = filemenu)
#
# #编辑菜单
# edit_menu = Menu(menu_bar,tearoff = 0)
# edit_menu.add_command(label = "cut",command=hello)
# edit_menu.add_command(label = "copy",command=hello)
# edit_menu.add_command(label = "paste",command=hello)
# edit_menu.add_command(label = "Edit",command=hello)
# menu_bar.add_cascade(label="Edit",menu=edit_menu)
#
# #帮助菜单
#
# help_menu = Menu(menu_bar,tearoff= 0)
# help_menu.add_command(label= "about",command = about)
# menu_bar.add_cascade(label = "help",menu=help_menu)
#
# root.config(menu= menu_bar)
# mainloop()

import hashlib
'''python  gui   工具开发'''
class MY_GUI():
    def __init__(self,window_name):
        self.init_window_name = window_name

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("文本处理工具_v1.2   by: 陈月白")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)


    #功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)
def gui_start():
    init_window = Tk()
    zmj_portal = MY_GUI(init_window)
    zmj_portal.set_init_window()
    init_window.mainloop()
gui_start()









