import pygame
import random
from circleshape import *
from constants import *
from logger import *




class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", center=(self.position), radius= self.radius, 
            width= LINE_WIDTH
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        velocity_asteroid_1 = self.velocity.rotate(random_angle)
        velocity_asteroid_2 = self.velocity.rotate(-random_angle)

        # make the two new smaller asteroids
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = velocity_asteroid_1 * 1.2
        

        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = velocity_asteroid_2 * 1.2
        

        

    