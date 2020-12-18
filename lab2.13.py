import turtle as t

def circle(x):
    for i in range(0, 360):
        t.forward(x)
        t.left(1)
def arc(x):
    for i in range(0, 180):
        t.forward(x)
        t.right(1)


t.speed(100)
t.shape('turtle')
t.color('yellow')
t.begin_fill()
circle(1)
t.end_fill()
t.penup()
t.goto(30, 60)
t.pendown()
t.color('blue')
t.begin_fill()
circle(1 / 6)
t.end_fill()
t.penup()
t.goto(-30, 60)
t.pendown()
t.color('blue')
t.begin_fill()
circle(1 / 6)
t.end_fill()
t.penup()
t.width(7)
t.goto(0, 55)
t.pendown()
t.right(90)
t.color('black')
t.forward(18)
t.penup()
t.goto(40, 50)
t.color('red')
t.pendown()
arc(0.69)