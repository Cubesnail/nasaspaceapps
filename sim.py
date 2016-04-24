from map import Map
from people import Person
from commands import Command
from buildings import *
from random import randrange
import os  # currently for OS-dependent clearing


class Sim:
    def __init__(self, size: list):
        self.people = []
        self.people.append(Person('John', 20 * 52, '45', 'M'))
        self.people.append(Person('Josh', 20 * 52, '45', 'M'))
        self.people.append(Person('Jacob', 20 * 52, '45', 'M'))
        self.people.append(Person('Jessica', 20 * 52, '45', 'F'))
        self.people.append(Person('Jane', 20 * 52, '45', 'F'))
        self.people.append(Person('Jackyln', 20 * 52, '45', 'F'))
        self.resources = Resources(100000, 100000, 100000, 100000, 100000, 100000, 100000)
        self.plants = {}
        self.map = Map(size[0], size[1])  # CONSTANT
        self.map.initialize()
        self.victory = False
        self.buildings = []
        self.ded = []
        self.food = Food()
    def get_person(self, name):  # name is str
        for pplz in self.people:
            if pplz.name == name:
                return pplz

    def person_exist(self, name):
        for pplz in self.people:
            if pplz.name == name:
                return True

    def display_summary(self):
        pass

    def pass_time(self):
        for building in self.buildings:
            building.time_pass()
        self.resources.food -= len(self.people) * 10
        self.resources.H2O -= len(self.people) * 20
        for people in self.people:
            health(people)


def health(worker: Person):
    if worker.location:
        if game.map.screen[worker.location[0]][worker.location[1]].type == 'MedicalCentre':
            return
    if worker.sex == 'M':
        pronouns = ['he', 'him', 'his']
    else:
        pronouns = ['she', 'her', 'her']
    fatal = '{} has tripped over {} shoelace and has been fatally injured.'.format(worker.name, pronouns[2])
    non_fatal = '{} was injured in a work-related issue.'.format(worker.name)
    injury = randrange(0,1000)
    if injury == 0:
        worker.health -= 150
        print(fatal)
    elif injury < 50:
        worker.health -= 10
        print(non_fatal)
    else:
        if worker.health != 100:
            worker.health += 1
    if game.resources.food <= 0:
        worker.health -= 5
    if game.resources.H2O <= 10:
        worker.health -= 10
    if worker.health <= -100:
        print('{} has unfortunately died in a minor fender bender.'.format(worker.name))
        dead(worker)

def dead(worker: Person):
    if worker.location:
        game.map.screen[worker.location[0]][worker.location[1]] = None
    game.people.remove(worker)
    game.ded.append(worker)
    if len(game.people) == 0:
        print('Good job. You killed everyone. Game Over.')
        quit()
class Build(Command):
    def __init__(self, building, location, simulation):
        self.location, self.building, self.simulation = location, building, simulation

    def do(self):
        if self.building.resources < self.simulation.resources:
            self.simulation.map.screen[self.location[0]][self.location[1]] = self.building
            self.simulation.resources -= self.building.resources
            self.simulation.buildings.append(self.building)
            self.building.location = self.location

        else:
            print('Not enough resources.')


class Destroy(Command):
    def __init__(self, location, simulation):
        self.location, self.simulation = location, simulation

    def do(self):
        self.simulation.resources += self.simulation.map[self.location[0], self.location[1]].resources
        self.simulation.map[self.location[0], self.location[1]] = None


class Collect(Command):
    def __init__(self, location, simulation):
        self.location, self.simulation = location, simulation

    def do(self):
        if type(self.simulation.map.screen[self.location[0], self.location[1]]) == Mine:
            temp = self.simulation.map.screen[self.location[0]][self.location[1]].collect()
            if temp == Resources():
                print('No resources were collected.')
            game.resources += temp

        if type(self.simulation.map.screen[self.location[0], self.location[1]]) == Agriculture:

            temp = self.simulation.map.screen[self.location[0], self.location[1]].harvest()
            temp = self.simulation.map.screen[self.location[0], self.location[1]].collect()
            game.Food += temp



class SendWorker(Command):
    def __init__(self, worker, location, sim):
        self.location = location
        self.worker = worker
        self.simulation = sim

    def do(self):
        if self.worker.location:
            self.simulation.map.screen[self.worker.location[0]][self.worker.location[1]].worker = None
        if self.simulation.map.screen[self.location[0]][self.location[1]].worker:
            temp = self.simulation.map.screen[self.location[0]][self.location[1]].worker.location
            self.simulation.map.screen[temp[0]][temp[1]].worker = None
            self.simulation.map.screen[self.location[0]][self.location[1]].worker.location = None
        self.simulation.map.screen[self.location[0]][self.location[1]].worker = self.worker
        self.worker.location = self.location


