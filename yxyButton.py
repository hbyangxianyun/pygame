import pygame

class Button:
    def __init__(self, title, pos, size, bg_color = (0, 255, 0), text_color = (255, 255, 255),
                 font_size = 30, id = False):
        self.title = title
        self.pos = pos
        self.size = size
        self.bg_color = bg_color
        self.text_color = text_color
        self.font_size = font_size
        self.old_color = bg_color
        self.id = id

    def draw(self, window):
        pygame.draw.rect(window, self.bg_color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        font = pygame.font.Font('files/JianLi.TTF', self.font_size)
        text = font.render(self.title, True, (255, 255, 255))
        t_w, t_h = text.get_size()
        window.blit(text, (self.pos[0] + self.size[0] / 2 - t_w / 2, self.pos[1] + self.size[1] / 2 - t_h / 2))

    def draw_gray(self, window):
        pygame.draw.rect(window, (200, 200, 200), (self.pos[0] + 2, self.pos[1] + 2, self.size[0] - 4, self.size[1] - 4))
        font = pygame.font.Font('files/JianLi.TTF', self.font_size)
        text = font.render(self.title, True, (255, 255, 255))
        t_w, t_h = text.get_size()
        window.blit(text, (self.pos[0] + self.size[0] / 2 - t_w / 2, self.pos[1] + self.size[1] / 2 - t_h / 2))

    def is_down(self, pos, window):
        m_x, m_y = pos
        btn_x, btn_y = self.pos
        btn_w, btn_h = self.size
        if btn_x <= m_x <= btn_x + btn_w and btn_y <= m_y <= btn_y + btn_h:
            self.bg_color = (200, 200, 200)
            pygame.display.update()
            return True

        return False

    def is_up(self, pos, window):
        m_x, m_y = pos
        btn_x, btn_y = self.pos
        btn_w, btn_h = self.size
        if btn_x <= m_x <= btn_x + btn_w and btn_y <= m_y <= btn_y + btn_h or self.id == True:
            self.bg_color = self.old_color
            self.draw(window)
            pygame.display.update()
            return True

        return False
