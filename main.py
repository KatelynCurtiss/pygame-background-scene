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
    pygame.draw.circle(screen, config.LIGHT_BLUE,(x + 9, y - 100),6, 0)
    pygame.draw.circle(screen, config.LIGHT_BLUE,(x + 300, y - 100),6, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 350, y - 150),4, 0)
    pygame.draw.circle(screen, config.LIGHT_BLUE,(x + 400, y - 12),16, 0)
    pygame.draw.circle(screen, config.LIGHT_BLUE,(x + 367, y - 150),4, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 90, y - 90),13, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 100, y - 100),3, 0)
    pygame.draw.circle(screen, config.LIGHT_BLUE,(x + 345, y - 110),6, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 78, y - 159),9, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 423, y - 35),10, 0)
    pygame.draw.circle(screen, config.LIGHT_BLUE,(x + 265, y - 89),5, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 109, y - 450),3, 0)
    pygame.draw.circle(screen, config.LIGHT_BLUE,(x + 125, y - 125),6, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 500, y - 159),9, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 23, y - 58),10, 0)
    pygame.draw.circle(screen, config.YELLOW,(x + 260, y - 28),5, 0)



def draw_grass(x, y):
    pygame.draw.rect(screen, config.BROWN, (0, HEIGHT - 100, WIDTH, 100))

def draw_house(x,y):
     pygame.draw.rect(screen, config.LIGHT_PINK, (0, HEIGHT - 20, WIDTH, 20))

def draw_cloud(x, y):
    pygame.draw.circle(screen, config.LIGHT_BLUE, (x, y), 40)
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