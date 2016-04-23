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
        #  temp = []
        # for k in range(0, self.width+2):
        #     temp.append("-")
        #  self.screen.append(temp)

        for k in range(self.height):
            # temp = ["|"]
            temp = []
            for x in range(self.width):
                temp.append(Ground(False))
            # temp.append("|")
            #  temp.append('\n')
            self.screen.append(temp)

        # create bottom border
        # temp = []
        # for k in range(0, self.width+2):
        #     temp.append("-")
        # self.screen.append(temp)


        # insert random natstruct

        area = self.width * self.height
        # approximately 20% of terrian is natstruct
        numstruct = int(0.2 * area)
        numcrater = random.randint(1, numstruct)
        numcave = numstruct - numcrater

        for k in range (0, numcrater):
            rx = random.randint(1, self.width - 1)
            ry = random.randint(1, self.height - 1)
            self.screen[rx][ry] = Crater(False)
        for k in range (0, numcave):
            rx = random.randint(1, self.width - 1)
            ry = random.randint(1, self.height - 1)
            self.screen[rx][ry] = Cave(False)

    def display(self):
        # TODO
        for k in range (0, self.height+2):
            for x in range(0, self.width+2):
                print(self.screen[k][x], end = '')
            print()

    def get_environment(self, location):
        return self.screen[location[0], location[1]]

    def __str__(self):
        result = ''
        for x in range(self.width+2):
            result = result + '-'
        result = result + '\n'
        for column in self.screen:
            result = result + '|'
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

    def update(self):
        # update
        pass



