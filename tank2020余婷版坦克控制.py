import pygame

pygame.init()
screen = pygame.display.set_mode((23*26 + 100, 23*26))
pygame.display.set_caption('坦克大战2020')
pygame.display.flip()

#载入坦克,每个方向两张图片，利用帧的变换模拟出坦克的运动状态。
tank_up = pygame.image.load('files/a.png')  #向上的坦克
tank_down = pygame.image.load('files/ab.png')  #向下的坦克
tank_left = pygame.image.load('files/al.png')  #向左的坦克
tank_right = pygame.image.load('files/ar.png')  #向右的坦克

tank = tank_up
playerpos = [23*8, 23 * 24]   #我方坦克出生坐标
screen.blit(tank, (playerpos[0], playerpos[1]))
pygame.display.update()

x_speed = 2
y_speed = 2
is_move = False

while True:
    #移动控制
    if is_move == True:
        screen.fill((0, 0, 0))
        playerpos[0] += x_speed
        playerpos[1] += y_speed
        screen.blit(tank, (playerpos[0], playerpos[1]))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #检测键盘事件
        if event.type == pygame.KEYDOWN:
            char = chr(event.key)
            #向上
            if event.key == pygame.K_w:
            #if char == 'w':
                is_move = True
                x_speed = 0
                y_speed = -1
                tank = tank_up

            #向左
            if char == 'a':
                is_move = True
                x_speed = -1
                y_speed = 0
                tank = tank_left

            #向下
            if char == 's':
                is_move = True
                x_speed = 0
                y_speed = 1
                tank = tank_down

            #向右
            if char == 'd':
                is_move = True
                x_speed = 1
                y_speed = 0
                tank = tank_right

        if event.type == pygame.KEYUP:
            is_move = False




