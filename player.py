from circleshape import *
from constants import *
from main import *
from shots import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
    rotation = 0
    shot_timer = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        self.move(dt)
        self.shot_timer -= dt
    def move(self, dt):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if keys[pygame.K_w]:
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            self.position -= forward * PLAYER_SPEED * dt
    def shoot(self):
        if self.shot_timer <= 0:
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
            velocity = pygame.Vector2(0, 1)
            velocity = velocity.rotate(self.rotation)
            velocity = velocity * PLAYER_SHOOT_SPEED
            pewpew = Shot(self.position.copy(), velocity)
        else:
            print ("Still reloading blasters")
