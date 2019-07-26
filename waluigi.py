import pygame
from object import Object
import random
class Waluigi(Object):
    def __init__(self, pos):
        super().__init__("WAH.png", pos)
        self.image = pygame.transform.smoothscale(self.image, (90, 70))
        self.accel = pygame.math.Vector2()
        self.speed = pygame.math.Vector2((random.randint(-10, 10), (random.randint(-10, 10))))

    def update(self):

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



