import pygame

pygame.init()

window = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Pygame小游戏')
window.fill((255, 255, 255))

#=========显示文字========
#1、创建字体对象
#Font(字体文件路径，字号)
font_JianLi = pygame.font.Font('files/JianLi.TTF', 30)
font_YaHei = pygame.font.Font('files/YaHeiCu.ttc', 30)

#2、创建文字对象
#render(文字内容，是否平滑True，文字颜色，背景颜色)
text_chuanpu = font_JianLi.render('川普，你好！', True, (255, 0, 0))
text_chuanpu_yahei = font_YaHei.render('川普，你好！', True, (0, 0, 0), (0, 128, 128))

#3、渲染到窗口上
window.blit(text_chuanpu, (0, 0))
window.blit(text_chuanpu_yahei, (0, 30))

#4、操作文字对象
# 1)获取文字的大小
w, h = text_chuanpu_yahei.get_size()
window.blit(text_chuanpu_yahei, (400 - w, 600- h))
#2)缩放和旋转
new_text_chuanpu = pygame.transform.scale(text_chuanpu_yahei, (200, 50))
window.blit(new_text_chuanpu, (0, 100))

new_text_chanpu_yahei = pygame.transform.rotozoom(text_chuanpu_yahei, 180, 1.8)
window.blit(new_text_chanpu_yahei, (0, 200))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()