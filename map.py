# SIMULATOR
# main program
from buildings import *
import os # used for: clear, 

class map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []
        self.screen = []
    def initialize(self):
        # TODO

        # O: open
        # B: base
        # 
        
        # initialzie graphical array
        # graphical array: position index start at 1 (border is 0)
        self.screen = []

        # create top border
        temp = []
        for k in range(0, self.width+2):
            temp.append("-")
        temp.append("\n")
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

    def display (self):
        # TODO
        
        for k in range (0, self.height+2):
            for x in range(0, self.width+2):
                print(self.screen[k][x], end = '')
            print()
    def update (self):
        # update
        pass


graphic = map(5, 5)

graphic.initialize()
graphic.display()
