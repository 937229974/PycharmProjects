import pytesseract
from PIL import Image,ImageEnhance



def test_img():
    # i = Image.open("D:/test2/智通图片/img.jpg")  # 打开截图
    # i = i.convert('RGB')
    # frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    # frame4.save('D:/test2/智通图片/new.jpg')
    # qq = Image.open('F:/pics/1.png')
    #
    # imgry = qq.convert('L')  # 图像加强，二值化
    # sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
    # sharp_img = sharpness.enhance(2.0)
    # sharp_img.save("F:/pics/1_R.png")
    new2 = Image.open('E:/pics/20180505164846.png')
    code = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    # try :
    #     s  =code.index("kk")
    # except:
    #     s = -1
    login = code.count("欢迎回来")
    home = code.count("不向学生借款")
    rec  = code.count("待还")
    plan = code.count('还款计划')
    overdue = code.count('逾')
    print(code)
    print('--------------%s'%overdue)
#图片识别
def read_img(url_path,flag):
    list = url_path.split('/')
    img_path="F:/pics/"
    img_path +=list[-1]
    print(img_path)

    new2 = Image.open(img_path)
    line = pytesseract.image_to_string(new2, lang='chi_sim+eng').strip()
    print('--------------')
    print(line)
    if flag == 1:
        login = line.count("欢迎回来") #登录失败
        home = line.count("不向学生借款") #登录成功
        if login > 0 :
            return  0
        if home > 0:
            return 1

    else:
        rec = line.count("待还") #还款完成的
        plan = line.count('还款计划') #正在还款
        overdue = line.count('逾') #逾期
        reg  = line.count("欢迎使用")
        rec_1  = line.count("系统目前没有您的借款记")
        if rec_1 >0:
            return 2
        if rec  > 0 and overdue == 0 :
            return 2
        if plan > 0:
            return 3
        if overdue >0 and overdue > 0 :
            return 4
        if reg > 0:
            return 0

# if   __name__ == "__main__":
#
#     url_path = "http://117.36.75.174:58008/images/screenshot-20180503100744.png"
#     flag = 2
#     code = read_img(url_path, flag)
#     print("code-----%s"%code)
#     if   code == None :
#          code = 5
#     print(code)
test_img()


