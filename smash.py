import pygame
from object import Object


class Smash(Object):
    def __init__(self, pos):
        super().__init__("Smash.png", pos)
        self.image.convert()
        self.accel = pygame.math.Vector2(0, 0)



    def update(self):
        self.speed += self.accel
        if self.accel.length_squared() == 0:
            self.speed *= 0.9
        elif (self.accel.length() > 10):
            self.speed.scale_to_length(10)
        screeninfo = pygame.display.Info()
        screenwidth = screeninfo.current_w
        if self.rect.right > screenwidth:
            self.speed.x *= -0.95
        if self.rect.left < 0:
            self.speed.x *= -0.95
        screenheight = screeninfo.current_h
        if self.rect.top < 0:
            self.speed.y *= -0.95
        if self.rect.bottom > screenheight:
            self.speed.y *= -0.95

        super().update()
    def reset(self, pos):
        self.rect.center = pos


