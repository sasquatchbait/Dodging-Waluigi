import pygame
from object import Object
class Waluigi(Object):
    def __init__(self, pos):
        super().__init__("Wah.png", pos)
        self.image = pygame.transform.scale(self.image (90, 70))
        self.accel = pygame.math.Vector2()

     def update(self):
         super().update()


