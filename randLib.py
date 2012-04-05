import sys
import math
#import mathutils
import random
import datetime

# Direction Map 1D
# =======
#  2 . 1
# =======
def nnX1D( i ):
    if i == 1:
        result = 1
    elif i == 2:
        result = -1
    else:
        result = 0
    return result

# Direction Map 2D
# =======
#    2
#  3 . 1
#    4
# =======
def nnX2D( i ):
    if i == 1:
        result = 1
    elif i == 3:  #was 3
        result = -1
    else:
        result = 0
    return result

def nnY2D( i ):
    if i == 2:
        result = 1
    elif i == 4:
        result = -1
    else:
        result = 0
    return result

# Direction Map 3D
# =======
#    2
#  3 . 1	5 = +Z, 6 = -Z
#    4
# =======
def nnX3D( i ):
    if i == 1:
        result = 1
    elif i == 2:  #was 3
        result = -1
    else:
        result = 0
    return result

def nnY3D( i ):
    if i == 2:
        result = 1
    elif i == 4:
        result = -1
    else:
        result = 0
    return result

def nnZ3D( i ):
    if i == 5:
        result = 1
    elif i == 6:
        result = -1
    else:
        result = 0
    return result

# Direction Map 4D
# =======
#    2
#  3 . 1	5 = +Z, 6 = -Z
#    4		7 = +W, 8 = +W
# =======
def nnX4D( i ):
    if i == 1:
        result = 1
    elif i == 2:  #was 3
        result = -1
    else:
        result = 0
    return result

def nnY4D( i ):
    if i == 2:
        result = 1
    elif i == 4:
        result = -1
    else:
        result = 0
    return result

def nnZ4D( i ):
    if i == 5:
        result = 1
    elif i == 6:
        result = -1
    else:
        result = 0
    return result

def nnW4D( i ):
    if i == 7:
        result = 1
    elif i == 8:
        result = -1
    else:
        result = 0
    return result

#
# 0 - Wall
# 1 - Open
# 2 - Visited
#
def create3DGrid( porosity, size ):
    grid = []
    for i in range( size ):
        grid.append([])
        for j in range( size ):
            grid[i].append([])
            for k in range( size ):
                grid[i][j].append( 1 )

    for i in range(int(size**3 * porosity)):
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        z = random.randint(0, size-1)

        grid[x][y][z] = 0

    return grid

#
# 0 - Wall
# 1 - Open
# 2 - Visited
#
def create2DGrid( size ):
    grid = []
    for i in range( size ):
        grid.append([])
        for j in range( size ):
            grid[i].append([])
            for k in range( size ):
                grid[i][j].append( 1 )

    return grid

#
# simpleRandomWalk1D
#
def simpleRandomWalk1D( steps, repeat ):
    row = 0
    col = 0

    stepGrid = []
    sumX = []

    originFlag = False
    originCount = 0

    # Initialize Grid
    for i in range( steps ):
        stepGrid.append([])
        sumX.append(0)
        #r.append([])
        for j in range( repeat ):
            stepGrid[i].append(0)
            #r[i].append(0)


    while col < repeat:
        x = 0
        xDir = 0
        prevX = 0
        while row < steps:
            direction = random.randint(1, 2)

            xDir = nnX1D( direction )

            prevX = x

            x += xDir

            stepGrid[row][col] = x
            sumX[row] += x
            #r[row][col] = math.sqrt( x**2 )
            if x == 0:
                originFlag = True

            row += 1
        col += 1
        row = 0

        if originFlag:
            originCount += 1
            originFlag = False

    # output
    row = 0
    col = 0

    fileName = './output/1D/randWalk_1D_st' + str(steps) + '_sa' + str(repeat) + '.dat'
    fileNameP0_X = './output/1D/randWalk_1D_st' + str(steps) + '_sa' + str(repeat) + '_P0_X.dat'

    outFile = open(fileName, 'w')

    # Print out walks
    while row < steps:
        outFile.write( "%6d" % ( row ) )

        while col < repeat:
            outFile.write( "%6d" % ( stepGrid[row][col] ) )
            col += 1

        avgX = ( sumX[row] / repeat )
        outFile.write( "%8.2f" % ( avgX ) )     # Average X
        outFile.write( "%8.2f" % ( avgX**2 ) )  # Average X Squared

        outFile.write( "\n" )
        col = 0
        row += 1

    outFile.close()

    probFile = open(fileNameP0_X, 'w')
    probFile.write( "%8.2f\n" % (originCount / repeat) )
    probFile.close()
