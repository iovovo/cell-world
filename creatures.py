from world import *
from variables import *

class Creature(object):

    def __init__(self, creatureType, strength, agility, intelligence, position):
        """ Base creature class. Three types to start: wolf eats deer. Deer eats bush. Bush eats sun.
        base stats are strength, agility, intelligence. These three make up the other stats as in:
        hp (health points) = Str * 8
        stamina = str * 4
        initiative = agi / 2
        movement = 1 + agi / 5
        sight = 1 + int / 3
        damage = str / 2 + agi / 3

        if stamina => maxStamina * 0.7: health += 1
        if stamina < maxStamina * 0.3: health -= 1
        if stamina < maxStamina * 0.1: health -= 2

        eating restores stamina.

        if health & stamina > maxStamina & maxHealth, birth.
        """
        self.level = 0
        self.experience = 0.0
        self.experienceRatio = 1.05
        self.levelRatio = 1.06   ##int(2 ** (1.06 * x)
        # self.position = position
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

        self.maxHealth = 10 + strength *  5
        self.health = self.maxHealth
        self.maxStamina = 4 + strength * 4
        self.stamina = self.maxStamina
        self.initiative = 1 + agility/2
        self.movement = 1 + agility/5
        self.sight = 1 + intelligence/3
        self.damage = strength/2 + agility/3

        def eat(self, food):
            self.Stamina += food.Stamina
            if self.Stamina > self.maxStamina:  self.Stamina = self.maxStamina
            

        """def poi(sight, position):
                                    nRange = zip(xrange(-sight, sight+1), xrange(0, 2*sight+1))
                                    surround = [[[-1,-1] for y in xrange(0, 2*sight+1) ] for x in xrange(0, 2*sight+1)]
                                    for y in nRange:
                                        if (position[0]+y[0] >= 0) and (position[0]+y[0] < s):
                                            for x in nRange:
                                                if (position[1]+x[0] >= 0) and (position[1]+x[0] < s):
                                                    surround[y[1]][x[1]] = list(field[position[0]+y[0]][position[1]+x[0]][1].position)
                                    return surround"""

"""if self.type == 3: # Wolf
    self.color = [0.451, 0.49, 0.518]
    Creature.wolves += 1
    self.ID = [self.type, self.wolves]
elif self.type == 2: # deer
    self.color = [0.75, 0.50, 0.218]
    Creature.deers += 1
    self.ID = [self.type, self.deers]
elif self.type == 1: # bush
    self.color = [0.15, 0.70, 0.15]
    Creature.bushes += 1
    self.ID = [self.type, self.bushes]
elif self.type == 0:
    self.color = [ 0, 0, 0 ]"""

class Wolf(Creature):
    color = [0.451, 0.49, 0.518]
    edible = "Deer"

class Deer(Creature):
    color = [0.75, 0.50, 0.218]
    edible = "Bush"

class Bush(Creature):
    color = [0.15, 0.70, 0.15]
    edible = "Sun"


        

"""
    def __init__(self, creatType, position):
        self.ageLimit = 40 #( (4-creatType) * 4 )
        self.birthLimit = 1
        self.age = 0
        self.birthCount = 0
        self.mStats = parentMStats
        # poner comprobaciones de age y births para ver si puede o no puede seguir teniendo children o si ya es demasiado viejo
        mBaseStats = numpy.random.normal(1.005, 0.01, 4)
        for x in range(4):
            self.mStats[x] *= mBaseStats[x]
        self.ID = [0,0]
        self.type = creatType
        self.edible = abs(creatType -1)
        self.initiative = self.mStats[0]*self.bStats[creatType][0]
        self.essence = self.mStats[1]*self.bStats[creatType][1]
        self.hp = self.essence
        self.sight = self.mStats[2]*self.bStats[creatType][2]
        self.move = self.mStats[3]*self.bStats[creatType][3]
        self.position = position
        if self.type == 3: # Wolf
            self.color = [1-1/self.initiative**2,1/self.move**0.5,1/self.essence**0.5]
            Creature.wolves += 1
            self.ID = [self.type, self.wolves]
            self.birthLimit = 2
        elif self.type == 2: # deer
            self.color = [1/self.initiative**0.5,1/self.essence**0.5,1-1/self.move**2]
            Creature.deers += 1
            self.ID = [self.type, self.deers]
            self.birthLimit = 1
        elif self.type == 1: # bush
            self.color = [1/self.essence**0.5, 1-1/self.essence**0.5, 1/self.essence**0.5]
            Creature.bushes += 1
            self.ID = [self.type, self.bushes]
            self.birthLimit = 10
        elif self.type == 0:
            self.color = [ 0, 0, 0 ]

    def moves(self, fPos):
        global field, newField
        newField[ fPos[0] ][ fPos[1] ] = copy.deepcopy(field[ self.position[0] ][ self.position[1] ])
        newField[ fPos[0] ][ fPos[1] ][1].position = [ fPos[0], fPos[1] ]
        field[self.position[0]][self.position[1]][1].dies()
        newField[self.position[0]][self.position[1]][1].dies()
    def eat(self, food):
        global field, newField
        # when mutations are added, check if carnivorous before type so meat eating plants can eat properly
        if self.type == 1:
            self.hp += 2
        elif self.type == 2:
            self.hp += (food.hp / 10)
            self.moves( food.position )
        elif self.type == 3:
            self.hp += food.hp / 4
            self.moves( food.position )
        if self.hp > self.essence:
            self.hp = self.essence
    def dies(self):

    def poi(self):
        sght = int(self.sight)
        nRange = zip(xrange(-sght, sght+1), xrange(0, 2*sght+1))
        nField = [[[-1,-1] for y in xrange(0, 2*sght+1) ] for x in xrange(0, 2*sght+1)]
        for y in nRange:
            if (self.position[0]+y[0] >= 0) and (self.position[0]+y[0] < s):
                for x in nRange:
                    if (self.position[1]+x[0] >= 0) and (self.position[1]+x[0] < s):
                        nField[y[1]][x[1]] = list(field[self.position[0]+y[0]][self.position[1]+x[0]][1].position)
        return nField
"""
