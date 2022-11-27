# Import the pygame library and initialise the game engine
import pygame

import endscreen
from Paddle import Paddle
from ball import Ball
from AIPaddle import AIPaddle

pygame.init()
font = pygame.font.SysFont(None, 30)
#Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
winner = "Player 1"
mainClock = pygame.time.Clock()
# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def paused():
    loop = 1

    while loop:
        draw_text("Game Paused, press any key to continue", font, WHITE, screen, 150, 40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    loop = 0
        pygame.display.update()
        screen.fill((0, 0, 0))
        mainClock.tick(60)


def game_engine(flag):

    paddleA = Paddle(WHITE, 10, 100)
    paddleA.rect.x = 20
    paddleA.rect.y = 200

    if(flag):
        paddleB = Paddle(WHITE, 10, 100)
    else:
        paddleB = AIPaddle(WHITE, 10, 100)
    paddleB.rect.x = 670
    paddleB.rect.y = 200

    ball = Ball(WHITE, 10, 10)
    ball.rect.x = 345
    ball.rect.y = 195

    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    # Add the car to the list of objects
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)

    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # Initialise player scores
    scoreA = 0
    scoreB = 0


    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carryOn = False  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Pressing the x Key will quit the game
                    carryOn = False
            elif scoreA==15 or scoreB==15:
                carryOn = False


        # Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B)
        keys = pygame.key.get_pressed()
        if(flag):
            if keys[pygame.K_w]:
                paddleA.moveUp(5)
            if keys[pygame.K_s]:
                paddleA.moveDown(5)
            if keys[pygame.K_p]:
                paddleB.moveUp(5)
            if keys[pygame.K_l]:
                paddleB.moveDown(5)
            if keys[pygame.K_BACKSPACE]:
                paused()
        else:
            if keys[pygame.K_w]:
                paddleA.moveUp(5)
            if keys[pygame.K_s]:
                paddleA.moveDown(5)
            if keys[pygame.K_BACKSPACE]:
                paused()
            # --- Game logic should go here
        all_sprites_list.update()

        # Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x >= 690:
            scoreA += 1
            ball.velocity[0] = -ball.velocity[0]
            ball.velocity[1]=0
            ball.scored()
        if ball.rect.x <= 0:
            scoreB += 1
            ball.velocity[0] = -ball.velocity[0]
            ball.velocity[1]=0
            ball.scored()
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

            # Detect collisions between the ball and the paddles
        if pygame.sprite.collide_rect(ball, paddleA) or pygame.sprite.collide_rect(ball, paddleB):
            ball.bounce()
        if(flag!=True):
            paddleB.updatePaddle(ball)

        # --- Drawing code should go here
        # First, clear the screen to black.
        screen.fill(BLACK)
        # Draw the net
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)


        # draw sprites
        all_sprites_list.draw(screen)

        # Display scores:
        font = pygame.font.SysFont("comicsansms", 74)
        text = font.render(str(scoreA), 3, WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(scoreB), 3, WHITE)
        screen.blit(text, (420, 10))


        # update the screen
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

        if(scoreA==10 or scoreB==10):
            winner ="Player 1" if scoreA>scoreB else "Player 2"
            endscreen.winner_screen(winner)





