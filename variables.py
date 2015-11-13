import random

visualMode = True
maxGeneration = 50
generationCount = 0

size=16
border=0.5
squareSize=[size,size]

crawler = [-1,0,1]
delay = 0.0
window = 0                                             # glut window number
width, height = 400, 400                               # window size
multW, multH = width/size, height/size

pause = 0
numberOfCreatures = [size/2, size, size*2]
# numberOfCreatures = [1,1,1]

def rollDice(sides):
    if sides <= 1:
        return 1
    else:
        return random.randint(1, sides)

def printStats(creature):
    print creature.__class__.__name__, creature.position,"HP", creature.health, "/", creature.maxHealth, ", Sta", creature.stamina, "/", creature.maxStamina, "Str, Agi, Int:", creature.strength, creature.agility, creature.intelligence, "Sight", creature.sight
