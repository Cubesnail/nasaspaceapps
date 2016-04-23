# NATURAL STRUCTURES

from environment import NatStruct
import math
import random

# resource list structure
# resources[ [Nat] [Nat] ... [Nat] ]
# resource order: Al, Fe, Si


class Crater:
    def __init__(self, isExplored):
        self.isBuildable = False
        self.isExplored = isExplored
        self.hasResources = False


class Cave:
    def __init__(self, isExplored):
        self.isBuildable = False
        self.isExplored = isExplored
        self.resources = {}
        self.hasResources = False

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

