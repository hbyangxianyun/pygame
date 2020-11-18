import pygame

WIN_WIDTH = 400     #窗口宽度
WIN_HEIGHT = 600    #窗口高度

pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Pygame小游戏-动画原理')
window.fill((255, 255, 255))
pygame.display.flip()



while True:
    #检测事件
    if event.type == pygame.QUIT:
        exit()

