import pygame

#1、初始化
pygame.init()

#2、创建游戏窗口
#set_mode(窗口的宽和高)
window = pygame.display.set_mode((400, 600))
#设置游戏窗口的标题
pygame.display.set_caption('Pygame小游戏')

#3、让游戏保持一直运行的状态
#game loop(游戏循环)
while True:
    #4、检测事件
    for event in pygame.event.get():
        #检测关闭按钮被点击的事件
        if event.type == pygame.QUIT:
            exit()



