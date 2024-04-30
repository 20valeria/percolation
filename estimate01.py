import sys
import stdio
import percolation
import percolation01

def evaluate(n, р, trials):
    count = 0
    for i in range(trials):
        isOpen = percolation01.random(n, р)
        if (percolation.percolates( isOpen )):
            count += 1
    return (1.0 * count / trials) * 100


def main( ):
    n = int(sys.argv[1])
    р = float(sys.argv[2])
    trials = int(sys.argv[3])
    q = evaluate(n, р, trials)
    print(q)


if __name__ == "__main__":
    main( )