#### END OF 1D

#
# simpleRandomWalk2D
#
def simpleRandomWalk2D( steps, repeat ):
    row = 0
    col = 0
    stepGridX = []
    stepGridY = []
    sumX = []
    sumY = []
    originFlag = False
    originCount = 0

    # Initialize Grid
    for i in range( steps ):
        stepGridX.append([])
        stepGridY.append([])
        sumX.append(0)
        sumY.append(0)
        #r.append([])
        for j in range( repeat ):
            stepGridX[i].append(0)
            stepGridY[i].append(0)


    while col < repeat:
        x = 0
        y = 0

        xDir = 0
        yDir = 0

        prevX = 0
        prevY = 0

        while row < steps:
            direction = random.randint(1, 4)

            xDir = nnX2D( direction )
            yDir = nnY2D( direction )

            prevX = x
            prevY = y

            x += xDir
            y += yDir

            stepGridX[row][col] = x
            stepGridY[row][col] = y

            sumX[row] += x
            sumY[row] += y

            if x == 0 and y == 0:
                originFlag = True

            row += 1
        col += 1
        row = 0

        if originFlag:
            originCount += 1
            originFlag = False

    # output
    row = 0
    col = 0

    fileName_X = './output/2D/randWalk_2D_st' + str(steps) + '_sa' + str(repeat) + '_X.dat'
    fileName_Y = './output/2D/randWalk_2D_st' + str(steps) + '_sa' + str(repeat) + '_Y.dat'
    fileName_P0 = './output/2D/randWalk_2D_st' + str(steps) + '_sa' + str(repeat) + '_P0.dat'

    outFile_X = open(fileName_X, 'w')
    outFile_Y = open(fileName_Y, 'w')

    # Print out walks
    while row < steps:
        outFile_X.write( "%6d" % ( row ) )
        outFile_Y.write( "%6d" % ( row ) )

        while col < repeat:
            outFile_X.write( "%6d" % ( stepGridX[row][col] ) )
            outFile_Y.write( "%6d" % ( stepGridY[row][col] ) )
            col += 1

        avgX = ( sumX[row] / repeat )
        avgY = ( sumY[row] / repeat )

        outFile_X.write( "%8.2f" % ( avgX ) )     # Average X
        outFile_X.write( "%8.2f" % ( avgX**2 ) )  # Average X Squared
        outFile_X.write( "\n" )

        outFile_Y.write( "%8.2f" % ( avgY ) )     # Average Y
        outFile_Y.write( "%8.2f" % ( avgY**2 ) )  # Average Y Squared
        outFile_Y.write( "\n" )

        col = 0
        row += 1

    outFile_X.close()
    outFile_Y.close()

    probFile = open(fileName_P0, 'w')
    probFile.write( "%8.2f\n" % (originCount / repeat) )
    probFile.close()
#### END OF 2D

