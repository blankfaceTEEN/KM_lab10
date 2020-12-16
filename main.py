import numpy as np

import matplotlib.pyplot as plt


def update(u):
    global canvas
    global count
    global y
    nx, ny = u.shape
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            u[i, j] = round(0.25 * ((u[i - 1, j] + u[i + 1, j]) +
                                    (u[i, j - 1] + u[i, j + 1])), 2)
            y.append(u[i, j])
            print('значение в [', i ,',',j,']:', u[i, j])
            count += 1
    return u


def calc(points, n):
    matrix = np.zeros([points, points])  # создал матрицу

    # Количество точек 10
    for i in range(points):
        matrix[0, i] = 2
        matrix[i, 0] = 0
        matrix[points - 1, i] = 1
        matrix[i, points - 1] = 1

    # Количество блужданий 100
    for i in range(n):
        print('БЛУЖДАНИЕ №' + str(i))
        matrix = update(matrix)

    print(matrix)

x = []
y = []
count = 0
calc(10, 100)
for i in range(len(y)):
    x.append(i)
fig, ax = plt.subplots()
ax.scatter(x, y)
fig.set_figwidth(100)
plt.show()
