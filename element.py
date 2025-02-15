import pygame
from config import ELEMENT_RADIUS, ELEMENT_SIZE, IMAGE_FILE

class Element:
    def __init__(self, element_type, x, y, vx, vy):
        self.type = element_type
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.update_image()

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def update_image(self):
        try:
            self.image = pygame.image.load(IMAGE_FILE[self.type])
            self.image= pygame.transform.scale(self.image, (ELEMENT_SIZE[self.type][0], ELEMENT_SIZE[self.type][1]))
        except pygame.error:
            print(f"Error updating image after collision {self.type}")

    def draw(self, screen):
        screen.blit(self.image, (int(self.x - ELEMENT_RADIUS), int(self.y - ELEMENT_RADIUS)))

    def collide(self, other):
        if self.type == other.type:
            return

        if (self.type == 'rock' and other.type == 'scissors') or \
           (self.type == 'scissors' and other.type == 'paper') or \
           (self.type == 'paper' and other.type == 'rock'):

            other.type = self.type
            other.update_image()
        else:
            self.type = other.type
            self.update_image()
