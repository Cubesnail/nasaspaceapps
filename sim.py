from map import Map
from people import Person
from commands import Command

class sim:
    def __init__(self,size: list):
        self.people = []
        self.people.append(Person('John','20','45','M'))
        self.people.append(Person('Josh','20','45','M'))
        self.people.append(Person('Jacob','20','45','M'))
        self.people.append(Person('Jessica','20','45','F'))
        self.people.append(Person('Jane','20','45','F'))
        self.people.append(Person('Jackyln','20','45','F'))
        self.materials = {'Al':100000, 'Si': 100000, 'Ti': 100000, 'Fe': 100000, 'Acrylic': 100000, 'H20': 1000000,
                     'O2': 1000000}
        self.plants = {}
        self.map = Map(size[0],size[1]) #CONSTANT
        self.victory = False

    def display_summary(self):
        pass


def parse(user_input):
    command_list = user_input.split()

    if command_list[0].upper() == 'build'.upper():
        if command_list[1].upper is in ['buildings'] #  TODO
            pass
    elif command_list[0].upper() == 'destroy'.upper():
        pass
    elif command_list[0].upper() == 'help'.upper():
        pass
    elif command_list[0].upper() == 'collect'.upper():
        pass
    elif command_list[0].upper() == 'send'.upper():
        pass
    elif command_list[0].upper() == 'explore'.upper():
        pass
    elif command_list[0].upper() == 'cancel'.upper():
        pass
    else:
        print('Error: Invalid Command, Please try again.')


class Build(Command):
    def __init__(self, building, location, grid):
        self.location = location
        self.grid = grid
        self.building = building

    def do(self):

class Destroy(Command):
    #  TODO
    def __init__(self, location):
        self.location = location
    def do(self):
        #  TODO
        pass

class Collect(Command):
    #  TODO
    def __init__(self,location):
        self.location = location
    def do(self):
        #  TODO
        pass

class SendWorker(Command):
    #  TODO
    def __init__(self, worker, location):
        self.location = location
        self.worker = worker

    def do(self):
        #  TODO
        pass

class Research(Command):
    #  TODO
    def __init__(self, product, location):
        self.location = location
        self.product = product

    def do(self):
        #  TODO
        pass


game = sim([10,10])

turn_end = False

while not game.victory:
    while not turn_end:
        command_queue = []
        print(game.map)
        print('What would you like to do?')
        command = input('\nEnter action:')
        parsed_command = parse(command)
        if command == 'Exit':
            turn_end = True
        if parsed_command:
            command_queue.append(parsed_command)