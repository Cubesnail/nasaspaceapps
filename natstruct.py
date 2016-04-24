# NATURAL STRUCTURES

from environment import NatStruct
import random


class Crater(NatStruct):
    """Crater class: No resources, Unable to build on top of.

    """
    def __init__(self, isExplored):
        """Initialize the crater class.

        :param isExplored:
        :rtype: None
        """

        self.isBuildable = False
        self.isExplored = isExplored
        self.hasResources = False
        self.type = 'Crater'

    def __str__(self):
        """Returns a user-readable string of the Crater object.

        :rtype: str
        """
        return 'A hole in the ground. But kind of not a hole.'


class Cave(NatStruct):
    """Cave class: Chance of resources, Able to build on top of.

    """
    def __init__(self, isExplored):
        """Initialize the cave object.

        :param isExplored:
        :rtype: None
        """
        self.isBuildable = True
        self.isExplored = isExplored
        self.resources = {}
        self.hasResources = False
        self.type = 'Cave'

        #  Generate materials
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
        """Return a user-readable string of the cave object.

        :rtype: str
        """
        return 'Its a cave. It might have something. It might not'


class Ground(NatStruct):
    """Ground class: No resources, able to build on top of.

    """
    def __init__(self, isExplored):
        """Initialize the ground class

        :param isExplored:
        :rtype: None
        """
        self.isBuildable = True
        self.isExplored = False
        self.resources = {}
        self.hasResources = False
        self.type = 'Ground'

    def __str__(self):
        """Return a user-readable string of the ground object.

        :rtype: str
        """
        return 'Its ground.'