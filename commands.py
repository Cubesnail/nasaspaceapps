from sim import Sim
from environment import *
from buildings import *
from materials import Resources
from location import Location

class Command:
    def do(self):
        raise NotImplementedError

class Info(Command):
    def __init__(self, building, location, simulation):
        self.location, self.building, self.simulation = location, building, simulation

    def do(self):
        #  TODO
        pass

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
        if self.simulation.map.screen[self.location[0]][self.location[1]] == 'Mine':
            temp = self.simulation.map.screen[self.location[0]][self.location[1]].collect()
            if temp == Resources():
                print('No resources were collected.')
            game.resources += temp

        if self.simulation.map.screen[self.location[0]][self.location[1]] == 'Agriculture':

            temp = self.simulation.map.screen[self.location[0], self.location[1]].harvestall()
            temp = self.simulation.map.screen[self.location[0], self.location[1]].collect()
            game.Food += temp
            game.resources.food = game.Food.totalfood


class SendWorker(Command):
    def __init__(self, worker, location, simulation):
        self.location = location
        self.worker = worker
        self.simulation = simulation

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


def build_parse():
    pass


def mine_parse():
    pass


def destroy_parse():
    pass


def collect_parse():
    pass


def explore_parse():
    pass


def grow_parse():
    pass


def exit_parse():
    pass


def info_parse():
    pass


'''
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
                elif command_list[1].upper() == 'AGRICULTURE':
                    return Build(Agriculture(), [int(command_list[2]), int(command_list[3])], game)
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
    elif command_list[0].upper() == "GROW":
        game.map.screen[int(command_list[2])][int(command_list[3])].plant_plant(command_list[1], 20)
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

'''