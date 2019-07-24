import pygame


class Smash(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__("Smash.png")


    def update(self):
        super().update(self)
