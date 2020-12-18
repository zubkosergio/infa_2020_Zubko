import turtle
turtle.shape('turtle')
turtle.left(90)
for i in range(1, 10, 1):
    turtle.circle(10*i, 360)
    turtle.left(180)
    turtle.circle(10*i, 360)
    turtle.left(180)
turtle.mainloop()
