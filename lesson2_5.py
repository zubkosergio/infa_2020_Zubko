import turtle
import math
turtle.shape('turtle')
for n in range(1,11):
    turtle.st()
    turtle.down()
    turtle.forward(10*n)
    turtle.left(90)
    turtle.forward(10*n)
    turtle.left(90)
    turtle.forward(10*n)
    turtle.left(90)
    turtle.forward(10*n)
    turtle.ht()
    turtle.up()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(180)


turtle.mainloop()
