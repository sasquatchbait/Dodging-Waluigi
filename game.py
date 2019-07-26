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

font = pygame.font.SysFont(None, 40)
def init():
    enemies.empty()
    for i in range(5):
        enemies.add(Waluigi((random.randint(50, screen_width - 50), random.randint(50, screen_height - 50))))



def main():
    init()
    dead = False
    score = 0
    while True:
        clock.tick(60)
        score += 1/60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    character.accel.x += 0.25
                if event.key == pygame.K_LEFT:
                    character.accel.x -= 0.25
                if event.key == pygame.K_UP:
                    character.accel.y -= 0.25
                if event.key == pygame.K_DOWN:
                    character.accel.y += 0.25
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    character.accel.x -= 0.25
                if event.key == pygame.K_LEFT:
                    character.accel.x += 0.25
                if event.key == pygame.K_UP:
                    character.accel.y += 0.25
                if event.key == pygame.K_DOWN:
                    character.accel.y -= 0.25
        character.update()
        enemies.update()
        player_hit = pygame.sprite.spritecollide(character, enemies, False)
        if player_hit:
            init()
            character.reset((150,150))
            dead = True
        screen.fill((102, 245, 6))
        if not dead:
            character.draw(screen)
        enemies.draw(screen)
        text = font.render("Time Survived: " + str(int(score)) + " seconds", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (200, 45)
        screen.blit(text, text_rect)
        pygame.display.flip()
        if dead:
            dead = False
            pygame.time.delay(1000)
            score = 0


if __name__ == "__main__":
    main()
