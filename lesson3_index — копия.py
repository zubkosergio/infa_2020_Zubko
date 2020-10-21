import turtle
turtle.shape('turtle')
turtle.color('blue')
turtle.pensize(3)
turtle.screensize(1000, 600)

num0 = [(0, 0), (0, -80), (40, -80), (40, 0), (0, 0)]
num1 = [(0, 0), (40, 40), (40, -40)]
num2 = [(0, 0), (40, 0), (40, -40), (0, -80), (40, -80)]
num3 = [(0, 0), (40, 0), (0, -40), (40, -40), (0, -80)]
num4 = [(0, 0), (0, -40), (40, -40), (40, 0), (40, -80)]
num5 = [(0, 0), (40, 0), (0, 0), (0, -40), (40, -40), (40, -80), (0, -80)]
num6 = [(0, 0), (-40, -40), (-40, -80), (0, -80), (0, -40), (-40, -40)]
num7 = [(0, 0), (40, 0), (0, -40), (0, -80)]
num8 = [(0, 0), (0, -80), (40, -80), (40, -40), (0, -40), (0, 0), (40, 0), (40, -40)]
num9 = [(0, 0), (0, -40), (40, -40), (40, 0), (0, 0), (40, 0), (40, -40), (0, -80)]


def one(coords, delta_x, delta_y):
    turtle.penup()
    turtle.goto(delta_x, delta_y)
    for i in coords:
        turtle.pendown()
        turtle.goto(i[0]+delta_x, i[1]+delta_y)
        turtle.penup()


def two(coords, delta_x, delta_y):
    turtle.penup()
    turtle.goto(delta_x, delta_y)
    for i in coords:
        turtle.pendown()
        turtle.goto(i[0]+delta_x, i[1]+delta_y)
        turtle.penup()


def three(coords, delta_x, delta_y):
    turtle.penup()
    turtle.goto(delta_x, delta_y)
    for i in coords:
        turtle.pendown()
        turtle.goto(i[0]+delta_x, i[1]+delta_y)
        turtle.penup()


def four(coords, delta_x, delta_y):
    turtle.penup()
    turtle.goto(delta_x, delta_y)
    for i in coords:
        turtle.pendown()
        turtle.goto(i[0]+delta_x, i[1]+delta_y)
        turtle.penup()


def five(coords, delta_x, delta_y):
    turtle.penup()
    turtle.goto(delta_x, delta_y)
    for i in coords:
        turtle.pendown()
        turtle.goto(i[0]+delta_x, i[1]+delta_y)
        turtle.penup()


def six(coords, delta_x, delta_y):
    turtle.penup()
    turtle.goto(delta_x, delta_y)
    for i in coords:
        turtle.pendown()
        turtle.goto(i[0]+delta_x, i[1]+delta_y)
        turtle.penup()


def seven(coords, delta_x, delta_y):
    turtle.penup()
    turtle.goto(delta_x, delta_y)
    for i in coords:
        turtle.pendown()
        turtle.goto(i[0]+delta_x, i[1]+delta_y)
        turtle.penup()


def eight(coords, delta_x, delta_y):
    turtle.penup()
    turtle.goto(delta_x, delta_y)
    for i in coords:
        turtle.pendown()
        turtle.goto(i[0]+delta_x, i[1]+delta_y)
        turtle.penup()


def nine(coords, delta_x, delta_y):
    turtle.penup()
    turtle.goto(delta_x, delta_y)
    for i in coords:
        turtle.pendown()
        turtle.goto(i[0]+delta_x, i[1]+delta_y)
        turtle.penup()


def zero(coords, delta_x, delta_y):
    turtle.penup()
    turtle.goto(delta_x, delta_y)
    for i in coords:
        turtle.pendown()
        turtle.goto(i[0]+delta_x, i[1]+delta_y)
        turtle.penup()



one(num1, 0, -40)
four(num4, 50, 0)
one(num1, 100, -40)
seven(num7, 150, 0)
zero(num0, 200, 0)
zero(num0, 250, 0)


#zero(num0, -50, 0)
#one(num1, 0, -40)
#two(num2, 50, 0)
#three(num3, 100, 0)
#four(num4, 150, 0)
#five(num5, 200, 0)
#six(num6, 290, 0)
#seven(num7, 300, 0)
#eight(num8, 350, 0)
#nine(num9, 400, 0)


turtle.mainloop()
