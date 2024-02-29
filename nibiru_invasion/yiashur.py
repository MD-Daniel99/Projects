import pygame

class Yiashur():
    
    def __init__(self, nibiru):
        self.screen = nibiru.screen
        self.screen_rect = nibiru.screen.get_rect()

        self.image = pygame.image.load('images/unnamed.bmp')

        self.rect = self.image.get_rect() # get_rect() to get the 'rect' attribute of ship's surface, eventually it will be used for ship's positioning
        self.rect.center = self.screen_rect.center #  значение self.rect.midbottom выравнивается по атрибуту midbottom прямоугольника экрана

    def blitme(self):
        self.screen.blit(self.image, self.rect) #  вывод изображения на экран в позиции, заданной self.rect