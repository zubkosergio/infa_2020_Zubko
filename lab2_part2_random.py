import turtle
turtle.shape('turtle')
turtle.color('red')
turtle.speed(10)
from random import *
for i in range(1, 1000):
    turtle.forward(randint(0, 60))
    turtle.left(randint(0, 360))
