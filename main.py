import pygame
import random
import config

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Background Scene')

def draw_sky():
    screen.fill(config.DARK_PURPLE)

def draw_stars(x, y):
    pygame.draw.circle(screen, config.YELLOW,(x + 15, y - 20),17, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 9, y - 100),6, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 300, y - 100),6, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 350, y - 150),4, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 400, y - 12),16, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 367, y - 150),4, 0)




def draw_grass(x, y):
    pygame.draw.rect(screen, config.BROWN, (0, HEIGHT - 100, WIDTH, 100))


def draw_cloud(x, y):
    pygame.draw.circle(screen, config.WHITE, (x, y), 40)
    pygame.draw.circle(screen, config.WHITE, (x + 40, y - 20), 40)
    pygame.draw.circle(screen, config.WHITE, (x + 80, y), 40)


def draw_cloud2(x, y):
    pygame.draw.circle(screen, config.WHITE, (x, y), 40)
    pygame.draw.circle(screen, config.WHITE, (x + 40, y - 20), 40)
    pygame.draw.circle(screen, config.WHITE, (x + 80, y), 40)


def draw_sun():
    pygame.draw.circle(screen, config.WHITE, (WIDTH - 100, 100), 50)


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
    draw_stars(100,190)
    draw_cloud2(40,40)
    draw_cloud(20,20)
    draw_grass(100,100)
    draw_sun()
   

    draw_text("Katelyn Curtiss", 50, 20, 36, config.LIGHT_PURPLE)
    draw_text("Alba Public Scools", 50, 60, 36, config.LIGHT_PURPLE)
    draw_text("(=^.^=)", 50, 80, 36, config.LIGHT_PURPLE)

  


    pygame.display.flip()

    pygame.time.Clock().tick(60)


pygame.quit()