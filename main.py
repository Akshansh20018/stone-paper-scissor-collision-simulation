import pygame
from simulation import Simulation
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS

def main():
    print("Starting the display...")
    pygame.init()
    infoObject = pygame.display.Info()
    screen_width, screen_height = infoObject.current_w, infoObject.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    # screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    game_width, game_height = WINDOW_WIDTH, WINDOW_HEIGHT  # Your desired game area size
    game_surface = pygame.Surface((game_width, game_height))
    pygame.display.set_caption("Rock Paper Scissors Simulation")
    clock = pygame.time.Clock()

    simulation = Simulation()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

        simulation.update()

        game_surface.fill((0, 0, 0))
        simulation.draw(game_surface)
        simulation.draw_counter(game_surface)

        scale = min(screen_width / game_width, screen_height / game_height)
        scaled_width = int(game_width * scale)
        scaled_height = int(game_height * scale)
        scaled_surface = pygame.transform.smoothscale(game_surface, (scaled_width, scaled_height))

        # Center the scaled surface on the screen
        x = (screen_width - scaled_width) // 2
        y = (screen_height - scaled_height) // 2

        # Clear the screen and blit the scaled game surface
        screen.fill((0, 0, 255))  # Fill with gray or any color for the letterboxing
        screen.blit(scaled_surface, (x, y))

        pygame.display.flip()

        if simulation.check_termination():
            print("Simulation ended successfully")
            running= False
        clock.tick(FPS)

    pygame.time.wait(10000)
    pygame.quit()

if __name__ == "__main__":
    main()
