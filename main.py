import pygame
from simulation import Simulation
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS

def reinforcement_choice():
    print("Select the element you would want to reinforce")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    return int(input("Enter your choice: "))

def main():
    choice = reinforcement_choice()
    pygame.init()
    print("Starting the display...")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Rock Paper Scissors Simulation")
    clock = pygame.time.Clock()

    simulation = Simulation()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        simulation.update()

        screen.fill((0, 0, 0))
        simulation.draw(screen)
        simulation.draw_counter(screen)
        pygame.display.flip()

        if simulation.check_termination():
            print("Simulation ended successfully")
            running= False
        clock.tick(FPS)

    pygame.time.wait(10000)
    pygame.quit()

if __name__ == "__main__":
    main()
