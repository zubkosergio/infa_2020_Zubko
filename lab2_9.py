import turtle
import numpy as np

turtle.shape('turtle')

print('Введите количество многоугольников')
n = int(input())
R = 30


def f(n, R):
    for k in range(1, n + 1):
        turtle.penup()
        turtle.goto(R * (k), 0)
        turtle.pendown()
        turtle.left(180 * (k + 4) / (2 * (k + 2)))

        for i in range(k + 2):
            turtle.forward(2 * R * k * np.sin(3.1415926 / (k + 2)))
            turtle.left(180 - 180 * (k) / (k + 2))

        turtle.right(180 - 180 * (k) / (k + 2))
        turtle.right(180 * (k) / (2 * (k + 2)))


f(n, R)
