""" Set up an environment to run a percolation simulation. 
"""
import sys
import random
import time

class Site:
    """ A node for a lattice. 
    """
    occupied = 0
    visited = 0
    clusters = [[]]
    spanning = []

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

        if self.occupied and not self.visited:
            output = '[' + output + ']'

        return output

def create2DGrid( porosity = 1.0, size = 5 ):
    """ Create a grid of [ size X size ] in 2 dimensions with a specified 
        porosity. 
    """
    grid = []
    Site.occupied = 0

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

def findSpanning( grid ):
    size = len(grid)

    lgroups = []
    tgroups = []

    rspanning = []
    bspanning = []

    # Left and Top edge group
    for i in range(size):
        # Left Edge
        if grid[i][0].occupied and grid[i][0].group > 0 and not lgroups.count(grid[i][0].group):
            lgroups.append(grid[i][0].group)
        # Top Edge
        if grid[i][0].occupied and grid[0][i].group > 0 and not tgroups.count(grid[0][i].group):
            tgroups.append(grid[0][i].group)

    # Find Spanning Clusters ( If they reach Left to Right )
    for x in lgroups:
        for i in range(size):
            if grid[i][size-1].group > 0 and grid[i][size-1].group == x and not rspanning.count(x): 
                rspanning.append(x)

    for x in tgroups:
        for i in range(size):
            if grid[size - 1][i].group > 0 and grid[size-1][i].group == x and not bspanning.count(x): 
                bspanning.append(x)

    spanning = {'LR': rspanning, 'TB': bspanning}

    # Return union of lists.
    return spanning
            

def analyzeGrid( grid ):
    i = j = 0
    group = 0
    size = len(grid)
    stack = []
    clusters = [[]]
    
    for k in range(size):
        for l in range(size):
            if grid[k][l].occupied and not grid[k][l].visited:
                stack.append([k, l])

                group += 1
                clusters.append([])
                clusters[group].append([k, l])

                while stack:
                    i, j = stack.pop()
                    
                    # Right
                    if(i + 1 < size and grid[i + 1][j].occupied and not grid[i + 1][j].visited):
                        stack.append([i + 1, j])
                        clusters[group].append([i + 1, j])
					
					# Up
                    if(j + 1 < size and grid[i][j + 1].occupied and not grid[i][j + 1].visited):
                        stack.append([i, j + 1])
                        clusters[group].append([i, j + 1])
					
                    # Left
                    if(i - 1 >= 0 and grid[i - 1][j].occupied and not grid[i - 1][j].visited):
                        stack.append([i - 1, j])
                        clusters[group].append([i - 1, j])
					
					# Down
                    if(j - 1 >= 0 and grid[i][j - 1].occupied and not grid[i][j - 1].visited):
                        stack.append([i, j - 1])
                        clusters[group].append([i, j - 1])
                    
                    # Mark this place as visited so we can skip then later.
                    grid[i][j].visited = True
                    grid[i][j].group = group
				
            # Mark visited, even unoccupied ones.
            grid[k][l].visited = True
    
    return clusters

if __name__ == "__main__":
    argc = len(sys.argv)
    showGrid = False
    runs = 1

    # Values for avg p_inf
    p_inf_avg = []
    p_inf_sum = 0
    p = 0

    # Start Timer
    time.clock()

    if argc >= 2:
        size = int(sys.argv[1]) 
    else: 
        size = 5

    if argc >= 3:
        runs = int(sys.argv[2])
    
    if argc >= 4 and sys.argv[3] == 'True':
        showGrid = True

    fileName = "./output/percolation/perc_{0}x{0}_{1}runs.dat".format(size, runs)
    outFile = open(fileName, 'w')

    print("Size: {0}, Show: {1}".format(size, showGrid))

    for j in range(21):
        p_inf_sum = 0
        p = j / 20.0

        for i in range(runs):
            lattice = create2DGrid(p, size)

            if showGrid:
                print("Initial Grid:")
                print2DGrid( lattice )

            Site.clusters = analyzeGrid( lattice )
            Site.spanning = findSpanning(lattice)

            # P Infinity
            c_max = 0
            for c in Site.clusters:
                if len(c) > c_max:
                    c_max = len(c)

            # If there is no spanning cluster, skip it.
            if len(Site.spanning) > 0 and Site.occupied > 0:
                p_inf_sum = (c_max / Site.occupied)
            else:
                p_inf_sum = 0

            if showGrid:
                print2DGrid( lattice )

                print("Spanning Clusters: ")
                print(Site.spanning)
                print("Occupied Sites: {0} out of {1}".format(Site.occupied, size*size))

        p_inf_avg.append(p_inf_sum / runs)

        print("Run {0} of {1}.".format(j, 20))
        outFile.write("{0} {1:.3f}\n".format(p, p_inf_avg[j]))

    print("Time: {0}s".format(time.clock()))

    outFile.close()
