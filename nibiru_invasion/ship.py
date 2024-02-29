import pygame

class Ship():
    """Ship and its position initialising"""

    def __init__(self, nibiru): # получает два параметра: ссылку self и ссылку на текущий экземпляр класса NibiruInvasion
        self.screen = nibiru.screen # экран присваивается атрибуту Ship, чтобы к нему можно было легко обращаться во всех модулях класса
        self.screen_rect = nibiru.screen.get_rect() # экран присваивается атрибуту Ship, чтобы к нему можно было легко обращаться во всех модулях класса

        self.image = pygame.image.load('images/ship.bmp') 
        self.rect = self.image.get_rect() # get_rect() to get the 'rect' attribute of ship's surface, eventually it will be used for ship's positioning
        self.rect.midbottom = self.screen_rect.midbottom #  значение self.rect.midbottom выравнивается по атрибуту midbottom прямоугольника экрана

    def blitme(self):
        self.screen.blit(self.image, self.rect) #  вывод изображения на экран в позиции, заданной self.rect