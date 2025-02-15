import pygame
from config import ELEMENT_RADIUS

class Element:
    def __init__(self, element_type, x, y, vx, vy):
        self.type = element_type
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        try:
            self.image = pygame.image.load(f"resources\\{self.type}-resized.jpeg")
        except pygame.error:
            print(f"Error loading image for {self.type}")

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, screen):
        screen.blit(self.image, (int(self.x - ELEMENT_RADIUS), int(self.y - ELEMENT_RADIUS)))

    def collide(self, other):
        if self.type == other.type:
            return

        if (self.type == 'rock' and other.type == 'scissors') or \
           (self.type == 'scissors' and other.type == 'paper') or \
           (self.type == 'paper' and other.type == 'rock'):
            # update the other object
            other.type = self.type
            other.image = pygame.image.load(f"resources\\{other.type}-resized.jpeg")
        else:
            self.type = other.type
            self.image = pygame.image.load(f"resources\\{self.type}-resized.jpeg")
