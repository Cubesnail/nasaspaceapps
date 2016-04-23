from map import Map
from people import Person
from commands import Command
from buildings import *
import os # currently for OS-dependent clearing


class Sim:
    def __init__(self,size: list):
        self.people = []
        self.people.append(Person('John','20*52','45','M'))
        self.people.append(Person('Josh','20*52','45','M'))
        self.people.append(Person('Jacob','20*52','45','M'))
        self.people.append(Person('Jessica','20*52','45','F'))
        self.people.append(Person('Jane','20*52','45','F'))
        self.people.append(Person('Jackyln','20*52','45','F'))
        self.materials = {'Al':100000, 'Si': 100000, 'Ti': 100000, 'Fe': 100000, 'Acrylic': 100000, 'H20': 1000000,
                     'O2': 1000000}
        self.plants = {}
        self.map = Map(size[0],size[1]) #CONSTANT
        self.map.initialize()
        self.victory = False

    def get_person(self, name): #name is str
        for pplz in self.people:
            if pplz.name == name:
                return pplz
    def person_exist(self,name):
        for pplz in self.people:
            if pplz.name == name:
                return True

    def display_summary(self):
        pass

    def pass_time(self):
        for column in self.map.screen:
            for row in column:
                row.time_pass()


class Build(Command):
    def __init__(self, building, location, simulation):
        self.location, self.building, self.simulation = location, building, simulation

    def do(self):
        if self.building.resources <= self.simulation.resources:
            self.simulation.map[self.location[0],self.location[1]] = self.building


class Destroy(Command):
    def __init__(self, location, simulation):
        self.location, self.simulation = location, simulation

    def do(self):
        self.simulation.resources += self.simulation.map[self.location[0],self.location[1]].resources
        self.simulation.map[self.location[0],self.location[1]] = None


class Collect(Command):
    #  TODO
    def __init__(self,location,simulation):
        self.location,self.simulation = location, simulation
    def do(self):
        if type(self.simulation.map[self.location[0],self.location[1]]) in ['Mine', 'Agriculture']:
            self.simulation.map[self.location[0],self.location[1]].collect()


class SendWorker(Command):
    #  TODO
    def __init__(self, worker, location, game):
        self.location = location
        self.worker = worker
        self.simulation = game
    def do(self):
        #  TODO
        self.simulation(self.location).persons.append(self.worker)

class Research(Command):
    #  TODO
    def __init__(self, product, location):
        self.location = location
        self.product = product

    def do(self):
        #  TODO
        pass

class Explore(Command):

    # TODO: implement explore with a worker
    #       remove worker from prev location, add to curr location

    def __init__(self, worker, location, game):
        self.location = location
        self.worker = worker
        if type(game.get_environment(location)) == NatStruct:
            game.get_environment(location).isExplored = True


game = Sim([10,10])

turn_end = False

def help_commands():
    print("-----Help text------")
    print("syntax: COMMAND (STRUCTURE) (WORKER) LOCATION_X LOCATION_Y")
    print("commands: build, destroy, help, collect, send, explore, cancel")
    print("structures (buildings): CommandCentre, MedicalCentre, Agriculture, Mine, Lab")
    print("example syntax:")
    print("-- build STRUCTURE LOC_X LOC_Y")
    print("-- destroy LOC_X LOC_Y")
    print("-- help")
    print("-- send WORKER LOC_X LOC_Y")

def parse(user_input):
    command_list = user_input.split()
    # syntax: command || location || 
    # example: build mine 1 2
    # -> builds mine at location 1,2
    if command_list[0].upper() == 'build'.upper():
        print(command_list[1].upper())
        if command_list[1].upper() in ['MINE','LAB','COMMANDCENTRE','MEDICALCENTRE','AGRICULTURE']: #  TODO
            if int(command_list[2]) < game.map.height and int(command_list[3]) < game.map.width:
                if command_list[1].upper() == 'MINE':
                    return Build(Mine(),[command_list[2],command_list[3]],game)
                elif command_list[1].upper() == 'LAB':
                    return Build(Lab(), [command_list[2], command_list[3]], game)
                elif command_list[1].upper() == 'COMMANDCENTRE':
                    return Build(CommandCentre(), [command_list[3], command_list[4]], game)
                elif command_list[1].upper() == 'MEDICALCENTRE':
                    return Build(MedicalCentre(), [command_list[3], command_list[4]], game)
                elif command_list[1].upper90 == 'AGRICULTURE':
                    return Build(Agriculture(), [command_list[3], command_list[4]], game)
                else:
                    print('Error: Invalid Command, Please try again.')
            else:
                print('Error: invalid location')
        else:
            print('Error: invalid structure')
    elif command_list[0].upper() == 'destroy'.upper():
        if command_list[1].isdigit() and command_list[2].isdigit() and command_list[1] <= game.map.height and \
            command_list[2] <= game.map.width:
            return Destroy(command_list[1],command_list[2])
    elif command_list[0].upper() == 'help'.upper():
        help_commands()
    elif command_list[0].upper() == 'collect'.upper():
        if command_list[1] < game.map.height and command_list[2] < game.map.width:
            return Collect([command_list[1], command_list[2]], game)
    elif command_list[0].upper() == 'send'.upper():
        # if command_list[1] in game.people[]
        if command_list[1] < game.map.height and command_list[2] < game.map.width:
            work = game.people[command_list[1]]
            return Send(game.get_person(command_list[1]), [command_list[2], command_list[3], game])
    elif command_list[0].upper() == 'explore'.upper():
        if command_list[2] < game.map.width and command_list[3] < game.map.width:
            return Explore(game.get_person(command_list[1]), [command_list[2], command_list[3]],game)
    elif command_list[0].upper() == 'cancel'.upper():
        pass
    elif command_list[0].upper() == 'EXIT':
        pass
    else:
        print('Error: Invalid Command, Please try again.')
"""
while not game.victory:
    while not turn_end:
        command_queue = []
        print(game.map)
        print('What would you like to do?')
        command = input('\nEnter action: ')
        parsed_command = parse(command)
        if command == 'Exit':
            turn_end = True
        if parsed_command:
            command_queue.append(parsed_command)
    if not game.victory:
        skip_time = input('\nHow long would you like to skip time for: ')
        while not skip_time.isdigit():
            print('Invalid input, please only enter an integer.')
            skip_time = input('\nHow long would you like to skip time for: ')
        skip_time = int(skip_time)
        for x in range(skip_time):
            game.pass_time()
    turn_end = False
"""

# game loop
while not game.victory:
    # change: removed command queue
    # motivation behind change: if user wants to build on same place twice,
    #   queue does not recognize error until queue is finalized.

    #_=os.system("cls") # windows
    #_=os.system("clear") # linux / unix derivatives

    os.system("cls" if os.name == 'nt' else 'clear')
    while not turn_end:

        print(game.map)
        command = input("Enter a command: ")
        #_=os.system("clear") # linux / unix
        #_=os.system("cls") # windows
        os.system("cls" if os.name == 'nt' else 'clear')
        if command.upper() == "EXIT":
            turn_end = True
        else:
            parse(command)


    if not game.victory:
        # time skipping function
        skip_time = input('\nHow long would you like to skip time for: ')
        while not skip_time.isdigit():
            print('Invalid input, please only enter an integer.')
            skip_time = input('\nHow long would you like to skip time for: ')
        skip_time = int(skip_time)
        for x in range(skip_time):
            game.pass_time()
    turn_end = False


