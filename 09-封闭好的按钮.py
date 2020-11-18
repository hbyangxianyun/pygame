import pygame
from yxyButton import Button

WIN_WIDTH = 400     #窗口宽度
WIN_HEIGHT = 600    #窗口高度

pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Pygame小游戏-动画原理')
window.fill((255, 255, 255))
pygame.display.flip()

#确定按钮
sure_button = Button('确定', (100, 100), (100, 50), (255, 0, 0), (255, 255, 255), 30, False)
sure_button.draw(window)

#取消按钮
cancle_button = Button('取消', (100, 200), (100, 50), (0, 255, 0), (255, 255, 255), 30, False)
cancle_button.draw(window)

#第三个按钮
delete_button = Button('删除', (100, 300), (100, 50), (0, 0, 255), (255, 255, 255), 30, False)
delete_button.draw(window)

pygame.display.update()

while True:
    #检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sure_button.is_down(event.pos, window):
                print('确定按钮被点击!')
                sure_button.draw_gray(window)
                pygame.display.update()
                sure_button.id = True
            if cancle_button.is_down(event.pos, window):
                print('取消！')
                cancle_button.id = True
                cancle_button.draw_gray(window)
                pygame.display.update()
            if delete_button.is_up(event.pos, window):
                print('删除!')
                delete_button.id = True
                delete_button.draw_gray(window)
                pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            if sure_button.is_up(event.pos, window) or sure_button.id == True:
                print('确定按钮被释放!')
                sure_button.id = False
            if cancle_button.is_up(event.pos, window) or cancle_button.id == True:
                print('取消按钮被释放!')
                cancle_button.id = False
            if delete_button.is_up(event.pos, window) or delete_button.id == True:
                print('删除按钮被释放')
                delete_button.id = False
