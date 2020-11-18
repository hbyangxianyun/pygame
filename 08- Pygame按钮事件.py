import pygame

WIN_WIDTH = 400     #窗口宽度
WIN_HEIGHT = 600    #窗口高度

pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Pygame小游戏-动画原理')
window.fill((255, 255, 255))
pygame.display.flip()

font = pygame.font.Font('files/JianLi.TTF', 30)

#1、确定按钮
bx1, by1, bw, bh = 30, 100, 100, 50
pygame.draw.rect(window, (255, 0, 0), (bx1, by1, bw, bh))
text1 = font.render('确定',True, (255, 255, 255))
tw1, th1 = text1.get_size()
tx1 = bx1 + bw / 2 - tw1 / 2
ty1 = by1 + bh / 2 - th1 /2
window.blit(text1, (tx1, ty1))

#2、取消按钮
bx2, by2 = 30, 200
pygame.draw.rect(window, (0, 255, 0), (bx2, by2, bw, bh))
text2 = font.render('取消',True, (255, 255, 255))
tw2, th2 = text2.get_size()
tx2 = bx2 + bw / 2 - tw2 / 2
ty2 = by2 + bh / 2 - th2 /2
window.blit(text2, (tx2, ty2))

pygame.display.update()

while True:
    #检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            exit()


