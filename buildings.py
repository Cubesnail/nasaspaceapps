from environment import Environment
from plants import Plant
from people import Person


class Agriculture(Environment):

    def __init__(self, cost: int, plant: Plant = None, worker: Person = None):
        """

        :param plant: Plant
        :param cost:
        :return:
        """
        self.plant = plant
        self.amount = 0
        self.capacity = 10
        self.cost = cost
        self.building_time = 20 #CONSTANT
        self.worker = worker

    def is_built(self):
        return self.building_time <= 0

    def collect(self):
        #  TODO
        if self.is_built() and self.worker:
            return self.plant
        return -1

    def time_pass(self, time: int = 1):

        if self.is_built():
            if self.plant and self.worker:
                self.plant.update_growth()
        self.building_time -= 1

    def is_empty(self):
        return not self.plant

    def is_full(self):
        if self.plant:
            return self.plant.is_full

    def __repr__(self):
        pass


class MedicalCentre(Environment):

    def __init__(self, cost: int, worker: Person = None):
        self.capacity = 10 #CONSTANT
        self.building_time = 20 #CONSTANT
        self.persons = []
        self.worker = worker

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


class CommandCentre(Environment):

    def __init__(self, cost: int, worker: Person = None):
        self.building_time = 30 #CONSTANT
        self.worker = worker

    def is_built(self):
        return self.building_time <=0

    def time_pass(self):
        self.building_time -= 1


class Mine(Environment):

    def __init__(self, cost: int, worker: Person = None):
        self.building_time = 10 #CONSTANT
        self.worker = worker
        self.resources = {}
        self.capacity = 30 #CONSTANT
    def is_built(self):
        return self.building_time <= 0

    def time_pass(self):
        #  TODO
        if not self.is_built():
            self.building_time -= 1
            return

    def collect(self):
        #  TODO
        pass
    def is_empty(self):
        return self.resources == {}

    def is_full(self):
        resource = 0
        for key, value in self.resources.items():
             resource += value
        if resource >= self.capacity:
            return True
        return False


class Lab(Environment):

    def __init__(self, cost: int, worker: Person = None, research = None, research_time = 0):
        self.building_time = 15 #CONSTANT
        self.worker = worker
        self.research = research
        self.research_time = research_time

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