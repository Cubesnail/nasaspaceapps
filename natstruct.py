# NATURAL STRUCTURES

from environment import NatStruct
import math
import random

# resource list structure
# resources[ [Nat] [Nat] ... [Nat] ]
# resource order: Al, Fe, Si


class Crater(NatStruct):
    def __init__(self, isExplored):
        self.isBuildable = False
        self.isExplored = isExplored
        self.hasResources = False
        self.type = 'Crater'
    def __str__(self):
        return 'A hole in the ground. But kind of not a hole.'


class Cave(NatStruct):
    def __init__(self, isExplored):
        self.isBuildable = False
        self.isExplored = isExplored
        self.resources = {}
        self.hasResources = False
        self.type = 'Cave'

        # arbitrary random chance generation shit

        randint = random.randrange(0, 100)
        if randint >= 20:
            self.hasResources = True
            amtAl = random.randrange(0, 100) * 10
            amtFe = random.randrange(0, 100) * 10
            amtSi = random.randrange(0, 100) * 10

            self.resources["Al"] = amtAl
            self.resources["Fe"] = amtFe
            self.resources["Si"] = amtSi
    def __str__(self):
        return 'Its a cave. It might have something. It might not'

class Ground(NatStruct):
    def __init__(self, isExplored):
        self.isBuildable = True
        self.isExplored = False
        self.resources = {}
        self.hasResources = False
        self.type = 'Ground'
    def __str__(self):
        return 'Its ground.'