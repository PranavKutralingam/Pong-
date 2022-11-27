import pygame, sys
from pong import game_engine
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('PONG')
size = (700, 500)
screen = pygame.display.set_mode(size)

# setting font settings
font = pygame.font.SysFont(None, 30)

"""
A function that can be used to write text on our screen and buttons
"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# A variable to check for the status later
click = False


# Main container function that holds the buttons and game functions
def main_menu():
    while True:

        screen.fill(BLACK)
        draw_text('Main Menu', font, WHITE, screen, 250, 40)

        mx, my = pygame.mouse.get_pos()

        # creating buttons
        button_1 = pygame.Rect(200, 100, 200, 50)
        button_2 = pygame.Rect(200, 180, 200, 50)
        button_3 = pygame.Rect(200, 260, 200, 50)

        # defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                game_engine(True)
        if button_2.collidepoint((mx, my)):
            if click:
                game_engine(False)
        if button_3.collidepoint((mx,my)):
            if click:
                pygame.display.quit()
                pygame.quit()
                exit()
                break
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)

        # writing text on top of button
        draw_text('2 Players', font, (255, 255, 255), screen, 270, 115)
        draw_text('Vs AI', font, (255, 255, 255), screen, 250, 195)
        draw_text('Quit', font, (255, 255, 255), screen, 230, 275)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

main_menu()
