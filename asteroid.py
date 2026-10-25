from circleshape import CircleShape

import pygame

from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position,
                           self.radius, LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += self.velocity * dt

    def split(self, log_function) -> None:
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_function("asteroid_split")

            delta_direction = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid = Asteroid(
                self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(
                self.position.x, self.position.y, new_radius)

            increase_speed_by = 1.2

            new_asteroid.velocity = self.velocity.rotate(
                delta_direction) * increase_speed_by
            new_asteroid2.velocity = self.velocity.rotate(
                -delta_direction) * increase_speed_by
