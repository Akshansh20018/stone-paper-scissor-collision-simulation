import pygame
from simulation import Simulation
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS

choice_map = {
    1: "rock",
    2: "paper",
    3: "scissors"
}

def reinforcement_choice():
    print("Select the element you would want to reinforce")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("Enter your choice: "))
    return choice_map[choice]

def main():
    choice = reinforcement_choice()
    pygame.init()
    print("Starting the display...")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Rock Paper Scissors Simulation")
    clock = pygame.time.Clock()

    simulation = Simulation()

    running = True
    ability_remaining = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Attempted to use the ability")
                    if ability_remaining>0 and simulation.counts[choice]>0:
                        simulation.send_reinforcements(choice)
                        ability_remaining-= 1
                        print("Ability used successfully.")
                        print(f"{ability_remaining} remaining for this round")
                    elif ability_remaining>0:
                        print("Too late to use this ability, as no elements of this type remain")
                    else:
                        print("Ability already used previously this round")

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
