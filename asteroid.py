import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # check if the asteroid is too small to split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        # create two new vectors
        new_vector1 = self.velocity.rotate(random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)
        # calculate the new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # create two new asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        # set the new velocities
        new_asteroid1.velocity = new_vector1 * 1.2
        new_asteroid2.velocity = new_vector2