import pygame
import random
from smash import Smash
from waluigi import Waluigi
pygame.init()
screen_info = pygame.display.Info()
screen_size = (screen_width, screen_height) =\
    (int(screen_info.current_w * 1), int(screen_info.current_h * 1))
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
character = Smash((120, 120))
enemies = pygame.sprite.Group()
enemies.empty()
for i in range(10):
    enemies.add(Waluigi((random.randint(50, screen_width - 50), random.randint(50, screen_height - 50))))



def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    character.accel.x += 0.15
                if event.key == pygame.K_LEFT:
                    character.accel.x -= 0.15
                if event.key == pygame.K_UP:
                    character.accel.y -= 0.15
                if event.key == pygame.K_DOWN:
                    character.accel.y += 0.15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    character.accel.x -= 0.15
                if event.key == pygame.K_LEFT:
                    character.accel.x += 0.15
                if event.key == pygame.K_UP:
                    character.accel.y += 0.15
                if event.key == pygame.K_DOWN:
                    character.accel.y -= 0.15
        character.update()
        enemies.update()
        screen.fill((102, 245, 6))
        character.draw(screen)
        enemies.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
