import turtle
import math
turtle.shape('turtle')
R = 100
k = 360
for i in range(k):
     turtle.forward(2*math.pi*R/360)
     turtle.left(360/k)
turtle.mainloop()
