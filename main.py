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
			glColor3f(world.map[y][x][0].color[0], world.map[y][x][0].color[1], world.map[y][x][0].color[2])
			draw_rect(x*multW, y*multH, multW, multH)
			if world.map[y][x][1] != None:
				glColor3f(world.map[y][x][1].color[0], world.map[y][x][1].color[1], world.map[y][x][1].color[2])
				draw_rect(x*multW+border, y*multH+border, multW-2*border, multH-2*border)



def roam():
	actionOrder.sort(key=getKey, reverse=True)
	y = actionOrder[0].surroundings(world)
	print y
	for rows in range(len(y)):
		print y[rows]

	print actionOrder[0].initiative
	#print map(lambda x: [x.initiative, x.__class__.__name__], actionOrder)


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
	# newCount = [Creature.bushes, Creature.deers, Creature.wolves]
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
	glLoadIdentity()                                   # reset position
	refresh2d(width, height)                           # set mode to 2d
	###
	global pause
	if pause == 0:
		roam()
		pause = 1

	# roam()
	printField()


	###
	glutSwapBuffers()                                  # important for double buffering

glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)               	# set window size
glutInitWindowPosition(0, 0)                       	# set window position
window = glutCreateWindow("Cell World")          	# create window with title
glutDisplayFunc(draw)                              	# set draw function callback
glutIdleFunc(draw)                                     	# draw all the time
glutMainLoop()                                         	# start everything
