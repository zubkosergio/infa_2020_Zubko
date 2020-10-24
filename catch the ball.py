import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((700, 700))
f = open('score1.txt', 'w')
f = open('score1.txt', 'r')


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

global x, y, r

def new_ball():
    global x, y, r
    x = randint(10, 800)
    y = randint(10, 700)
    r = randint(20, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


#def click(event):
    #print(x, y, r)

#def coords(event):
    #for event in pygame.event.get():
        #print(event.pos[0], event.pos[1])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

Score = []
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            def click():
                print(x, y, r)
            def coords():
                for event in pygame.event.get():
                    print(event.pos[0], event.pos[1])
            def great():
                if (((x - event.pos[0])**2) + ((y - event.pos[1])**2) + r**2) < 2 * r ** 2:
                    print('great')
                    Score.append(1)
                    print('счёт:', len(Score))
                else:
                    print('try again later')
            for line in f:
                print('игрок1:', len(Score))

            click()
            coords()
            great()






    new_ball()
    pygame.display.update()
    screen.fill(BLACK)


f.close()
pygame.quit()