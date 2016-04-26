
class Command:
    def do(self):
        raise NotImplementedError

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
