""" Set up an environment to run a percolation simulation. 
"""
import random

clusters = []
clusters.append([])

class Site:
    """ A node for a lattice. 
    """
    occupied = 0
    visited = 0

    def __init__(self, x, y, occupied):
        self.x = x
        self.y = y
        self.occupied = occupied
        self.visited = False
        self.group = 0

        if self.occupied:
            Site.occupied += 1

    def __str__(self):
        output = '{0}'.format(self.group)

        if self.occupied:
            output = '[' + output + ']'

        return output

def create2DGrid( porosity = 1.0, size = 5 ):
    """ Create a grid of [ size X size ] in 2 dimensions with a specified 
        porosity. 
    """
    grid = []
    for i in range( size ):
        grid.append([])
        for j in range( size ):
            occupied = False

            if porosity < random.random():  # Algorithm 3.8 - pg. 87
                occupied = True

            grid[i].append( Site(i, j, occupied) )

    return grid

def print2DGrid( grid ):
    """ Display a grid with the cluster label identifier.
    """
    for i in range(len(grid)):
        print('%s' % ', '.join(map(str, grid[i])))
        print('\n')

def walkGrid(grid, i, j, lbl):
    """ Walk a grid and determine the cluster label for this site.
    """
    size = len(grid)
    if i >= size or i < 0 or j >= size or j < 0:
        return

    if grid[i][j+1].occupied:
        walkGrid(grid, i, j + 1, lbl)
    if grid[i+1][j].occupied:
        walkGrid(grid, i + 1, j, lbl)
    if grid[i][j-1].occupied:
        walkGrid(grid, i, j - 1, lbl)
    if grid[i-1][j].occupied:
        walkGrid(grid, i - 1, j, lbl)

    grid[i][j].group = lbl
    grid[i][j].visited = True

    Site.visited += 1

def analyzeGrid( grid ):
    """ Determine the clusters for a grid.
        Based on Algorithm 3.9 - pg. 90
    """
    size = len(grid)
    lbl = 1
    while Site.visited < Site.occupied:
        for i in range(size):
            for j in range(size):
                if grid[i][j].occupied and not grid[i][j].visited:
                    print("Found at [{0}, {1}], Label = {2}".format(i, j, lbl))
                    walkGrid(grid, i, j, lbl)
                    lbl += 1

if __name__ == "__main__":
    p = 0.5
    size = 10

    lattice = create2DGrid(p, size)
    print("Initial Grid:")
    print2DGrid( lattice )

    print("Occupied Sites: {0} out of {1}".format(Site.occupied, size*size))