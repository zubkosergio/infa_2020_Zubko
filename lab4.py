import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
surf = pygame.display.set_mode((500, 1000), 0, 32)
screen.set_colorkey((0, 0, 0))

WHITE = (255, 250, 240)
BLACK = (48, 44, 40)
GREEN = (50, 205, 50)
LGREEN = (0, 255, 0)
LIME = (190, 245, 116)
LIGHT_PINK = (234, 198, 175)
PURPLE = (221, 175, 233)
YELLOW = (225, 225, 0)
TAN = (255, 238, 170)
PINK = (234, 175, 175)
BRPURPLE = (229, 128, 255)


rect(surf, (154, 206, 235), (0, 0, 500, 400))
rect(surf, (178, 236, 93), (0, 400, 500, 600))
for i in range(0, 100):
    sun = pygame.Surface((500, 400))
    sun.set_colorkey((255, 175, 45))
    sun.set_alpha(-i/0.39 + 255)
    pygame.draw.circle(sun, (255, 255, 102), (300, 100), i)
    screen.blit(sun, (50, 50))

#UNICORN TAIL
pygame.draw.ellipse(screen, LIGHT_PINK, (190, 626, 30, 17))
pygame.draw.ellipse(screen, PINK, (187, 629, 40, 20))
pygame.draw.ellipse(screen, LIGHT_PINK, (184, 638, 45, 25))
pygame.draw.ellipse(screen, TAN, (180, 655, 50, 23))
pygame.draw.ellipse(screen, PURPLE, (177, 661, 35, 18))
pygame.draw.ellipse(screen, LIME, (180, 670, 53, 20))
pygame.draw.ellipse(screen, PINK, (170, 675, 40, 20))
pygame.draw.ellipse(screen, LIME, (166, 682, 42, 18))
pygame.draw.ellipse(screen, PINK, (184, 685, 40, 16))
pygame.draw.ellipse(screen, PURPLE, (160, 686, 40, 18))
pygame.draw.ellipse(screen, PURPLE, (164, 690, 45, 20))
pygame.draw.ellipse(screen, LIGHT_PINK, (163, 696, 55, 25))
pygame.draw.ellipse(screen, TAN, (170, 700, 50, 20))
pygame.draw.ellipse(screen, LIME, (176, 700, 48, 14))
pygame.draw.ellipse(screen, LIME, (157, 708, 48, 14))
pygame.draw.ellipse(screen, PURPLE, (175, 715, 40, 18))
pygame.draw.ellipse(screen, PINK, (155, 720, 50, 20))
pygame.draw.ellipse(screen, LIME, (179, 726, 48, 18))
pygame.draw.ellipse(screen, LIGHT_PINK, (157, 715, 55, 25))
pygame.draw.ellipse(screen, TAN, (180, 715, 50, 20))
pygame.draw.ellipse(screen, PURPLE, (160, 730, 50, 18))

#UNICORN_BODY
pygame.draw.ellipse(screen, WHITE, (200, 600, 180, 90))
pygame.draw.polygon(screen, WHITE, [[300, 650], [365, 650], [365, 550], [320, 550]])
pygame.draw.polygon(screen, WHITE, [[225, 650], [240, 650], [240, 750], [225, 750]])
pygame.draw.polygon(screen, WHITE, [[350, 650], [362, 650], [362, 740], [350, 740]])
pygame.draw.polygon(screen, WHITE, [[315, 650], [330, 650], [330, 750], [315, 750]])
pygame.draw.polygon(screen, WHITE, [[260, 650], [272, 650], [272, 740], [260, 740]])
pygame.draw.ellipse(screen, WHITE, (337, 535, 67, 28))
pygame.draw.ellipse(screen, WHITE, (317, 520, 60, 50))
pygame.draw.polygon(screen, PINK, [[340, 525], [354, 524], [355, 460]])

#EYE
pygame.draw.ellipse(screen, BRPURPLE, (345, 535, 19, 19))
pygame.draw.ellipse(screen, WHITE, (348, 538, 12, 6))
pygame.draw.ellipse(screen, BLACK, (355, 541, 7, 7))

#HAIR
pygame.draw.ellipse(screen, PINK, (314, 516, 40, 20))
pygame.draw.ellipse(screen, PINK, (300, 525, 44, 18))
pygame.draw.ellipse(screen, LIGHT_PINK, (314, 530, 30, 17))
pygame.draw.ellipse(screen, PINK, (316, 516, 40, 20))
pygame.draw.ellipse(screen, LIGHT_PINK, (284, 533, 45, 25))
pygame.draw.ellipse(screen, TAN, (290, 545, 50, 23))
pygame.draw.ellipse(screen, LIME, (280, 560, 53, 20))
pygame.draw.ellipse(screen, PURPLE, (280, 575, 40, 20))
pygame.draw.ellipse(screen, LIGHT_PINK, (263, 580, 55, 25))
pygame.draw.ellipse(screen, TAN, (270, 585, 50, 20))
pygame.draw.ellipse(screen, LIME, (280, 590, 38, 14))
pygame.draw.ellipse(screen, PURPLE, (270, 593, 40, 18))
pygame.draw.ellipse(screen, PURPLE, (280, 545, 30, 18))
pygame.draw.ellipse(screen, PINK, (270, 560, 40, 20))
pygame.draw.ellipse(screen, LIME, (266, 572, 38, 18))

#TREES
pygame.draw.polygon(surf, WHITE, [[40, 600], [60, 600], [60, 670], [40, 670]])
pygame.draw.polygon(surf, BLACK, [[40, 600], [60, 600], [60, 670], [40, 670]], 1)
pygame.draw.polygon(surf, WHITE, [[120, 600], [135, 600], [135, 690], [120, 690]])
pygame.draw.polygon(surf, BLACK, [[120, 600], [135, 600], [135, 690], [120, 690]], 1)
pygame.draw.polygon(surf, WHITE, [[220, 450], [240, 450], [240, 540], [220, 540]])
pygame.draw.polygon(surf, BLACK, [[220, 450], [240, 450], [240, 540], [220, 540]], 1)

pygame.draw.ellipse(surf, GREEN, (50, 160, 160, 210))
pygame.draw.ellipse(surf, LGREEN, (50, 160, 160, 210), 5)
pygame.draw.ellipse(surf, GREEN, (100, 270, 180, 95))
pygame.draw.ellipse(surf, LGREEN, (100, 270, 180, 95), 5)
pygame.draw.ellipse(surf, GREEN, (30, 250, 120, 180))
pygame.draw.ellipse(surf, LGREEN, (30, 250, 120, 180), 5)
pygame.draw.ellipse(surf, GREEN, (120, 333, 200, 160))
pygame.draw.ellipse(surf, LGREEN, (120, 333, 200, 160), 5)
pygame.draw.ellipse(surf, GREEN, (10, 350, 100, 110))
pygame.draw.ellipse(surf, LGREEN, (10, 350, 100, 110), 5)
pygame.draw.ellipse(surf, GREEN, (30, 390, 200, 190))
pygame.draw.ellipse(surf, LGREEN, (30, 390, 200, 190), 5)
pygame.draw.ellipse(surf, GREEN, (0, 450, 100, 160))
pygame.draw.ellipse(surf, LGREEN, (0, 450, 100, 160), 5)
pygame.draw.ellipse(surf, GREEN, (73, 500, 110, 140))
pygame.draw.ellipse(surf, LGREEN, (73, 500, 110, 140), 5)

rscreen = pygame.transform.flip(screen, 1

pygame.display.update()

RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
pygame.quit()
