#!/usr/bin/env python
background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'
import pygame

from pygame.locals import  *

#向sys模块借用exit函数来退出程序
from sys import  exit

#初始化pygame，为使用硬件做准备
pygame.init()

#创建一个窗口
screen  = pygame.display.set_mode((640,480),0,32)
#设置窗口标题
pygame.display.set_caption("hello word!")

background  = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
while  True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()

    screen.blit(background, (0, 0))
    # 将背景图画上去

    x, y = pygame.mouse.get_pos()
    # 获得鼠标位置
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    # 计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    # 把光标画上去

    pygame.display.update()