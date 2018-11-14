# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import PIL.Image as image
from PIL import Image,ImageEnhance
import time,re, random
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO



# 根据位置对图片进行合并还原
# filename:图片
# location_list:图片位置
#内部两个图片处理函数的介绍
#crop函数带的参数为(起始点的横坐标，起始点的纵坐标，宽度，高度）
#paste函数的参数为(需要修改的图片，粘贴的起始点的横坐标，粘贴的起始点的纵坐标）


#对比RGB值
def is_similar(image1,image2,x,y):
    pass
    #获取指定位置的RGB值
    pixel1=image1.getpixel((x,y))
    pixel2=image2.getpixel((x,y))
    for i in range(0,3):
        # 如果相差超过50则就认为找到了缺口的位置
        if abs(pixel1[i]-pixel2[i])>= 50:
            return False
    return True

#计算缺口的位置
def get_location(image1,image2):
    i=0
    # 两张原始图的大小都是相同的260*155
    # 那就通过两个for循环依次对比每个像素点的RGB值
    # 如果相差超过50则就认为找到了缺口的位置
    for i in range(0,260):
        for j in range(0,116):
            if is_similar(image1,image2,i,j)==False:
                return  i



#滑动验证码破解程序
def main():
    # image_file = Image.open("convert_image.png")  # open colour image
    # image_file = image_file.convert('1')  # convert image to black and white
    # image_file.save('result.png')
    #打开火狐浏览器
    i = Image.open("F:/pics/K_3.png").convert('1') # 打开截图
    rangle = (int(0), int(0), int(57),
              int(157))
    frame1 = i.crop(rangle)
    frame1.save('F:/pics/K_3_a.png')


    i = Image.open("F:/pics/K_3.png").convert('1')  # 打开截图
    rangle = (int(57), int(0), int(311),
              int(157))
    frame2 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame2.save('F:/pics/K_3_b.png')

    # i = Image.open("F:/pics/z9.png").convert('1')  # 打开截图
    # # rangle = (int(57), int(0), int(311),
    # #           int(157))
    # # frame2 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    # i.save('F:/pics/z9_a.png')


    # #计算缺口位置
    # # loc= get_location(frame1, frame2)
    # # print(loc)
    # with  open("F:/pics/K_1.png",'wb') as f:
    #       print(f.write())
#14


#主函数入口
if __name__ == "__main__":
    main()