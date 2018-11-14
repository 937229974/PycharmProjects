from tkinter import *

class my_gui():
    def __init__(self,window_name):
        self.init_window_name = window_name
    def set_window(self):
        self.init_window_name.title("批处理小程序  v1.0  by: yufeng")
        self.init_window_name.geometry('1068x681+10+10')
        #标签
        self.uname_label = Label(self.init_window_name,text="用户名 :",width= 30 ,height = 5)
        self.uname_label.grid(row= 2,column = 4)

        self.uname_text = Text(self.init_window_name,width= 30 ,height = 2)
        self.uname_text.grid(row =2,column=5 ,rowspan=1, columnspan=1)

        self.pass_label =Label(self.init_window_name,text="密码 ：")
        self.pass_label.grid(row = 4 ,column =4)

        self.pass_text = Text(self.init_window_name,width =30 ,height =2)
        self.pass_text.grid(row =4 ,column =5)

        self.serach_button = Button(self.init_window_name,text='查询信息',command=self.login, width= 10 ,height = 1)
        self.serach_button.grid(row =7 ,column =5)

        self.result_text = Text(self.init_window_name,width =100 ,height = 70)
        self.result_text.grid(row=13, column=5, columnspan=10)

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



def gui_start():
    window = Tk()
    project  = my_gui(window)
    project.set_window()
    window.mainloop()
gui_start()