from variables import *
from terrains import *
from creatures import *
import random

#random.randint(0,2)
worldMap = [ [ [Terrain(0)] for y in range(size)] for x in range(size) ]
actionOrder = []

def sparkles(world):
	for i in range(size/3):
		y = random.randint(0,size-1)
		x = random.randint(0,size-1)
		actionOrder.append(Wolf(5, 5, 5, [y,x]))
		world[y][x].append(actionOrder[-1])
	for i in range(size):
		y = random.randint(0,size-1)
		x = random.randint(0,size-1)
		actionOrder.append(Deer(5, 5, 5, [y,x]))
		world[y][x].append(actionOrder[-1])
	for i in range(size*2):
		y = random.randint(0,size-1)
		x = random.randint(0,size-1)
		actionOrder.append(Bush(5, 5, 5, [y,x]))
		world[y][x].append(actionOrder[-1])


sparkles(worldMap)