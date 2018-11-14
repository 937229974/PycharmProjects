import pytesseract
from PIL import Image,ImageEnhance
'''
你我贷 图片识别
'''
def read_img_ppd(flag):
    img_path="E:/IMG/15.png"

    print(img_path)

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    print('--------------')
    print(line)
    if flag == 1:
        login = line.count("欢迎回来")  # 登录失败
        home = line.count("不向学生借款")  # 登录成功
        jisu = line.count('极速贷')
        backDay = line.count('应还款 日')
        if login > 0:
            return 0
        if home > 0 or jisu > 0 or backDay > 0:
            return 1

    elif flag == 2:
        rec = line.count("待还")  # 还款完成的
        plan = line.count('还款计划')  # 正在还款
        overdue = line.count('逾')  # 逾期
        reg = line.count("欢迎使用")
        rec_1 = line.count("系统目前没有您的借款记")
        if rec_1 > 0:
            return 2
        if rec > 0 and overdue == 0:
            return 2
        if plan > 0 and overdue == 0:
            return 3
        if overdue > 0 and overdue > 0:
            return 4
        if reg > 0:
            return 0
    elif flag == 3:
        rec_h = line.count("极速货 2018")
        if rec_h >0 :
            return 3
        else :
            return 0
def read_img_jf(flag):
    #
    img_path = "C:/Users/Administrator/Desktop/玖富万卡/登录成功/借款逾期.png"

    print(img_path)

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    print('--------------')
    print(line)
    if flag == 1:
        login = line.count("短信验证码登录")  # 登录失败
        login1 = line.count("去注册")  # 登录失败
        home = line.count("积分")  # 登录成功
        home1 = line.count("近真月待还")  # 登录成功
        if login > 0 or login1 > 0:
            return 0
        elif home > 0 or home1 > 0:
            return 1

    else:
        no_bill = line.count("暂时还没有账单")  #
        bill = line.count("已结")  #
        bill_2 = line.count("还款中")  #
        if no_bill > 0 or bill:
            return 2
        elif bill_2 >0 :
            return 3
def read_img_xef(flag):
    #
    img_path = "C:/Users/Administrator/Desktop/信而富(1)/登录成功/20180521184034.png"

    print(img_path)

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    print('--------------')
    print(line)
    if flag == 1:
        login = line.count("置 ........")  # 登录失败
        login1 = line.count("信而窨")  # 登录失败
        home = line.count("认证提额")  # 登录成功
        home1 = line.count("诚信会员")  # 登录成功
        home2 = line.count("补充资料")  # 登录成功
        if login > 0 or login1 > 0:
            return 0
        elif home > 0 or home1 > 0 or home2 > 0:
            return 1

    else:
        no_bill = line.count("您还没有苄目关记录硪")  #
        bill_3 = line.count("还款成功")  #
        bill_4 = line.count("还款失败")  #
        if no_bill > 0 :
            return 2
        elif bill_4 > 0:
            return 4
        elif bill_3 >0:

            return 3

def read_img_yqb(flag):
    #
    img_path = "C:/Users/Administrator/Documents/Tencent Files/937229974/FileRecv/用钱宝/登录成功/有借款记录.png"

    print(img_path)

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    print('--------------')
    print(line)
    if flag == 1:
        login = line.count("已有 帐号去登录")  # 登录失败
        login1 = line.count("忘记密码")  # 登录失败
        home = line.count("获取额虔")  # 登录成功
        home1 = line.count("可借额")  # 登录成功
        bill_4 = line.count("冻结")  # 登录成功
        home3 = line.count("获取额度尖败")  # 登录成功
        bill_3 = line.count("囤 囤 囤 囤 囤 囤")  #
        bill_44 = line.count("请您珍惜")
        if login > 0 or login1 > 0:
            return 0
        elif bill_4 >0 or bill_44 > 0  :
            return 4
        elif home > 0 or home1 > 0 or home3 > 0:
            return 1
        elif bill_3 >0 :
            return 3
def read_img_jjd(flag):

    img_path = "E:/pics/222/20180613174043.png"

    print(img_path)

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    print('--------------')
    print(line)
    if flag == 1:
        login = line.count("今借到借款攻胳")  # 登录失败
        login1 = line.count("已阅读并同意 《今借到用户协议》")  # 登录失败
        login2 = line.count("登录脏册")  # 登录失败
        login3 = line.count("手机号或密码错误")  #

        loan = line.count("求借款") # 登录成功 求借款
        iou = line.count("补借条")  #登录成功  补借条
        #home = line.count("这皇您便用今借到的第")  # 登录成功

        if login > 0 or login1 > 0 or login2 > 0 or login3 >0:
            return 0
        elif loan > 0 or iou > 0:
            return 1

    else:
        no_bill = line.count("待还总额 7夹待还 30夹待还")  # 登录成功
        no_bill_detail = line.count("0 0 0")  # 登录成功
        no_bill_2 = line.count("暂时还没有借入待还")
        shengyu = line.count("剩余")  # 登录成功
        shengyu_1 = line.count("剩佘")  # 登录成功
        overdure = line.count("逾期")
        overdure_1 = line.count("元")

        if no_bill > 0 and no_bill_detail > 0 :
            return 2
        elif no_bill_2 >0 :
            return 2
        elif shengyu > 0 or overdure_1 > 0 or shengyu_1 >0:
            return 3
        elif overdure > 0:
            return 4
if __name__ =="__main__":
    # s= read_img_jjd(2)
    # s= read_img_xef(2)
    s = read_img_ppd(3)

    if s == None:
        s = 5
    print(s)