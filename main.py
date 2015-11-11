import subprocess
import time
import random
import copy
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from variables import *
from terrains import *
from world import *
from creatures import *

def printField():
	for y in xrange(size):
		for x in xrange(size):
			# glColor3f(world.map[y][x][0].color[0], world.map[y][x][0].color[1], world.map[y][x][0].color[2])
			# draw_rect(x*multW, y*multH, multW, multH)
			if world.getCreature(y,x) != None:
				glColor3f(world.map[y][x][1].color[0], world.map[y][x][1].color[1], world.map[y][x][1].color[2])
				draw_rect(x*multW+border, y*multH+border, multW-2*border, multH-2*border)

def roam():
	sortActionOrder(actionOrder)
	for turn in range(len(actionOrder)):
		actionOrder[turn].chooseAction(world, actionOrder)
		actionOrder[turn].passiveActions()
		# printStats(actionOrder[turn])



def refresh2d(width, height):
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
	glMatrixMode (GL_MODELVIEW)
	glLoadIdentity()

def draw_rect(x, y, width, height):
	glBegin(GL_QUADS)                                  # start drawing a rectangle
	glVertex2f(x, y)                                   # bottom left point
	glVertex2f(x + width, y)                           # bottom right point
	glVertex2f(x + width, y + height)                  # top right point
	glVertex2f(x, y + height)                          # top left point
	glEnd()                                            # done drawing a rectangle

def draw():                                            # ondraw is called all the time
	global generationCount
	# newCount = [Creature.bushes, Creature.deers, Creature.wolves]
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
	glLoadIdentity()                                   # reset position
	refresh2d(width, height)                           # set mode to 2d
	###

	time.sleep(delay)
	roam()
	printField()
	generationCount += 1
	print generationCount
	if generationCount >= maxGeneration:
		time.sleep(5)
		exit()

	###
	glutSwapBuffers()                                  # important for double buffering

def screen():
	glutInit()                                             # initialize glut
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	glutInitWindowSize(width, height)               	# set window size
	glutInitWindowPosition(0, 0)                       	# set window position
	window = glutCreateWindow("Cell World")          	# create window with title
	glutDisplayFunc(draw)                              	# set draw function callback
	glutIdleFunc(draw)                                     	# draw all the time
	glutMainLoop()                                         	# start everything

def main(visualMode):
	i = 0
	if visualMode == True:
		screen()
	elif visualMode == False:
		while i <= maxGeneration:
			roam()
			i += 1
		else:
			print map(lambda x: printStats(x), actionOrder)

main(visualMode)
