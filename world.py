from variables import *
from terrains import *
from creatures import *
import random

#random.randint(0,2)
worldMap = [ [ [Terrain(0), Wolf(5, 5, 5)] for y in range(size)] for x in range(size) ]
actionOrder = []
