from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.position = position
        self.velocity = velocity
        self.radius = SHOT_RADIUS
        image_size = self.radius * 2 # Or just 1, 1 if you only use rect for position
        self.image = pygame.Surface([image_size, image_size], pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius, width = 10)
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)