#
# simpleRandomWalk3D
#
def simpleRandomWalk3D( steps, repeat ):
    row = 0
    col = 0
    stepGridX = []
    stepGridY = []
    stepGridZ = []
    sumX = []
    sumY = []
    sumZ = []
    originFlag = False
    originCount = 0

    # Initialize Grid
    for i in range( steps ):
        stepGridX.append([])
        stepGridY.append([])
        stepGridZ.append([])
        sumX.append(0)
        sumY.append(0)
        sumZ.append(0)
        #r.append([])
        for j in range( repeat ):
            stepGridX[i].append(0)
            stepGridY[i].append(0)
            stepGridZ[i].append(0)


    while col < repeat:
        x = 0
        y = 0
        z = 0

        xDir = 0
        yDir = 0
        zDir = 0

        prevX = 0
        prevY = 0
        prevZ = 0

        while row < steps:
            direction = random.randint(1, 6)

            xDir = nnX3D( direction )
            yDir = nnY3D( direction )
            zDir = nnZ3D( direction )

            prevX = x
            prevY = y
            prevZ = z

            x += xDir
            y += yDir
            z += zDir

            stepGridX[row][col] = x
            stepGridY[row][col] = y
            stepGridZ[row][col] = z

            sumX[row] += x
            sumY[row] += y
            sumZ[row] += z

            if x == 0 and y == 0 and z == 0:
                originFlag = True

            row += 1
        col += 1
        row = 0

        if originFlag:
            originCount += 1
            originFlag = False

    # output
    row = 0
    col = 0

    fileName_X = './output/3D/randWalk_3D_st' + str(steps) + '_sa' + str(repeat) + '_X.dat'
    fileName_Y = './output/3D/randWalk_3D_st' + str(steps) + '_sa' + str(repeat) + '_Y.dat'
    fileName_Z = './output/3D/randWalk_3D_st' + str(steps) + '_sa' + str(repeat) + '_Z.dat'
    fileName_P0 = './output/3D/randWalk_3D_st' + str(steps) + '_sa' + str(repeat) + '_P0.dat'

    outFile_X = open(fileName_X, 'w')
    outFile_Y = open(fileName_Y, 'w')
    outFile_Z = open(fileName_Z, 'w')

    # Print out walks
    while row < steps:
        outFile_X.write( "%6d" % ( row ) )
        outFile_Y.write( "%6d" % ( row ) )
        outFile_Z.write( "%6d" % ( row ) )

        while col < repeat:
            outFile_X.write( "%6d" % ( stepGridX[row][col] ) )
            outFile_Y.write( "%6d" % ( stepGridY[row][col] ) )
            outFile_Z.write( "%6d" % ( stepGridZ[row][col] ) )
            col += 1

        avgX = ( sumX[row] / repeat )
        avgY = ( sumY[row] / repeat )
        avgZ = ( sumZ[row] / repeat )

        outFile_X.write( "%8.2f" % ( avgX ) )     # Average X
        outFile_X.write( "%8.2f" % ( avgX**2 ) )  # Average X Squared
        outFile_X.write( "\n" )

        outFile_Y.write( "%8.2f" % ( avgY ) )     # Average Y
        outFile_Y.write( "%8.2f" % ( avgY**2 ) )  # Average Y Squared
        outFile_Y.write( "\n" )

        outFile_Z.write( "%8.2f" % ( avgZ ) )     # Average Z
        outFile_Z.write( "%8.2f" % ( avgZ**2 ) )  # Average Z Squared
        outFile_Z.write( "\n" )

        col = 0
        row += 1

    outFile_X.close()
    outFile_Y.close()
    outFile_Z.close()

    probFile = open(fileName_P0, 'w')
    probFile.write( "%8.2f\n" % (originCount / repeat) )
    probFile.close()
#### END OF 3D

