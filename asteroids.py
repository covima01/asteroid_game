from circleshape import *

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius, width=3)
    def update(self, dt):
        self.position += self.velocity * dt
