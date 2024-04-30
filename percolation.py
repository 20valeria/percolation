import numpy as np

def _flow(isOpen, isFull, i, j):
    n = len(isFull)
    if i < 0 or i >= n or j < 0 or j >= n:
        return
    if not isOpen[i][j] or isFull[i][j]:
        return
    isFull[i][j] = True

    _flow(isOpen, isFull, i + 1, j)  # Вниз
    _flow(isOpen, isFull, i, j + 1)  # Вправо
    _flow(isOpen, isFull, i, j - 1)  # Влево



def flow(isOpen):
    n = len(isOpen)
    isFull = np.zeros((n, n), dtype=bool)
    for j in range(n):
        _flow(isOpen, isFull, 0, j)
    return isFull

def percolates(isOpen):
    isFull = flow(isOpen)
    n = len(isFull)
    for j in range(n):
        if isFull[n - 1][j]:
            return True
    return False

