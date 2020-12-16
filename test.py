import numpy as np


def py_update(u):
    nx, ny = u.shape

    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            u[i, j] = round(0.25 * ((u[i - 1, j] + u[i + 1, j]) +
                                    (u[i, j - 1] + u[i, j + 1])), 2)


def calc(N=10, Niter=100, func=py_update):
    u = np.zeros([N, N])
    for i in range(N):
        u[0, i] = 2
        u[i, 0] = 0
        u[N - 1, i] = 1
        u[i, N - 1] = 1
    for i in range(Niter):
        func(u)
        print(u)
        return u


u = calc(func=py_update, N=10)
