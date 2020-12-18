import turtle
import math
turtle.shape('turtle')
k = 1
for i in range(1, 10000):
    rho = i/(180/math.pi)
    dx = rho*math.cos(rho)
    dy = rho*math.sin(rho)
    turtle.goto(dx, dy)
