import sys
import numpy as np
import matplotlib.pyplot as plt
import percolation
import percolation01

n = int(sys.argv[1])
p = float(sys.argv[2])
trials = int(sys.argv[3])

for i in range(trials):
    isOpen = percolation01.random(n, p)
    percolation01.draw(isOpen)
    plt.show()

    isFull = percolation.flow(isOpen)

    visualization_matrix = np.where(isFull, 2, isOpen)

    percolation01.draw(visualization_matrix)
    plt.show()
