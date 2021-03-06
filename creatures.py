from world import *
from variables import *

class Creature(object):

    def __init__(self, strength, agility, intelligence, position):
        """ Base creature class. Three types to start: wolf eats deer. Deer eats bush. Bush eats sun.               Base stats are strength, agility, intelligence. These three make up the other stats as in:
        hp (health points) = Str * 8                stamina = str * 4                 initiative = agi / 2                  movement = 1 + agi / 5                  sight = 1 + int / 3                     damage = str / 2 + agi / 3
        if stamina => maxStamina * 0.7: health += 1             if stamina < maxStamina * 0.3: health -= 1          if stamina < maxStamina * 0.1: health -= 2
        eating restores stamina.
        if health & stamina > maxStamina & maxHealth, birth."""
        self.level = 0
        self.experience = 0.0
        self.experienceRatio = 1.05
        self.levelRatio = 1.06   ##int(2 ** (1.06 * x)
        self.position = position
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

    def die(self):
        pass

    def move(self, position, world):
        world.setCreature(self.position[0], self.position[1], None)
        self.position = position
        world.setCreature(position[0], position[1], self)

    def eat(self, food, world):
        self.stamina += food.stamina
        if self.stamina > self.maxStamina:  self.stamina = self.maxStamina
        self.move(food.position, world)

    def surroundings(self):
        yRange = range(self.position[0]-self.sight, self.position[0]+self.sight+1)
        xRange = range(self.position[1]-self.sight, self.position[1]+self.sight+1)
        return [[ [y, x] if ( (y >= 0) and (y < size) and (x >= 0) and (x < size) ) else [-1,-1] for y in yRange ] for x in xRange]

    def findFood(self, world):
        preys = []
        surround = self.surroundings()
        if self.sight > self.movement:
            searchRange = len(surround) - (self.sight + self.movement)
        else:
            searchRange = len(surround)
        for y in range(searchRange):
            for x in range(searchRange):
                if (surround[y][x] != [-1,-1]) and (world.getCreature(surround[y][x][0], surround[y][x][1]).__class__.__name__ == self.edible):
                    preys.append(surround[y][x])
        if len(preys) != 0:
            return preys[random.randint(0,len(preys)-1)]
        else:
            return None

    def attack(self, target):
        target.health -= self.damage
        if target.health <= 0:
            self.eat(target)

    def passiveActions(self):
        if (self.stamina >= self.maxStamina * 0.5) and (self.health != self.maxHealth):
            self.health += 1
            if self.stamina > self.maxStamina:  self.stamina = self.maxStamina
            if self.health > self.maxHealth:  self.health = self.maxHealth
        elif self.stamina <= self.maxStamina * 0.25:
            self.health -= 1
        if self.health <= 0:
            self.die()


    def chooseAction(self, world, actionOrder):
        if self.stamina <= 0.7*self.maxStamina:
            self.stamina -= 2
            target = self.findFood(world)
            if target != None:
                self.eat(world.getCreature(target[0], target[1]), world)
        else:
            self.stamina -= 2





class Wolf(Creature):
    color = [0.451, 0.49, 0.518]
    edible = "Deer"

class Deer(Creature):
    color = [0.75, 0.50, 0.218]
    edible = "Bush"

class Bush(Creature):
    color = [0.15, 0.70, 0.15]
    edible = "Sun"

    def reproduce(self, world, actionOrder):
        emptySpots = []
        surround = self.surroundings()
        for y in range(len(surround)):
            for x in range(len(surround)):
                if surround[y][x] != [-1,-1]:
                    creature = world.getCreature(surround[y][x][0], surround[y][x][1])
                    if creature == None:
                        emptySpots.append(surround[y][x])
        if len(emptySpots) != 0:
            birthSpot = emptySpots[random.randint(0,len(emptySpots)-1)]
            self.stamina = self.stamina / 3
            self.health = self.health / 3
            actionOrder.append(Bush(rollDice(10), rollDice(0), rollDice(0), birthSpot))
            actionOrder[-1].health -= actionOrder[-1].health*0.7
            actionOrder[-1].stamina -= actionOrder[-1].stamina*0.7
            world.setCreature( birthSpot[0], birthSpot[1], actionOrder[-1])

    def chooseAction(self, world, actionOrder):
        if self.stamina != self.maxStamina:
            self.eat()
        elif self.stamina == self.maxStamina and self.health == self.maxHealth:
            self.reproduce(world, actionOrder)
            self.stamina -= 2
            pass

    def eat(self):
        self.stamina += 1
