#!BPY
"""
Name: 'Random Walk'
Blender: 261
Group: 'Add'
Tooltip: 'Performs a random walk in a scene.'
"""
#
# Assignment 1 - Random Walk
# PHY 710
# Author: Andrew Maxwell
# Due: February 23, 2012
#

#
# Usage: python random_walk.py <number of steps> <output file name>
# Ex: python random_walk.py 10 output.txt
#
# Blender References:
#   Example from http://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro/Advanced_Tutorials/Python_Scripting/Export_scripts
#   http://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro/Advanced_Tutorials/Python_Scripting/Introduction_New
#


import sys
import randLib

#=========================
# Main
#=========================

argc = len(sys.argv)

steps = 0
fileName = "C:/Users/student/Desktop/output.txt"
fileName2 = "C:/Users/student/Desktop/prob.txt"
fileName3 = "C:/Users/student/Desktop/r.txt"

if argc == 3:
	steps = int(sys.argv[1])
	fileName = sys.argv[2]
elif argc == 1:
	steps = 5
else:
	disp( "%s\n" % ( "Usage: python random_walk.py <number of steps> <output file name>" ) )
	sys.exit()

print("10 Steps")
randLib.selfAvoidingRandomWalk( 100, 1000, 100 )

#print("100 Steps")
#randLib.simpleRandomWalk4D( 100, 10 )
#print("2/5")
#randLib.simpleRandomWalk4D( 100, 100 )
#print("3/5")
#randLib.simpleRandomWalk4D( 100, 1000 )
#print("4/5")
#randLib.simpleRandomWalk4D( 100, 10000 )
#print("5/5")
#randLib.simpleRandomWalk4D( 100, 100000 )

# Open an output file.
#outFile = open(fileName, 'w')
#probFile = open(fileName2, 'w')
#rFile = open(fileName3, 'w')
#outFile.truncate()

# Grab the selected object from the scene.
#obj = bpy.context.object

#scn = bpy.context.scene
#scn.objects.unlink(obj)

#bpy.ops.mesh.primitive_uv_sphere_add()

#obj = bpy.context.object
#p = create3DGrid( 0, 20 )

#simpleRandomWalk( obj, steps, 10 )
#nonReversalRandomWalk( cube, steps )
#selfAvoidingRandomWalk( obj, p, steps )
#prevTime = int(datetime.datetime.now().second)

#while steps > 0:
#	if (int(datetime.datetime.now().second) - prevTime) > 0:
#randomWalkInMedia( obj, p, 100 )
#		prevTime = int(datetime.datetime.now().second)
#		steps -= 1

#outFile.close()
#probFile.close()
#rFile.close()
