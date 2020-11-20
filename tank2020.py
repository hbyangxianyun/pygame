import pygame
import math
#from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((23*26 + 100, 23*26))
pygame.display.set_caption('坦克大战2020')
pygame.display.flip()

White = (255, 255, 255)
Black = (0, 0, 0)

#载入坦克,每个方向两张图片，利用帧的变换模拟出坦克的运动状态。
tank_up = pygame.image.load('files/a.png')  #向上的坦克
tank_up_2 = pygame.image.load('files/b.png')  #向上的坦克
tank_down = pygame.image.load('files/ab.png')  #向下的坦克
tank_down_2 = pygame.image.load('files/bb.png')  #向下的坦克
tank_left = pygame.image.load('files/al.png')  #向左的坦克
tank_left_2 = pygame.image.load('files/bl.png')  #向左的坦克
tank_right = pygame.image.load('files/ar.png')  #向右的坦克
tank_right_2 = pygame.image.load('files/br.png')  #向右的坦克

#我方坦克形象列表
playerlist = [tank_up, tank_up_2, tank_left, tank_left_2, tank_down, tank_down_2, tank_right, tank_right_2]
playerpos = [23*8, 23 * 24]   #我方坦克出生坐标
screen.fill(White)
screen.blit(playerlist[0], playerpos)
pygame.display.update()

x_speed = 2
y_speed = 2
is_move = False
mf = 0
Direction = 0   #0向前2向左4向后6向右
num = 0

def refresh():
    screen.fill((255, 255, 255))
    screen.blit(playerlist[Direction + mf % 2], playerpos)
    pygame.display.update()

def playermove():
    global mf
    mf += 1

while True:
    playerpos_T = playerpos[0] % 23 == 0 and playerpos[1] % 23 == 0
    playerpos_F = playerpos[0] % 23 != 0 or playerpos[1] % 23 != 0

    #移动控制
    playermove()
    refresh()
    print(playerpos)

    if is_move == True or playerpos_F:
        screen.fill((255, 255, 255))
        playerpos[0] += x_speed
        playerpos[1] += y_speed
        refresh()
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #检测键盘事件
        if event.type == pygame.KEYDOWN:
            char = chr(event.key)
            #向上
            if event.key == pygame.K_w and playerpos_T:
            #if char == 'w':
                is_move = True
                x_speed = 0
                y_speed = -1
                Direction = 0

            #向左
            if char == 'a' and playerpos_T:
                is_move = True
                x_speed = -1
                y_speed = 0
                Direction = 2

            #向下
            if char == 's' and playerpos_T:
                is_move = True
                x_speed = 0
                y_speed = 1
                Direction = 4

            #向右
            if char == 'd' and playerpos_T:
                is_move = True
                x_speed = 1
                y_speed = 0
                Direction = 6

        if event.type == pygame.KEYUP:
            is_move = False




