from buildings import *
from natstruct import *


class Map:
    """Map class. Stores the game map.

    """
    def __init__(self, width, height):
        """Instantiate a Map object

        :param width:
        :param height:
        :return:
        """
        self.width = width
        self.height = height
        self.objects = []
        self.screen = []

    def initialize(self):
        """Initialize the map object.

        :rtype: None
        """
        self.screen = []

        for k in range(self.height):
            temp = []
            for x in range(self.width):
                temp.append(Ground(False))
            self.screen.append(temp)

        area = self.width * self.height
        #  Generate the terrain on the map.
        numstruct = int(0.2 * area)
        numcrater = random.randint(1, numstruct)
        numcave = numstruct - numcrater

        #  Place the generated structures.
        for k in range (0, numcrater):
            rx = random.randint(1, self.width - 1)
            ry = random.randint(1, self.height - 1)
            self.screen[rx][ry] = Crater(False)
        for k in range (0, numcave):
            rx = random.randint(1, self.width - 1)
            ry = random.randint(1, self.height - 1)
            self.screen[rx][ry] = Cave(False)

    def get_environment(self, location):
        return self.screen[location[0], location[1]]

    def __str__(self):
        """Return a user-readable string representation of the Map object.

        :rtype: str
        """

        result = ''
        for x in range(self.width+2):
            result = result + '-'
        result = result + '\n'

        for column in self.screen:
            result = result + '|'
            #  Set symbols for each of the buildings or terrain of the map.
            for row in column:
                if type(row) is Agriculture:
                    result = result + 'A'
                elif type(row) is MedicalCentre:
                    result = result + '+'
                elif type(row) is CommandCentre:
                    result = result + '*'
                elif type(row) is Mine:
                    result = result + 'M'
                elif type(row) is Lab:
                    result = result + 'L'
                elif type(row) is Crater:
                    result = result + 'V'
                elif type(row) is Cave:
                    result = result + '^'
                elif type(row) is str:
                    result = result + row
                elif type(row) is Ground:
                    result = result + 'O'
            result = result + '|'
            result = result + '\n'
        for x in range(self.width+2):
            result = result + '-'
        result = result + '\n'
        return result
