from environment import Building
from plants import Plant
from people import Person
from materials import Resources
from food import Food

class Agriculture(Building):

    def __init__(self, location: list = None, plant: Plant = None, worker: Person = None):
        """

        :param plant: Plant

        :return:
        """
        self.plants = []
        #self.amount = 0
        self.capacity = 1000
        self.building_time = 20 #CONSTANT
        self.worker = worker
        self.resources = Resources(3000, 11000)
        self.location = location
        self.type = 'Agriculture'
        self.food = Food()
    def plant_plant(self, plantname, numGrow):
        if someplant.lower() == "rice":
            self.food.rice.isGrow = True
            self.food.rice.numGrow = numGrow

        if someplant.lower() == "wheat":
            self.food.wheat.isGrow = True
            self.food.wheat.numGrow = numGrow

        if someplant.lower() == "onion":
            self.food.onion.isGrow = True
            self.food.onion.numGrow = numGrow

        if someplant.lower() == "radish":
            self.food.radish.isGrow = True
            self.food.radish.numGrow = numGrow


    def is_built(self):
        return self.building_time <= 0

    def harvestall(self):
        self.rice.harvest()
        self.wheat.harvest()
        self.onion.harvest()
        self.radish.harvest()


    def collect(self):
        temp = Food()
        temp.totalfood += self.wheat.numEatable
        temp.totalfood += self.rice.numEatable
        temp.totalfood += self.onion.numEatable
        temp.totalfood += self.radish.numEatable

        self.wheat.numEatable = 0
        self.rice.numEatable = 0
        self.onion.numEatable = 0
        self.radish.numEatable = 0

        return temp


    def time_pass(self, time: int = 1):

        if self.is_built():
            if self.worker:
                #self.amount += 100
                #self.plant.update_growth()
                for plt in self.plants:
                    plt.update_growth()
                    
        self.building_time -= 1

    def is_empty(self):
        return not self.plant

    def is_full(self):
        if self.plant:
            return self.plant.is_full

    def __repr__(self):
        pass

    def __str__(self):
        if self.worker:
            worker = "worker: " + self.worker.name  + "\n"
        else:
            worker = "worker: " + "none" + "\n"
        builtness = "built: " + str(self.is_built()) + "\n"

        rice = "Rice: \n" + \
                "grow? " + str(self.food.rice.isGrow) + "harvestable: " + str(self.food.rice.numHarvest) + \
                "growth percent: " + str(self.food.rice.percentGrow) + "\n"
        wheat = "Wheat: \n" + \
                "grow? " + str(self.food.wheat.isGrow) + "harvestable: " + str(self.food.wheat.numHarvest) + \
                "growth percent: " + str(self.food.wheat.percentGrow) + "\n"
        onion = "Onion: \n" + \
                "grow? " + str(self.food.onion.isGrow) + "harvestable: " + str(self.food.onion.numHarvest) + \
                "growth percent: " + str(self.food.onion.percentGrow) + "\n"
        radish = "Radish: " + \
                "grow? " + str(self.food.radish.isGrow) + "harvestable: " + str(self.food.radish.numHarvest) + \
                "growth percent: " + str(self.food.radish.percentGrow) + "\n"
        return builtness + worker + rice + wheat + onion + radish

class MedicalCentre(Building):

    def __init__(self, location: list= None, worker: Person = None):
        self.location = location
        self.capacity = 10 #CONSTANT
        self.building_time = 20 #CONSTANT
        self.persons = []
        self.worker = worker
        self.amount = Resources()
        self.resources = Resources(3000, 9000, 2000)
        self.type = 'Medical Centre'

    def is_built(self):
        return self.building_time <= 0

    def time_pass(self):
        if not self.is_built():
            self.building_time -= 1
            return
        for person in self.persons:
            person.health += round(10/len(self.persons) + 0.5)
            if person.health >= 10:
                person.job = None
                self.persons.remove(person)

    def is_full(self):
        return len(self.persons) == self.capacity

    def __str__(self):
        result = 'Your medical centre at {}, {}'.format(self.location[0], self.location[1]) + '\n'
        if not self.is_built():
            result = result + \
                'This medical centre is under construction and will take {} weeks to finish'.format(self.building_time)
        if self.worker:
            result = result + '{} is working here.'
        else:
            result = result + 'This medical centre currently has no workers and is not functional.'
        return result

class CommandCentre(Building):

    def __init__(self, location: list= None, worker: Person = None):
        self.building_time = 30 #CONSTANT
        self.worker = worker
        self.location = location
        self.type = 'Agriculture'
        self.resources = Resources(4000, 10000, 1000) 
    def is_built(self):
        return self.building_time <=0

    def time_pass(self):
        self.building_time -= 1

    def __str__(self):
        result = 'Your command centre at {}, {}:'.format(self.location[0], self.location[1])
        if not self.is_built():
            result = result + \
                     '\nIs currently under construction and will be finished in {} weeks.'.format(self.building_time)
        if self.worker:
            result = result + '\nWorker: {}'.format(self.worker.name)
        else:
            result = result + '\nHas no worker and is currently nonfunctional'
        return result


class Mine(Building):

    def __init__(self, location= None, worker: Person = None):
        self.building_time = 10 #CONSTANT
        self.location = location
        self.worker = worker
        self.amount = Resources()
        self.capacity = 30 #CONSTANT
        self.amount = Resources()
        self.type = 'Agriculture'
        self.resources = Resources(0, 12000) 
    def is_built(self):
        return self.building_time <= 0

    def time_pass(self):
        #  TODO
        if self.is_built() and self.worker:
            self.amount.Al += 1000
            self.amount.Fe += 1000
            self.amount.Si += 1000

        elif not self.is_built():
            self.building_time -= 1

    def collect(self):
        temp = Resources()
        temp, self.amount = self.amount, temp
        return temp

    def is_empty(self):
        return self.amount == {}

    def is_full(self):
        resource = 0
        for key, value in self.resources.items():
             resource += value
        if resource >= self.capacity:
            return True
        return False

    def __str__(self):
        result = 'Location {}, {}'.format(self.location[0],self.location[1]) + ' currently has ' + \
                 str(self.amount) + '\n'
        if self.worker:
            result = result + 'Worker: {}'.format(self.worker)
        else:
            result = result + 'No worker.'
        if not self.is_built():
            result = result + \
                     'It is currently under construction and will take {} weeks to finish\n'.format(self.building_time)
        return result


class Lab(Building):

    def __init__(self, location= None, worker: Person = None, research = None, research_time = 0):
        self.building_time = 15 #CONSTANT
        self.location = location
        self.worker = worker
        self.research = research
        self.research_time = research_time
        self.type = 'Lab'
        self.resources = Resources(5000, 9000, 4000) 
    def is_built(self):
        return self.building_time <= 0

    def time_pass(self):
        if not self.is_built():
            self.building_time -= 1
            return
        if self.worker:
            self.research_time -= 1

    def time_left(self):
        if self.research_time:
            return self.research_time

    def __str__(self):
        #  TODO
        pass
