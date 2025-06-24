# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid_field import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    running = True
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    asteroid_group = pygame.sprite.Group()
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updatable_group, drawable_group)
    player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    field = AsteroidField()
   
    while running:
        keys = pygame.key.get_pressed()
        color = (0, 0, 0)
        screen.fill(color)
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player1.shoot()
        for asteroid in asteroid_group:
            if player1.collide(asteroid):
                print("Game over!")
                sys.exit(1)
        for shot in shots_group:
            for asteroid in asteroid_group:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
        updatable_group.update(dt)



        dt = clock.tick(60) / 1000












if __name__ == "__main__":
    main()