#
# simpleRandomWalk4D
#
def simpleRandomWalk4D( steps, repeat ):
    row = 0
    col = 0
    stepGridX = []
    stepGridY = []
    stepGridZ = []
    stepGridW = []
    sumX = []
    sumY = []
    sumZ = []
    sumW = []
    originFlag = False
    originCount = 0

    # Initialize Grid
    for i in range( steps ):
        stepGridX.append([])
        stepGridY.append([])
        stepGridZ.append([])
        stepGridW.append([])
        sumX.append(0)
        sumY.append(0)
        sumZ.append(0)
        sumW.append(0)
        #r.append([])
        for j in range( repeat ):
            stepGridX[i].append(0)
            stepGridY[i].append(0)
            stepGridZ[i].append(0)
            stepGridW[i].append(0)


    while col < repeat:
        x = 0
        y = 0
        z = 0
        w = 0

        xDir = 0
        yDir = 0
        zDir = 0
        wDir = 0

        prevX = 0
        prevY = 0
        prevZ = 0
        prevW = 0

        while row < steps:
            direction = random.randint(1, 8)

            xDir = nnX4D( direction )
            yDir = nnY4D( direction )
            zDir = nnZ4D( direction )
            wDir = nnW4D( direction )

            prevX = x
            prevY = y
            prevZ = z
            prevW = w

            x += xDir
            y += yDir
            z += zDir
            w += wDir

            stepGridX[row][col] = x
            stepGridY[row][col] = y
            stepGridZ[row][col] = z
            stepGridW[row][col] = w

            sumX[row] += x
            sumY[row] += y
            sumZ[row] += z
            sumW[row] += w

            if x == 0 and y == 0 and z == 0 and w == 0:
                originFlag = True

            row += 1
        col += 1
        row = 0

        if originFlag:
            originCount += 1
            originFlag = False

    # output
    row = 0
    col = 0

    fileName_X = './output/4D/randWalk_4D_st' + str(steps) + '_sa' + str(repeat) + '_X.dat'
    fileName_Y = './output/4D/randWalk_4D_st' + str(steps) + '_sa' + str(repeat) + '_Y.dat'
    fileName_Z = './output/4D/randWalk_4D_st' + str(steps) + '_sa' + str(repeat) + '_Z.dat'
    fileName_W = './output/4D/randWalk_4D_st' + str(steps) + '_sa' + str(repeat) + '_W.dat'
    fileName_P0 = './output/4D/randWalk_4D_st' + str(steps) + '_sa' + str(repeat) + '_P0.dat'

    outFile_X = open(fileName_X, 'w')
    outFile_Y = open(fileName_Y, 'w')
    outFile_Z = open(fileName_Z, 'w')
    outFile_W = open(fileName_W, 'w')

    # Print out walks
    while row < steps:
        outFile_X.write( "%6d" % ( row ) )
        outFile_Y.write( "%6d" % ( row ) )
        outFile_Z.write( "%6d" % ( row ) )
        outFile_W.write( "%6d" % ( row ) )

        while col < repeat:
            outFile_X.write( "%6d" % ( stepGridX[row][col] ) )
            outFile_Y.write( "%6d" % ( stepGridY[row][col] ) )
            outFile_Z.write( "%6d" % ( stepGridZ[row][col] ) )
            outFile_W.write( "%6d" % ( stepGridW[row][col] ) )
            col += 1

        avgX = ( sumX[row] / repeat )
        avgY = ( sumY[row] / repeat )
        avgZ = ( sumZ[row] / repeat )
        avgW = ( sumW[row] / repeat )

        outFile_X.write( "%8.2f" % ( avgX ) )     # Average X
        outFile_X.write( "%8.2f" % ( avgX**2 ) )  # Average X Squared
        outFile_X.write( "\n" )

        outFile_Y.write( "%8.2f" % ( avgY ) )     # Average Y
        outFile_Y.write( "%8.2f" % ( avgY**2 ) )  # Average Y Squared
        outFile_Y.write( "\n" )

        outFile_Z.write( "%8.2f" % ( avgZ ) )     # Average Z
        outFile_Z.write( "%8.2f" % ( avgZ**2 ) )  # Average Z Squared
        outFile_Z.write( "\n" )

        outFile_W.write( "%8.2f" % ( avgW ) )     # Average Z
        outFile_W.write( "%8.2f" % ( avgW**2 ) )  # Average Z Squared
        outFile_W.write( "\n" )

        col = 0
        row += 1

    outFile_X.close()
    outFile_Y.close()
    outFile_Z.close()
    outFile_W.close()

    probFile = open(fileName_P0, 'w')
    probFile.write( "%8.2f\n" % (originCount / repeat) )
    probFile.close()
#### END OF 4D

def nonReversalRandomWalk( shape, n ):
    count = 0

    x = 0
    y = 0
    z = 0

    xDir = 0
    yDir = 0
    zDir = 0

    prevX = 0
    prevY = 0
    prevZ = 0

    rotX = 0.0
    rotY = 0.0
    rotZ = 0.0

    #outFile.write( "%s\n%s\n%s" % 
    #    ( "Non-Reversal Random Walk",
    #      "=========================",
    #      "t  x(t)  y(t)  z(t)     X     Y     Z\n" ) )

    while count < n:
        direction = random.randint(1, 6)

        xDir = nnX( direction )
        yDir = nnY( direction )
        zDir = nnZ( direction )

        while (x + xDir == prevX) and (y + yDir == prevY) and (z + zDir == prevZ):
            direction = random.randint(1, 6)

            xDir = nnX( direction )
            yDir = nnY( direction )
            zDir = nnZ( direction )

        prevX = x
        prevY = y
        prevZ = z

        x += xDir
        y += yDir
        z += zDir

        #if x != 0:
            #    rotX = 1.57
            #if z != 0:
                #    rotY = 1.57

        shape.delta_location = mathutils.Vector((x,y,z))

        #addCylinder(mathutils.Vector((
        #                        (x + prevX)/2.0, 
        #                        (y + prevY)/2.0, 
        #                        (z + prevZ)/2.0)),
        #            mathutils.Euler((rotX, rotY, rotZ)))

        outFile.write( "%6d%6d%6d%6d%6d%6d\n" % ( x, y, z, xDir, yDir, zDir ) )

        count += 1

