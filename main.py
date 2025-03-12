import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =pygame.time.Clock()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # set the containers for each sprite
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    # create the player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update each player
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        # fill the screen with black
        screen.fill((0,0,0))

        # draw each player individually
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        # limit the frame rate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()