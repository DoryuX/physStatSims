""" Set up an environment to run a percolation simulation. 
"""
import random

class Site:
    """ A node for a lattice. 
    """
    occupied = 0
    visited = 0
    clusters = [[]]

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
	i = j = 0
	group = 0
	size = len(grid)
	stack = []

	print("Grid: {0}x{0}\n".format(size))

	for k in range(size):
		for l in range(size):
			if grid[k][l].occupied and not grid[k][l].visited:
				stack.append([k, l])
				
				group += 1
				Site.clusters.append([])
				Site.clusters[group].append([k, l])
				
				while stack:
					i, j = stack.pop()
					
					# Right
					if(i + 1 < size and grid[i + 1][j].occupied and not grid[i + 1][j].visited):
						stack.append([i + 1, j])
						Site.clusters[group].append([i + 1, j])
					
					# Up
					if(j + 1 < size and grid[i][j + 1].occupied and not grid[i][j + 1].visited):
						stack.append([i, j + 1])
						Site.clusters[group].append([i, j + 1])
					
					# Left
					if(i - 1 >= 0 and grid[i - 1][j].occupied and not grid[i - 1][j].visited):
						stack.append([i - 1, j])
						Site.clusters[group].append([i - 1, j])
					
					# Down
					if(j - 1 >= 0 and grid[i][j - 1].occupied and not grid[i][j - 1].visited):
						stack.append([i, j - 1])
						Site.clusters[group].append([i, j - 1])
					
					# Mark this place as visited so we can skip then later.
					grid[i][j].visited = True
					grid[i][j].group = group
				
			# Mark visited, even unoccupied ones.
			grid[k][l].visited = True

if __name__ == "__main__":
	p = 0.5
	size = 5

	lattice = create2DGrid(p, size)
	print("Initial Grid:")
	print2DGrid( lattice )
	analyzeGrid( lattice )
	print2DGrid( lattice )

	print("Occupied Sites: {0} out of {1}".format(Site.occupied, size*size))
