#  SIMULATOR
#  main program
from buildings import *
import os # used for: clear, 
import random
from natstruct import *

class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []
        self.screen = []
    def initialize(self):

        # initialzie graphical array
        # graphical array: position index start at 1 (border is 0)
        self.screen = []

        # create top border
        temp = []
        for k in range(0, self.width+2):
            temp.append("-")
        self.screen.append(temp)

        for k in range(0, self.height):
            temp = ["|"]
            for x in range(0, self.width):
                temp.append(None)
            temp.append("|")
            #  temp.append('\n')
            self.screen.append(temp)

        # create bottom border
        temp = []
        for k in range(0, self.width+2):
            temp.append("-")
        self.screen.append(temp)


        # insert random natstruct

        area = self.width * self.height
        # approximately 20% of terrian is natstruct
        numstruct = int(0.2 * area)
        numcrater = random.randint(1, numstruct)
        numcave = numstruct - numcrater

        for k in range (0, numcrater):
            rx = random.randint(1, self.width)
            ry = random.randint(1, self.height)
            self.screen[rx][ry] = Crater(False)
        for k in range (0, numcave):
            rx = random.randint(1, self.width)
            ry = random.randint(1, self.height)
            self.screen[rx][ry] = Cave(False)

    def display(self):
        # TODO
        for k in range (0, self.height+2):
            for x in range(0, self.width+2):
                print(self.screen[k][x], end = '')
            print()

    def __str__(self):
        result = ''
        for column in self.screen:
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
                else:
                    result = result + 'O'
            result = result + '\n'
        return result

    def update(self):
        # update
        pass


graphic = Map(10, 10)

graphic.initialize()
print(graphic)
