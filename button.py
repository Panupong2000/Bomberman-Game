import pygame

class Button:
    def __init__(self, center_x, center_y, width, height, inactive_color, active_color, text, title, font_size, action=None):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.centerx = center_x
        self.rect.centery = center_y
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text = text
        self.font = pygame.font.SysFont(None, font_size)
        self.action = action
        self.title = title

    def draw(self, surface, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            color = self.active_color
        else:
            color = self.inactive_color

        pygame.draw.rect(surface, color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

        textsurface = self.font.render(self.title, False, (0, 0, 0))
        font_w = textsurface.get_width()
        font_h = textsurface.get_height()
        surface.blit(textsurface, (surface.get_width() // 2 - font_w // 2, surface.get_height() // 3 - font_h // 2))

    def do_action(self):
        if self.action:
            self.action()

    def change_title(self,title):
        self.title = title
