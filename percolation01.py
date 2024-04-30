import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def random(n, p):
    a = np.random.choice([False, True], size=(n, n), p=[1 - p, p])
    return a

def draw(matrix):
    cmap = mcolors.ListedColormap(['black', 'white', 'blue'])
    bounds = [0, 0.5, 1.5, 2]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)
    plt.figure(figsize=(6, 6))
    plt.imshow(matrix, cmap=cmap, norm=norm)
    plt.axis('scaled')

def main():

    n = int(sys.argv[1])
    p = float(sys.argv[2])
    test = random(n, p)
    draw(test, False)


if __name__ == "__main__":
    main()
