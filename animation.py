import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation
import percolation01


def update_flow(isOpen, isFull, n):
    updated = False
    for i in range(n):
        for j in range(n):
            if isFull[i][j]:
                for di, dj in [(1, 0), (0, 1), (0, -1)]: # Вниз, вправо, влево
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if isOpen[ni][nj] and not isFull[ni][nj]:
                            isFull[ni][nj] = True
                            updated = True
    return updated



def init():
    mat.set_data(display_matrix(isOpen, isFull))
    return [mat]


def display_matrix(isOpen, isFull):
    matrix = np.zeros(isOpen.shape)
    matrix[isOpen & ~isFull] = 1
    matrix[isFull] = 2
    return matrix

def update(frame):
    updated = update_flow(isOpen, isFull, n)
    if updated:
        mat.set_data(display_matrix(isOpen, isFull))
    return [mat]

n = 200
p = 0.63

isOpen = percolation01.random(n, p)
isFull = np.zeros((n, n), dtype=bool)
isFull[0, :] = isOpen[0, :]

fig, ax = plt.subplots()
cmap = mcolors.ListedColormap(['black', 'white', 'blue'])
bounds = [0, 1, 2, 3]
norm = mcolors.BoundaryNorm(bounds, cmap.N)
mat = ax.matshow(display_matrix(isOpen, isFull), cmap=cmap, norm=norm)
plt.axis('off')

ani = FuncAnimation(fig, update, frames=range(400), init_func=init, blit=True, interval=300)

plt.show()