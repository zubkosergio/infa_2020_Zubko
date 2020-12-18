import turtle
turtle.shape('turtle')
n = int(input('введите число лепестков'))
for i in range(1, n+1, 1):
    turtle.left(360/n)
    turtle.circle(50, 360)
turtle.mainloop()
