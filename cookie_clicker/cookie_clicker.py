import pygame
from pygame.locals import *

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Cookie Image
cookie = pygame.image.load("cookie.png")
cookie = pygame.transform.scale(cookie, (250, 250))
cookie_rect = cookie.get_rect()
cookie_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Score Text
score = 0
cookies_per_second = 0
custom_font = pygame.font.Font("DripOctober.ttf", 32)
custom_text = custom_font.render(f"You have {score} cookies", True, (255, 0, 0), (0, 0, 0))
custom_text_rect = custom_text.get_rect()
custom_text_rect.x = 0
custom_text_rect.y = 10

# Load the Click Sound
click = pygame.mixer.music.load("click (1).wav")
pygame.mixer.music.set_volume(0.2)

# Cookies Per Click Increase
cookies_to_power = 100
power_available = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Blit the Cookie onto the Display Surface
    display_surface.blit(cookie, cookie_rect)

    # Blit the Text onto the Display Surface
    display_surface.blit(custom_text, custom_text_rect)

    # Check if the Cookie is Clicked
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = event.pos
        if cookie_rect.collidepoint(mouse_pos):
            score += 1
            pygame.mixer.music.play()
            
    power_rect = pygame.draw.rect(display_surface, (128, 128, 128), pygame.Rect(WINDOW_WIDTH - 100, 0, 100, 60))
    if score >= cookies_to_power:
        power_available = True
        power_rect = pygame.draw.rect(display_surface, (0, 255, 0), pygame.Rect(WINDOW_WIDTH - 100, 0, 100, 60))
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = event.pos
            if power_rect.collidepoint(mouse_pos):
                score -= cookies_to_power
                cookies_to_power += 100
                cookies_per_second += 1
    
    score += cookies_per_second

    custom_text = custom_font.render(f"You have {score} cookies", True, (255, 0, 0), (0, 0, 0))
    pygame.time.delay(100)
    # Update the Display
    pygame.display.update()