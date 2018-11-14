import pytesseract
from PIL import Image,ImageEnhance
'''
你我贷 图片识别
'''
def read_img_ppd(flag):
    img_path="C:/Users/Administrator/Desktop/test/8.png"

    print(img_path)

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    print('--------------')
    print(line)
    if flag == 1:
        login = line.count("欢迎回来")  # 登录失败
        login1 = line.count("欢迎使用")  # 登录失败
        home = line.count("提醒")  # 登录成功
        overdue1  = line.count('已')
        backDay = line.count('立即还款')
        xinyongdu = line.count('可借额度')
        if login > 0 or login1 >0:
            return 0
        if home > 0 or  backDay > 0:
            return 1
        if xinyongdu > 0:
            return  1
        if overdue1 > 0 :
            return  4

    elif flag == 2:
        rec = line.count("待还")  # 还款完成的
        no_rec = line.count("暂无待还列表")  # 还款完成的
        plan = line.count('还声欠计划')  # 正在还款
        reg = line.count("欢迎使用")
        if rec > 0 or plan >0:
            return 3
        if no_rec > 0 :
            return 2
        if reg > 0:
            return 0


if __name__ =="__main__":
    s = read_img_ppd(2)
    if s == None:
        s = 5
    print(s)