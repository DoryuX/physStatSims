import sys
import random
import math

def create2DGrid( prob = 0.5, size = 5 ):
    """ Create a grid of [ size X size ] in 2 dimensions with all -1. 
    """
    grid = []

    for i in range( size + 1 ):
        grid.append([])
        for j in range( size + 1 ):
            if i != 0 and j != 0:
                if random.random() < prob:
                    grid[i].append(-1)
                else:
                    grid[i].append(1)
            else:
                grid[i].append(0)

    return grid

def ising( grid, Jkt, msMax, transient, numToDiscard ):
    size = len(grid)

    ip = [0]
    im = [0]

    W = {}

    # Look-up table for mod.
    for i in range(1, size):
        ip.append(i + 1)
        im.append(i - 1)

    ip[size - 1] = 1
    im[1] = size - 1

    # Look-up table.
    for i in range(-4, 6, 2):
        W[i] = 1

        if i > 0:
            W[i] = math.exp(-2 * Jkt * i)

    # Monte Carlo
    count = 0
    for mcs in range(1, msMax):
        for i in range(1, size):
            for j in range(1, size):
                ici = grid[i][j]
                ien = grid[ip[i]][j] + grid[im[i]][j] + grid[i][ip[j]] + grid[i][im[j]]
                ien *= ici

                if random.random() < W[ien]:
                    grid[i][j] = -ici

            if mcs >= transient:
                count += 1
                if count == numToDiscard:
                    count = 0
                    # Do Analysis.

def print2DGrid( grid ):
    """ Display a grid with the cluster label identifier.
    """
    for i in range(len(grid)):
        print('%s' % ', '.join(map(str, grid[i])))
        print('\n')

if __name__ == "__main__":
    lattice = create2DGrid( 0.5, 5 )

    print2DGrid(lattice)

    ising(lattice, 4.0, 100, 8, 4)

    print2DGrid(lattice)

