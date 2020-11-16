import pygame
from color import color

pygame.init()
window = pygame.display.set_mode((400, 600))
pygame.display.set_caption('pygame的按钮事件')
window.fill((255, 255, 255))

pygame.display.flip()


font = pygame.font.Font('files/ygy.ttf', 30)
#1、确定按钮
bx1, by1, bw, bh = 30, 100, 100, 50
pygame.draw.rect(window, (255, 0, 0), (bx1, by1, bw, bh))
text1 = font.render('确定', True, (255, 255, 255))
tw1, th1 = text1.get_size()
tx1 = bx1 + bw / 2 - tw1 / 2
ty1 = by1 + bh / 2 - th1 / 2
window.blit(text1, (tx1, ty1))

#2、取消按钮
bx2, by2 = 30, 200
pygame.draw.rect(window, (0, 255, 0), (bx2, by2, bw, bh))
text2 = font.render('取消', True, (255, 255, 255))
tw2, th2 = text2.get_size()
tx2 = bx2 + bw / 2 - tw2 / 2
ty2 = by2 + bh / 2 - th2 / 2
window.blit(text2, (tx2, ty2))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if bx1 <= mx <= bx1 + bw and by1 <= my <= by1 + bw:
                pygame.draw.rect(window, (200, 200, 200), (bx1 + 2, by1 + 2, bw - 4, bh - 4))
                window.blit(text1, (tx1, ty1))
                pygame.display.update()
                print("确定按钮被点击")
            elif bx2 <= mx <= bx2 + bw and by2 <= my <= by2 + bw :
                pygame.draw.rect(window, (200, 200, 200), (bx2 + 2, by2 + 2, bw - 4, bh - 4))
                window.blit(text2, (tx2, ty2))
                pygame.display.update()
                print("取消按钮被点击")
        elif event.type == pygame.MOUSEBUTTONUP:
            mx, my = event.pos
            if bx1 <= mx <= bx1 + bw and by1 <= my <= by1 + bw:
                pygame.draw.rect(window, (255, 0, 0), (bx1, by1, bw, bh))
                window.blit(text1, (tx1, ty1))
                pygame.display.update()
                print("确定按钮被点击")
            elif bx2 <= mx <= bx2 + bw and by2 <= my <= by2 + bw:
                pygame.draw.rect(window, (0, 255, 0), (bx2, by2, bw, bh))
                window.blit(text2, (tx2, ty2))
                pygame.display.update()
                print("取消按钮被点击")

