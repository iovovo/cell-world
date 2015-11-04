import random

size=16
border=0.5
squareSize=[size,size]
alive=1
dead=0

crawler = [-1,0,1]
delay = 0.3
window = 0                                             # glut window number
width, height = 400, 400                               # window size
multW, multH = width/size, height/size

pause = 0
numberOfCreatures = [0, 0, 1]

def rollDice(sides):
    if sides <= 1:
        return 1
    else:
        return random.randint(1, sides)
