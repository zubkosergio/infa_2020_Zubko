import turtle
turtle.shape('turtle')
n = int(input('введите чётное количество ног'))
for i in range(1, n+1, 1):
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(100)
    turtle.right(360/n)

turtle.mainloop()