class Research(Command):
    #  TODO
    def __i88init__(self, product, location):
        self.location = location
        self.product = product

    def do(self):
        #  TODO
        pass


class Explore(Command):
    # TODO: implement explore with a worker
    #       remove worker from prev location, add to curr location

    def __init__(self, worker, location, sim):
        self.location = location
        self.worker = worker
        if type(sim.get_environment(location)) == NatStruct:
            sim.get_environment(location).isExplored = True

    def do(self):
        pass


class Nothing(Command):
    def __init__(self):
        pass

    def do(self):
        pass


game = Sim([10, 10])

turn_end = False


def help_commands():
    print("-----Help text------")
    print("syntax: COMMAND (STRUCTURE) (WORKER) LOCATION_X LOCATION_Y")
    print("commands: build, destroy, help, collect, send, explore, cancel, info")
    print("structures (buildings): CommandCentre, MedicalCentre, Agriculture, Mine, Lab")
    print("example syntax:")
    print("-- build STRUCTURE LOC_X LOC_Y")
    print("-- destroy LOC_X LOC_Y")
    print("-- help")
    print("-- send WORKER LOC_X LOC_Y")
    print("-- info WORKER/LOC_X LOC_Y")


def parse(user_input):
    """ Takes a user input and parses it and returns a command.
    """
    command_list = user_input.split()
    # syntax: command || location || 
    # example: build mine 1 2
    # -> builds mine at location 1,2
    if command_list[0].upper() == 'build'.upper():
        print(command_list[1].upper())
        if command_list[1].upper() in ['MINE', 'LAB', 'COMMANDCENTRE', 'MEDICALCENTRE', 'AGRICULTURE']:  # TODO
            if int(command_list[2]) < game.map.height and int(command_list[3]) < game.map.width:
                if command_list[1].upper() == 'MINE':
                    return Build(Mine(), [int(command_list[2]), int(command_list[3])], game)
                elif command_list[1].upper() == 'LAB':
                    return Build(Lab(), [command_list[2], command_list[3]], game)
                elif command_list[1].upper() == 'COMMANDCENTRE':
                    return Build(CommandCentre(), [int(command_list[2]), int(command_list[3])], game)
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
            return Destroy(command_list[1], command_list[2])
    elif command_list[0].upper() == 'help'.upper():
        help_commands()
    elif command_list[0].upper() == 'collect'.upper():
        if int(command_list[1]) < game.map.height and int(command_list[2]) < game.map.width:
            return Collect([int(command_list[1]), int(command_list[2])], game)
    elif command_list[0].upper() == 'send'.upper():
        # if command_list[1] in game.people[]
        if int(command_list[2]) < game.map.height and int(command_list[3]) < game.map.width:
            #  work = game.people[command_list[1]]
            return SendWorker(game.get_person(command_list[1]), [int(command_list[2]), int(command_list[3])], game)
    elif command_list[0].upper() == 'explore'.upper():
        if command_list[2] < game.map.width and command_list[3] < game.map.width:
            return Explore(game.get_person(command_list[1]), [command_list[2], command_list[3]], game)
    elif command_list[0].upper() == 'cancel'.upper():
        pass
    elif command_list[0].upper() == 'EXIT':
        pass
    elif command_list[0].upper() == 'INFO':
        if command_list[1].isdigit():
            print(game.map.screen[int(command_list[1])][int(command_list[2])])
        else:
            print(game.get_person(command_list[1]))
    else:
        print('Error: Invalid Command, Please try again.')
    return Nothing()


# game loop
while not game.victory:
    # change: removed command queue
    # motivation behind change: if user wants to build on same place twice,
    #   queue does not recognize error until queue is finalized.

    # _=os.system("cls") # windows
    # _=os.system("clear") # linux / unix derivatives

    os.system("cls" if os.name == 'nt' else 'clear')
    while not turn_end:
        print(game.resources)
        print(game.map)
        command = input("Enter a command: ")
        # _=os.system("clear") # linux / unix
        # _=os.system("cls") # windows
        os.system("cls" if os.name == 'nt' else 'clear')
        if command.upper() == "EXIT":
            turn_end = True
        else:
            parse(command).do()

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
