import pygame
from object import Object


class Smash(Object):
    def __init__(self, pos):
        super().__init__("Smash.png", pos)
        self.accel = pygame.math.Vector2(0, 0)

    def update(self):
        self.speed += self.accel
        if (self.accel.length_squared() == 0):
            self.speed *= 0.95
        screeninfo = pygame.display.Info()
        screenwidth = screeninfo.current_w
        if self.rect.right > screenwidth:
            self.speed.x *= -1
        if self.rect.left < 0:
            self.speed.x *= -1
        screenheight = screeninfo.current_h
        if self.rect.top < 0:
            self.speed.y *= -1
        if self.rect.bottom > screenheight:
            self.speed.y *= -1

        super().update()

