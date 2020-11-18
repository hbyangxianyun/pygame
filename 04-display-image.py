import pygame
from math import pi

pygame.init()

window = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Pygame小游戏-显示图形')
window.fill((255, 255, 255))

#=========显示图形========
#1、画直线
#line(画在哪，线的颜色，起点，终点)
pygame.draw.line(window,(255, 0, 0), (10, 20), (390, 20))
#2、画折线
#line(画在哪，线的颜色，是否闭合，点集， 线宽=1)
points = [(20, 300), (120, 160), (180, 260), (300, 100), (300, 300)]
pygame.draw.lines(window, (0, 255, 0), True, points, 3)

#3、画圆
#circle(位置，线的颜色，圆心坐标，圆的半径，线宽=0)
#线宽为0，则是填充圆，设置线宽就是圆环。
pygame.draw.circle(window, (0, 0, 255), (200, 260), 100, 2)

#4、画矩形
#rect(位置，线的颜色，矩形范围，线宽=0)
#线宽为0，则是填充圆，设置线宽就是圆环。
pygame.draw.rect(window, (120, 20, 60), (200, 300, 100, 200),5)

#4、画椭圆
#ellipse(位置，线的颜色，椭圆范围，线宽=0)
#线宽为0，则是填充圆，设置线宽就是圆环。
pygame.draw.ellipse(window, (128, 128, 128), (200, 300, 100, 200), 3)

#4、画弧线
#ellipse(位置，线的颜色，矩形范围，起始弧度， 终止弧度， 线宽=1)
#线宽为0，则是填充圆，设置线宽就是圆环。
pygame.draw.arc(window, (0, 128, 0), (200, 300, 100, 200), 0, pi/0.8, 4)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()