import math
from config import ELEMENT_RADIUS

def check_collision(elem1, elem2):
    if(elem1.type==elem2.type):
        return False

    distance = math.sqrt((elem1.x - elem2.x)**2 + (elem1.y - elem2.y)**2)
    return distance <= 2 * ELEMENT_RADIUS

def resolve_collision(elem1, elem2):
    # Swap velocities for a simple elastic collision
    elem1.vx, elem2.vx = elem2.vx, elem1.vx
    elem1.vy, elem2.vy = elem2.vy, elem1.vy

    # Apply rock-paper-scissors rules
    elem1.collide(elem2)