#
# randomWalkInMedia
#
def randomWalkInMedia( steps, repeat, porosity, size ):
    row = 0
    col = 0
    rGrid = []
    r2Grid = []
    sumR = []
    sumR2 = []

    grid = create3DGrid( 1 - porosity, size )

    # Initialize Grid
    for i in range( steps ):
        rGrid.append([])
        r2Grid.append([])
        sumR.append(0)
        sumR2.append(0)
        #r.append([])
        for j in range( repeat ):
            rGrid[i].append(0)
            r2Grid[i].append(0)

    while col < repeat:
        x = 0
        y = 0
        z = 0

        xDir = 0
        yDir = 0
        zDir = 0

        prevX = 0
        prevY = 0
        prevZ = 0

        while row < steps:
            direction = random.randint(1, 6)

            xDir = nnX3D( direction )
            yDir = nnY3D( direction )
            zDir = nnZ3D( direction )

            # If a site is blocked, move some where else.
            while (grid[x + xDir][y + yDir][z + zDir] == 0):
                direction = random.randint(1, 6)

                xDir = nnX3D( direction )
                yDir = nnY3D( direction )
                zDir = nnZ3D( direction )

            prevX = x
            prevY = y
            prevZ = z

            x += xDir
            y += yDir
            z += zDir

            # Standard Deviation
            rGrid[row][col] = math.sqrt((x**2) + (y**2) + (z**2))
            r2Grid[row][col] = rGrid[row][col]**2

            sumR[row] += rGrid[row][col]
            sumR2[row] += r2Grid[row][col]

            row += 1
        col += 1
        row = 0

    # output
    row = 0
    col = 0

    fileName_R = './output/porosity/randWalk_3D_' + str(size) + '_st' + str(steps) + '_sa' + str(repeat) + '_por' + str(porosity) + '_R.dat'
    fileName_R2 = './output/porosity/randWalk_3D_' + str(size) + '_st' + str(steps) + '_sa' + str(repeat) + '_por' + str(porosity) + '_R2.dat'

    outFile_R = open(fileName_R, 'w')
    outFile_R2 = open(fileName_R2, 'w')

    # Print out walks
    while row < steps:
        outFile_R.write( "%6d" % ( row ) )
        outFile_R2.write( "%6d" % ( row ) )

        while col < repeat:
            outFile_R.write( "%6d" % ( rGrid[row][col] ) )
            outFile_R2.write( "%6d" % ( r2Grid[row][col] ) )
            col += 1

        avgR = ( sumR[row] / repeat )
        avgR2 = ( sumR2[row] / repeat )

        outFile_R.write( "%8.2f" % ( avgR ) )     # Average X
        outFile_R.write( "%8.2f" % ( avgR2 ) )  # Average X Squared
        outFile_R.write( "\n" )

        outFile_R2.write( "%8.2f" % ( avgR ) )     # Average Y
        outFile_R2.write( "%8.2f" % ( avgR2 ) )  # Average Y Squared
        outFile_R2.write( "\n" )

        col = 0
        row += 1

    outFile_R.close()
    outFile_R2.close()
#### END OF 3D

