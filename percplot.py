import numpy as np
import matplotlib.pyplot as plt
import sys
import estimate01

def estimate_evaluate(n, x, trials):
    return np.sin(np.pi * x)


def curve(n, x0, y0, x1, y1, trials=100, gap=0.01, err=0.0025):
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = estimate01.evaluate(n, xm, trials)

    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        plt.plot([x0, x1], [y0, y1], 'k-', lw=1)
        return

    curve(n, x0, y0, xm, fxm)
    plt.plot(xm, fxm, 'ko', markersize=2)
    curve(n, xm, fxm, x1, y1)



n = int(sys.argv[1])
plt.figure(figsize=(8, 6))
plt.gca().set_aspect('equal', adjustable='box')
curve(n, 0.0, 0.0, 1.0, 1.0)
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)


plt.show()
