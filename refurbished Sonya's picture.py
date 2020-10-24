import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1000, 720))
surf1 = pygame.display.set_mode((1000, 720), 0, 32)
surf1.set_colorkey((0, 0, 0))

#рисуем фон
polygon(screen, (254, 214, 163), [(0,0), (1000,0), (1000,180), (0,180)])
polygon(screen, (254, 214, 197), [(0,180), (1000,180), (1000,360), (0,360)])
polygon(screen, (254, 214, 149), [(0,360), (1000,360), (1000,510), (0,510)])
#polygon(screen, (192, 143, 143), [(0,510), (1000,510), (1000,720), (0,720)])
#солнце
for i in range(0, 60):
    sun = pygame.Surface((900, 900))
    sun.set_colorkey((255, 175, 45))
    sun.set_alpha(-i / 0.23 + 255)
    pygame.draw.circle(sun, (255, 255, 102), (450, 100), i)
    screen.blit(sun, (50, 50))
#оранжевая гора
polygon(screen, (255, 140, 0), [(0,360), (1000,240), (915,205), (865,220),(800,185), (755, 200),(700,135),(665,135),(630,170), (595,210), (525,230), (500,260),(450,240),(400,310),(365,295),(290,305), (170,210),(155,180), (115,165), (15,285),(0,330)])
circle(screen, (255, 140, 0), (680, 143), 17) #изгиб горы
#кирпичная гора
polygon(screen,(173, 65, 49), [(0,540),(1000,490),(1000,275),(960,345),(910,340),(885,380),(835,345),(785,410),(685,360),(565,360),(505,425),(410,440),(340,375),(250,360),(220,450),(150,410),(110,490),(10,380),(0,370)])
#изгибы горы
circle(screen, (173, 65, 49), (625, 400), 71)
ellipse(screen, (173, 65, 49), (10,300,130,520))
#оставшаяся часть фона
polygon(screen, (180, 135, 149), [(0,540), (1000,490), (1000,720), (0,720)])
#темная гора
polygon(screen, (44, 7, 33), [(0,720),(1000,720),(1000,470),(970,490),(940,520),(835,600),(765,630),(740,635),(715,630),(645,600),(480,680),(390,665),(360,645),(245,510),(150,440),(0,410)])
#разные чаечки
def bird (a,b,c):
    polygon(surf1,(64, 27, 3),[(a,b),(a-20*c,b-12*c),(a-18*c,b-14*c),(a-12*c,b-13*c),(a-5*c,b-10*c),(a+1*c,b-5),
                                (a+3*c,b-8*c),(a+12*c,b-12*c),(a+22*c,b-13*c)])
    reversed_surf1 = pygame.transform.flip(surf1, False, True)
    polygon(reversed_surf1, (64, 27, 3), [(a, b), (a - 20 * c, b - 12 * c), (a - 18 * c, b - 14 * c), (a - 12 * c, b - 13 * c),
                                  (a - 5 * c, b - 10 * c), (a + 1 * c, b - 5), (a + 3 * c, b - 8 * c),
                                  (a + 12 * c, b - 12 * c), (a + 22 * c, b - 13 * c)])
    screen.blit(reversed_surf1, (0, 0))

rev_screen = pygame.transform.flip(screen, False, True)
screen.blit(rev_screen, (0, 0))

bird (250,240,1)
bird (330,260,1)
bird (430,240,1)
bird (350,300,1)
bird (390,270,1)
bird (790,520,1)
bird (690,550,1)
bird(780,590, 2)
bird(610,500,2)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()