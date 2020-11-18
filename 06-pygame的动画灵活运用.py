import pygame
from math import pi

WIN_WIDTH = 400     #窗口宽度
WIN_HEIGHT = 600    #窗口高度

pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Pygame小游戏-动画原理')
window.fill((255, 255, 255))

image_baoer = pygame.image.load('files/宝儿姐.png')
window.blit(image_baoer, (100, 300))

pygame.display.flip()

# 1、显示静态球
x = 100
y = 100
dx = dy = 0.1
d = 1
r = 30
ix, iy = 100, 300

pygame.draw.circle(window, (255, 0, 0), (x, y), r)
pygame.display.update()

num = 1
while True:
    num += 1
    #2、移动动画
    # if num % 10 == 0:
    #     pygame.draw.circle(window, (255, 255, 255), (x, y), 50)
    #     if x >= WIN_WIDTH - 50 :
    #         dx = -dx
    #     elif y >= WIN_HEIGHT - 50 :
    #         dy = -dy
    #     elif x <= 25 :
    #         dx = -dx
    #     elif y <= 25 :
    #         dy = -dy
    #     x += dx
    #     y += dy
    #     pygame.draw.circle(window, (255, 0, 0), (x, y), 50)
    #     pygame.display.update()
    #2、缩放动画
    # if num % 10 == 0:
    #     pygame.draw.circle(window, (255, 255, 255), (x, y), r)
    #     if r < 0:
    #         d = -d
    #     elif r > 200 :
    #         d = -d
    #     r += d
    #     print(r, d)
    #     pygame.draw.circle(window, (255, 0, 0), (x, y), r)
    #     pygame.display.update()

    #3、旋转动画
    # if num % 10 == 0:
    #     window.fill((255, 255, 255))
    #     d += 5
    #     new_image_baoer = pygame.transform.rotozoom(image_baoer, d, 1)
    #     window.blit(new_image_baoer, (ix, iy))
    #     pygame.display.update()
    #4、移动和缩放
    if num % 1000 == 0:
        pygame.draw.circle(window, (255, 255, 255), (x, y), r)
        window.blit(image_baoer, (ix, iy))      #使图片不会被破坏
        if x >= WIN_WIDTH - r :
            dx = -dx
        elif y >= WIN_HEIGHT - r :
            dy = -dy
        elif x <= r :
            dx = -dx
        elif y <= r :
            dy = -dy
        x += dx
        y += dy
        if r < 0:
            d = -d
        elif r > 50 :
            d = -d
        r += d
        pygame.draw.circle(window, (255, 0, 0), (x, y), r)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

