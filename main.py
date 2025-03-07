import pygame
import random
import config

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Background Scene')

def draw_sky():
    screen.fill(config.LIGHT_BLUE)

def draw_grass():
    pygame.draw.rect(screen, config.GREEN, (0, HEIGHT - 100, WIDTH, 100))

def draw_tree(x, y):
    pygame.draw.rect(screen, config.BROWN, (x, y, 30, 60))
    pygame.draw.circle(screen, config.GREEN, (x + 15, y - 20), 40)

def draw_cloud(x, y):
    pygame.draw.circle(screen, config.WHITE, (x, y), 40)
    pygame.draw.circle(screen, config.WHITE, (x + 40, y - 20), 40)
    pygame.draw.circle(screen, config.WHITE, (x + 80, y), 40)

def draw_sun():
    pygame.draw.circle(screen, config.YELLOW, (WIDTH - 100, 100), 50)

def draw_text(text, x, y, font_size, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_sky()
    draw_grass()
    draw_sun()
    draw_tree(100, HEIGHT - 160)
    draw_tree(600, HEIGHT - 160)

    draw_text("Katelyn Curtiss", 50, 20, 36, config.LIGHT_PURPLE)
    draw_text("Alba Public Scools", 50, 60, 36, config.LIGHT_PURPLE)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()