#
# selfAvoidingRandomWalk
#
def selfAvoidingRandomWalk( steps, repeat, size ):
    row = 0
    col = 0
    stepGridX = []
    stepGridY = []
    sumX = []
    sumY = []

    sumOfThisRunX = []
    sumOfThisRunY = []

    centerOfMassX = []
    centerOfMassY = []

    runStop = []

    rgx = []
    rgy = []
    rg = []

    grid = create2DGrid( size )

    # Initialize Grid
    for i in range( steps ):
        stepGridX.append([])
        stepGridY.append([])
        sumX.append(0)
        sumY.append(0)
        #r.append([])
        for j in range( repeat ):
            stepGridX[i].append(0)
            stepGridY[i].append(0)
            sumOfThisRunX.append(0)
            sumOfThisRunY.append(0)
            centerOfMassX.append(0)
            centerOfMassY.append(0)
            runStop.append(0)
            rgx.append(0)
            rgy.append(0)
            rg.append(0)

    numSuccess = 0

    while col < repeat:
        x = 0
        y = 0

        xDir = 0
        yDir = 0

        prevX = 0
        prevY = 0

        numSteps = 0

        while row < steps:
            direction = random.randint(1, 4)

            xDir = nnX2D( direction )
            yDir = nnY2D( direction )

            while (x + xDir == prevX) and (y + yDir == prevY):
                direction = random.randint(1, 4)

                xDir = nnX2D( direction )
                yDir = nnY2D( direction )

            prevX = x
            prevY = y

            x += xDir
            y += yDir

            stepGridX[row][col] = x
            stepGridY[row][col] = y

            sumX[row] += x
            sumY[row] += y

            if ( grid[x][y] == 2 ):
                numSteps = row
                runStop[col] = row
                break
            else:
                grid[x][y] = 2

            row += 1
        if row == steps:
            numSteps = steps
            runStop[col] = row - 1
            numSuccess += 1
        
        col += 1
        row = 0

    # Radius of Gyration
    row = 0
    col = 0

    # Center of Mass
    while col < repeat:
        while row <= runStop[col]:
            sumOfThisRunX[col] += stepGridX[row][col]
            sumOfThisRunY[col] += stepGridY[row][col]

            row += 1
        col += 1
        row = 0

    col = 0
    row = 0

    # Calculating Rg
    while col < repeat:
        centerOfMassX[col] = sumOfThisRunX[col] / steps
        centerOfMassY[col] = sumOfThisRunY[col] / steps

        sumOfDistanceX = 0
        sumOfDistanceY = 0
        while row <= runStop[col]:
            sumOfDistanceX += math.pow(stepGridX[row][col] - centerOfMassX[col], 2)
            sumOfDistanceY += math.pow(stepGridY[row][col] - centerOfMassY[col], 2)

            row += 1

        tSteps = runStop[col]

        if tSteps == 0:
            tSteps = 1

        rgx[col] = math.sqrt(sumOfDistanceX) / tSteps
        rgy[col] = math.sqrt(sumOfDistanceY) / tSteps

        rg[col] = math.sqrt( math.pow(rgx[col], 2) + math.pow(rgy[col], 2) )

        col += 1
        row = 0

    col = 0
    row = 0


    # output
    row = 0
    col = 0

    fileName_X = './output/avoiding/randWalk_2D_' + str(size) + '_st' + str(steps) + '_sa' + str(repeat) + '_X.dat'
    fileName_Y = './output/avoiding/randWalk_2D_' + str(size) + '_st' + str(steps) + '_sa' + str(repeat) + '_Y.dat'
    fileName_Success = './output/avoiding/randWalk_2D_' + str(size) + '_st' + str(steps) + '_sa' + str(repeat) + '_Success.dat'

    fileName_Rg = './output/avoiding/randWalk_2D_' + str(size) + '_st' + str(steps) + '_sa' + str(repeat) + '_Rg.dat'

    outFile_X = open(fileName_X, 'w')
    outFile_Y = open(fileName_Y, 'w')

    # Print out walks
    while row < steps:
        outFile_X.write( "%6d" % ( row ) )
        outFile_Y.write( "%6d" % ( row ) )

        while col < repeat:
            outFile_X.write( "%6d" % ( stepGridX[row][col] ) )
            outFile_Y.write( "%6d" % ( stepGridY[row][col] ) )
            col += 1

        avgX = ( sumX[row] / repeat )
        avgY = ( sumY[row] / repeat )

        outFile_X.write( "%8.2f" % ( avgX ) )     # Average X
        outFile_X.write( "%8.2f" % ( avgX**2 ) )  # Average X Squared
        outFile_X.write( "\n" )

        outFile_Y.write( "%8.2f" % ( avgY ) )     # Average Y
        outFile_Y.write( "%8.2f" % ( avgY**2 ) )  # Average Y Squared
        outFile_Y.write( "\n" )

        col = 0
        row += 1

    outFile_X.close()
    outFile_Y.close()

    outFile_success = open(fileName_Success, 'w')
    outFile_success.write("%8.2f\n" % (numSuccess / repeat))
    outFile_success.close()

    # Print Radius of Gyration
    row = 0
    col = 0

    outfile_Rg = open(fileName_Rg, 'w')

    while col < repeat:
        outfile_Rg.write( "%6d" % ( col ) )
        outfile_Rg.write( "%8.2f" % ( rgx[col] ) ) 
        outfile_Rg.write( "%8.2f" % ( rgy[col] ) ) 
        outfile_Rg.write( "%8.2f" % ( rg[col] ) ) 
        outfile_Rg.write( "\n" )

        col += 1

    outfile_Rg.close()
#### END OF 2D

