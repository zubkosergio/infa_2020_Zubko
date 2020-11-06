import pygame
from pygame.draw import *
from random import randint
import time
pygame.init()
id = input('print here your username')


FPS = 30
Score = 0
screen = pygame.display.set_mode((800, 800))


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
font_name = pygame.font.match_font('verdana')

def score_list():
    f = open('score2.txt', 'a')
    f.write(id + ' ' + str(Score) + '\n')
    f.close()

def scorebar(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, CYAN)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Circle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a = randint(20, 120)
        self.image = pygame.Surface((a, a))
        self.image.set_colorkey(BLACK)
        self.rad = a//2
        color = COLORS[randint(0, 5)]
        self.circle = pygame.draw.circle(self.image, color, (a//2, a//2), a//2)
        self.rect = self.image.get_rect()
        self.rect.center = (randint(100, 700), randint(100, 700))
        self.speedx = randint(-10, 15)
        self.speedy = randint(-10, 10)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > 800:
            self.speedx = randint(-10, 1)
        if self.rect.left < 0:
            self.speedx = randint(1, 10)
        if self.rect.bottom > 800:
            self.speedy = randint(-10, -1)
        if self.rect.top < 0:
            self.speedy = randint(1, 10)


pygame.display.update()
clock = pygame.time.Clock()
pygame.mixer.init()
all_sprites = pygame.sprite.Group()
circles = pygame.sprite.Group()
rand_circ = Circle()
circles.add(rand_circ)
all_sprites.add(rand_circ)
s = time.time()
finished = False
while not finished:
    clock.tick(FPS)
    if s < time.time() - 60:
        finished = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in circles:
                if (sprite.rect.center[0] - event.pos[0])**2 + (sprite.rect.center[1] - event.pos[1])**2 < sprite.rad**2:
                    sprite.kill()
                    Score += 1

    if s + 1 > time.time():
        rand_circ = Circle()
        circles.add(rand_circ)
        all_sprites.add(rand_circ)
    all_sprites.update()




    pygame.display.update()
    screen.fill(BLACK)
    score_list()
    all_sprites.draw(screen)
    pygame.display.flip()
    scorebar(screen, str(Score) + ' killed, remains 00:' + str(-time.time() + 60 + s), 30, 800 // 2, 10)



pygame.quit()
