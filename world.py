from variables import *
from terrains import *
from creatures import *
import random

class World(object):
	map = [ [ [Terrain(0), None] for y in range(size)] for x in range(size) ]

	def getCreature(self, y, x):
		return self.map[y][x][1]

	def setCreature(self, y, x, creaturePointer):
		self.map[y][x][1] = creaturePointer

	def getTerrain(self, y, x):
		return self.map[y][x][0]

def sparkles(world):
	for i in range(numberOfCreatures[0]):
		y, x = random.randint(0,size-1), random.randint(0,size-1)
		actionOrder.append(Wolf(rollDice(6), rollDice(4), rollDice(5), [y,x]))
		world.setCreature( y, x, actionOrder[-1])
	for i in range(numberOfCreatures[1]):
		y, x = random.randint(0,size-1), random.randint(0,size-1)
		actionOrder.append(Deer(rollDice(4), rollDice(6), rollDice(5), [y,x]))
		world.setCreature( y, x, actionOrder[-1])
	for i in range(numberOfCreatures[2]):
		y, x = random.randint(0,size-1), random.randint(0,size-1)
		# y, x = 0, 0
		actionOrder.append(Bush(rollDice(10), rollDice(0), rollDice(0), [y,x]))
		world.setCreature( y, x, actionOrder[-1])

def sortActionOrder(actionOder):
	actionOrder.sort(key=getKey, reverse=True)

#function to get the key value of initiative to sort the creatures action order.
def getKey(creature):
    return creature.initiative

world = World()
actionOrder = []
sparkles(world)
