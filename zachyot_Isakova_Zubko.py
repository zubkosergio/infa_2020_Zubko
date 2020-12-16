import numpy as np
import turtle


FPS = 2
vectors = []
print('введите данные о длине, высоте, уклоне рисунка и количестве точек')
L = int(input())
h = int(input())
a = int(input())
t = int(input())
A = np.array([0, 0]) # нулевой вектор
G = np.array([L, 0]) # вектор, рисующий линию снизу
n = 2 * t
r_vectors = []
dots = [(0, 0)]
r_dots = []
R = np.array([-1, 1])  # отражающий вектор
B = np.array([0, h + (L / 2) * np.sin(a * np.pi / 180)]) # вспомогательный вектор


def vectorall(L, h, a, t, A, B, G, dots):
    def vectoring(f, L, h, a, k, A, B, G, dots):
        for i in range(k + 2):
            vk_x = np.array([L / f, 0])
            if i >= k + 1:
                vk_y = np.array([0, h + (L / 2) * np.sin(a * np.pi / 180)])
                vk_rem = vk_y
            else:
                if i == 0:
                    vk_y = np.array([0, h])
                    vk_rem = vk_y
                elif i % 2 == 0:
                    vk_y = np.array([0, h + (L / (f) * i) * np.sin(a * np.pi / 180)])
                    vk_rem = vk_x + vk_y
                else:
                    vk_y = np.array([0, h + (L * (i - 1) / f) * np.sin(a * np.pi / 180)])
                    vk_rem = vk_x - vk_y
            vectors.append(vk_rem)
            r_vectors.append(vk_rem * R)
            A = A + vectors[i]
            dots.append((A[0], A[1]))
            G = G + r_vectors[i]
            r_dots.append((G[0], G[1]))
        r_dots.pop()

    if t % 2 == 0:
        A = A + np.array([L / n, 0])
        G = G - np.array([L / n, 0])
        r_dots.append((L, 0))
        k = t - 1
        f = n - 2
        L = L * (n - 2) / n
        vectoring(f, L, h, a, k, A, B, G, dots)
    else:
        k = t
        f = n
        vectoring(f, L, h, a, k, A, B, G, dots)



vectorall(L, h, a, t, A, B, G, dots)
r_dots.reverse()
turtle.hideturtle()
turtle.setposition(dots[1])

for i in range(len(r_dots)):
    dots.append(r_dots[i])

for i in range(len(dots)):
    if i == 0:
        turtle.penup()
        turtle.goto(dots[i])
        turtle.pendown()
    turtle.goto(dots[i])
    turtle.speed(100)

Up = []
Down = []
for i in range(len(dots)):
    if i%2 == 0:
        Up.append(dots[i])
    else:
        Down.append(dots[i])
if t%2 == 0:
    Down.reverse()
else:
    Up.reverse()
Final_mas = []
for i in range(len(Up)):
    Final_mas.append(Up[i])
for i in range(len(Down)):
    Final_mas.append(Down[i])

for i in range(len(Final_mas)):
    turtle.goto(Final_mas[i])
turtle.mainloop()
print(Final_mas)




