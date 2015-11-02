from variables import *
from terrains import *
from creatures import *
import random

#random.randint(0,2)
worldMap = [ [ [Terrain(0), Creature(3, 5, 5, 5, [y,x])] for y in range(size)] for x in range(size) ]
actionOrder = []
