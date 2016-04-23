from environment import Building
from plants import Plant
from people import Person
from materials import Resources

class Agriculture(Building):

    def __init__(self, location: list = None, plant: Plant = None, worker: Person = None):
        """

        :param plant: Plant

        :return:
        """
        self.plant = plant
        self.amount = 0
        self.capacity = 1000
        self.building_time = 20 #CONSTANT
        self.worker = worker
        self.resources = Resources(3000, 11000)
        self.location = location
        self.type = 'Agriculture'
    def is_built(self):
        return self.building_time <= 0

    def collect(self):
        #  TODO
        if self.is_built() and self.worker:
            return self.amount
        return -1

    def time_pass(self, time: int = 1):

        if self.is_built():
            if self.plant and self.worker:
                self.amount += 100
                self.plant.update_growth()
        self.building_time -= 1

    def is_empty(self):
        return not self.plant

    def is_full(self):
        if self.plant:
            return self.plant.is_full

    def __repr__(self):
        pass
    

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

        self.building_time -= 1

    def collect(self):

        return self.amount
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
                     'It is currently under construction and will take {} weeks to finish'.format(self.building_time)
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