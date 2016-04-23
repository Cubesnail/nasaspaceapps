from map import Map
from people import Person
from commands import Command
from buildings import *
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
        self.victory = False

    def display_summary(self):
        pass

    def pass_time(self):
        for column in map.screen:
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


game = Sim([10,10])

turn_end = False


def parse(user_input):
    command_list = user_input.split()

    if command_list[0].upper() == 'build'.upper():
        if command_list[1].upper in ['MINE','LAB','COMMANDCENTRE','MEDICALCENTRE','AGRICULTURE']: #  TODO
            if command_list[3] < game.map.height and command_list[4] < game.map.width:
                if command_list[1].upper == 'MINE':
                    return Build(Mine(),[command_list[3],command_list[4]],game)
    elif command_list[0].upper() == 'destroy'.upper():
        if command_list[1].isdigit() and command_list[2].isdigit() and command_list[1] <= game.map.height and \
            command_list[2] <= game.map.width:
            return Destroy(command_list[1],command_list[2])
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