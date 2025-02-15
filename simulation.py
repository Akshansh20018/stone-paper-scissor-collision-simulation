import random
from element import Element
from config import WINDOW_WIDTH, WINDOW_HEIGHT, ELEMENT_COUNT, ELEMENT_RADIUS
from utils import check_collision, resolve_collision
import pygame
pygame.init()

class Simulation:
    def __init__(self):
        self.elements = []
        self.initialize_elements()

    def initialize_elements(self):
        types = ['rock', 'paper', 'scissors']
        corners = [(50, 50), (WINDOW_WIDTH - 50, 50), (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)]

        for t, corner in zip(types, corners):
            for _ in range(ELEMENT_COUNT // 3):
                x = random.randint(corner[0] - 40, corner[0] + 40)
                y = random.randint(corner[1] - 40, corner[1] + 40)
                vx = random.uniform(-2, 2)
                vy = random.uniform(-2, 2)
                self.elements.append(Element(t, x, y, vx, vy))

    def update(self):
        for element in self.elements:
            element.update()
            self.check_boundary_collision(element)

        for i in range(len(self.elements)):
            for j in range(i + 1, len(self.elements)):
                if check_collision(self.elements[i], self.elements[j]):
                    resolve_collision(self.elements[i], self.elements[j])

    def check_boundary_collision(self, element):
        if element.x - ELEMENT_RADIUS <= 0 or element.x + ELEMENT_RADIUS >= WINDOW_WIDTH:
            element.vx *= -1
        if element.y - ELEMENT_RADIUS <= 0 or element.y + ELEMENT_RADIUS >= WINDOW_HEIGHT:
            element.vy *= -1

    def draw(self, screen):
        for element in self.elements:
            element.draw(screen)
