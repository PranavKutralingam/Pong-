import pygame
BLACK=(0,0,0)
class AIPaddle(pygame.sprite.Sprite):
    def __init__(self, color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.rect=self.image.get_rect()

    def updatePaddle(self, ball):
        if ball.rect.top > self.rect.top:
            self.rect.y += 5
            if self.rect.y > 400:
                self.rect.y = 400
        elif ball.rect.bottom < self.rect.bottom:
            self.rect.y -= 5
            if self.rect.y < 0:
                self.rect.y = 0
