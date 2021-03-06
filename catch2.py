import pygame
from pygame.draw import *
from random import randint
import time
id = input('print here your username')

FPS = 30
Score = 0

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

def table_top(i):
    return int(i[1])

def sort_table():
    f = open('records.txt', 'r')
    results = []
    while True:
        res = f.readline()
        if res == '':
            break
        results.append(res)

    for i in range(len(results)):
        results[i] = results[i].split()

    f.close()
    fw = open('records.txt', 'w')
    results.sort(key=table_top, reverse=True)
    for i in range(len(results)):
        fw.write(str(results[i][0]) + " " + str(results[i][1]) + "\n")
    fw.close()

class Circle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a = randint(20, 100)
        self.image = pygame.Surface((a, a))
        self.image.set_colorkey(BLACK)
        self.rad = a//2
        color = COLORS[randint(0, 5)]
        self.circle = pygame.draw.circle(self.image, color, (a//2, a//2), a//2)
        self.rect = self.image.get_rect()
        self.rect.center = (randint(100, 1100), randint(100, 700))
        self.speedx = randint(-10, 20)
        self.speedy = randint(-10, 20)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > 1200:
            self.speedx = randint(-15, 1)
        if self.rect.left < 0:
            self.speedx = randint(1, 15)
        if self.rect.bottom > 800:
            self.speedy = randint(-15, -1)
        if self.rect.top < 0:
            self.speedy = randint(1, 15)

class Python(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        b = randint(30, 80)
        image1 = pygame.image.load('unnamed.png').convert_alpha()
        new_image = pygame.transform.scale(image1, (b, b))
        self.width = b
        self.rad = b // 2
        self.image = pygame.Surface((b, b))
        self.image = new_image
        self.rect = self.image.get_rect()
        self.rect.center = (randint(100, 1100), randint(100, 700))
        self.speedx = randint(5, 20)
        self.speedy = randint(-20, 20)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > 1200:
            self.speedx = randint(-15, 1)
        if self.rect.left < 0:
            self.speedx = randint(1, 15)
        if self.rect.bottom > 800:
            self.speedy = randint(-15, -1)
        if self.rect.top < 0:
            self.speedy = randint(1, 15)

pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("My Game")

all_sprites = pygame.sprite.Group()
circles = pygame.sprite.Group()
pythones = pygame.sprite.Group()
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in pythones:
                if (sprite.rect.right[0] > event.pos[0]) and (sprite.rect.bottom[1] > event.pos[1]):
                    sprite.kill()
                    Score += 2

    if s + 1 > time.time():
        rand_circ = Circle()
        circles.add(rand_circ)
        all_sprites.add(rand_circ)
    elif s + 2 > time.time():
        rand_pyth = Python()
        pythones.add(rand_pyth)
        all_sprites.add(rand_pyth)
    all_sprites.update()


    pygame.display.update()
    screen.fill(BLACK)
    score_list()
    sort_table()
    all_sprites.draw(screen)
    pygame.display.flip()
    scorebar(screen, str(Score) + ' killed, remains 00:' + str(-time.time() + 60 + s), 30, 600, 10)



pygame.quit()
