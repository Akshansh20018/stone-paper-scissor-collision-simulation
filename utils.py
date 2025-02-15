import math
from config import ELEMENT_RADIUS

def check_collision(elem1, elem2):
    distance = math.sqrt((elem1.x - elem2.x)**2 + (elem1.y - elem2.y)**2)
    return distance <= 2 * ELEMENT_RADIUS

def resolve_collision(elem1, elem2):
    # Swap velocities for a simple elastic collision
    elem1.vx, elem2.vx = elem2.vx, elem1.vx
    elem1.vy, elem2.vy = elem2.vy, elem1.vy

    # Apply rock-paper-scissors rules
    elem1.collide(elem2)

# # 
#     # Calculate the center points of each element
#     center1 = (elem1.x + ELEMENT_SIZE[elem1.type][0] / 2, elem1.y + ELEMENT_SIZE[elem1.type][1] / 2)
#     center2 = (elem2.x + ELEMENT_SIZE[elem2.type][0] / 2, elem2.y + ELEMENT_SIZE[elem2.type][1] / 2)

#     # Calculate the distance between centers
#     distance = math.sqrt((center1[0] - center2[0])**2 + (center1[1] - center2[1])**2)

#     # Calculate the sum of half-widths and half-heights
#     sum_half_widths = (ELEMENT_SIZE[elem1.type][0] + ELEMENT_SIZE[elem2.type][0]) / 2
#     sum_half_heights = (ELEMENT_SIZE[elem1.type][1] + ELEMENT_SIZE[elem2.type][1]) / 2

#     # Check if the distance is less than the sum of half sizes
#     return distance < math.sqrt(sum_half_widths**2 + sum_half_heights**2)