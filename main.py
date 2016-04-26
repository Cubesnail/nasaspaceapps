import os
from sim import Sim
from commands import *

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


intro_materials = {'Al':10000, 'Fe':100000, 'Si':1000000, 'Acrylic':100000, 'H2O':10000, 'Food':1000000 }

def intro_materials_parser(user_input):

    command_list = user_input.split()

    if command_list[0].lower() == 'add':
        intro_materials[command_list[1]] += int(command_list[2])
        return 0
    elif command_list[0].lower() == 'sub':
        intro_materials[command_list[1]] -= int(command_list[2])
        return 0
    elif command_list[0].lower() == 'h':
        print(msgcmds)
        garbage = input("press any key to continue: ")
        return 0

    elif command_list[0].lower() == 'done':
        print("done!")
        return 1

    else:
        print("invalid input")
        return -1



 # introductory loop

msg1 = "After many years of hard work, the human race is ready to launch its first manned mission to mars. However, the state of the earth is in ruins. These astronauts won't be coming back. Your job is to manage mission Cultivator. First, you must prove that colonization is possible with a two year test run before mission control sends additional earth-bound resources and people."

msg2 = "You have 3000kg of total allowed cargo. Materials that can be brought: Aluminum, Iron, Silicone, Acrylic, Food, and Water. Be aware that it will take 150 days to travel to mars. There are 6 people on board. Each person consumes, on average, 2kg of food and 1kg of water per day."

msgcmds = "Use the syntax 'COMMAND MATERIAL MASS' \n " +\
        "Commands: add, sub \n" + \
        "Materials: Al, Fe, Si, Acrylic, Food, H2O\n" + \
        "Type h to view this information again.\n"

def disp_init_mat(matdict):
    totalmass = 0
    for mat in matdict:
        print(str(mat) + ": " + str(matdict[mat]))
        totalmass += matdict[mat]
    print("total mass: " + str(totalmass))

materialschosen = False

print(msg1)
print(msg2)
print(msgcmds)
uin = input("press any key to continue ")
"""
while not materialschosen:

    os.system("cls" if os.name == 'nt' else 'clear')

    disp_init_mat(intro_materials)

    user_input = input("Enter a command: ")
    errcode = intro_materials_parser(user_input)

    if errcode==1:
        materialschosen == True
        break
"""

game.resources.Al = intro_materials["Al"]
game.resources.Fe = intro_materials["Fe"]
game.resources.Si = intro_materials["Si"]
game.resources.acrylic = intro_materials["Acrylic"]
game.resources.H2O = intro_materials["H2O"]

game.food.totalfood = intro_materials["Food"]
game.resources.food = game.food.totalfood

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
