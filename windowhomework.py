import pygame

# Initialize Pygame
pygame.init()

# Set up the game screen
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")

# Define colors
GREY = (58, 58, 58)

# Background color
screen.fill(GREY)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with GREY
    screen.fill(GREY)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()