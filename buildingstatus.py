# graphically display building information

from buildings import *
import os
from map import *


class buildingstatus:
    def __init__(self, game):
        self.simulation = game

    def display(self):
        chosen = False
        exitspecific = False
        # building overview

        while not chosen:
            print("List of current buildings:")
            for b in self.simulation.buildings:
                print(str(b) + '. ' + type(b))

            print("")
 
            userin = input("Enter the building number to view stats: ")
            if userin.isdigit():
                os.system('cls' if os.name == 'nt' else 'clear')
                chosen = True
            elif userin.upper == "EXIT":
                # to do
                pass
            else:
                print("that's not a valid input!")
        while not exitspecific:
            print("building info:")


            print("Complete: " + ("yes" if self.simulation.buildings.is_built() else str(self.simulation.buildings[userin].building_time) + " weeks left."))


            print("Worker:" + ("none" if self.simulation.buildings[userin] == None else self.simulation.buildings[userin].name))

