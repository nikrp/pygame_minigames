# Imports
import pygame
from sys import exit

# Initialize Pygame
pygame.init()

# Window
display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tic Tac Toe")
display.fill((255, 255, 255))

# Tic Tac Toe Board
def board():
    left = pygame.draw.line(display, (0, 0, 0), (100, 700), (100, 400), 3)

# Quit Game
def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Main Loop
def main():
    quit_game()
    
    running = True
    while running:
        board()

if __name__ == "__main__":
    main()