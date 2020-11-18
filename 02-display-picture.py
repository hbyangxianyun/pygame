import pygame

pygame.init()
window = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Pygame的小游戏')
window.fill((255, 255, 255))

#=====游戏启动界面的静态效果图======
#1、加载图片
image_baoer = pygame.image.load('files/宝儿姐.png')
#渲染图片
#blid(渲染对象，坐标:屏幕左上角为坐标原点)
window.blit(image_baoer, (0, 0))

#3、操作图片
#1)获得图片大小
w, h = image_baoer.get_size()
#print(w, h)
window.blit(image_baoer, (400 - w, 600 - h))

#2、旋转和缩放
#scale(缩放对象，目标大小) - 可能会发生形变
new_image_baoer = pygame.transform.scale(image_baoer, (100, 80))
window.blit(new_image_baoer, (210, 0))
#rotozoom(缩放或者旋转对象，旋转角度，缩放比例)

new_image_baoer_rotozoom = pygame.transform.rotozoom(image_baoer, 180, 1)
window.blit(new_image_baoer_rotozoom, (0, 140))

#3、刷新显示页面
#pygame.display.flip()第一次刷新
#pygame.display.update()第二次刷新
pygame.display.flip()

while True:
    #=====游戏帧信息刷新=====
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()




