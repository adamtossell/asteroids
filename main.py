# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update each player
        updatable.update(dt)

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