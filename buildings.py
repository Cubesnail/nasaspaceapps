from environment import Environment
from Materials import Plant
class Agriculture(Environment):

    def __init__(self, cost: int, plant: Plant = None, worker: Person = None):
        """

        :param type: Plant
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
        if self.is_built():
            return self.amount
        return -1

    def time_pass(self, time: int = 1):
        self.building_time -= 1
        #  TODO
        pass

    def is_empty(self):
        return self.amount == 0

    def is_full(self):
        return self.amount == self.capacity

    def __repr__(self):
        pass

class MedicalCentre(Environment):

    def __init__(self, cost: int, worker: Person = None):
        self.capacity = 10 #CONSTANT
        self.building_time = 20 #CONSTANT
        self.persons = {}
        self.worker = worker

    def is_built(self):
        return self.building_time <= 0

    def time_pass(self):
        #  TODO
        pass

    def is_full(self):
        return len(self.persons) == self.capacity

class CommandCentre(Environment):

    def __init__(self, cost: int, worker: Person = None):
        self.building_time = 30 #CONSTANT
        self.worker = worker

    def is_built(self):
        return self.building_time <=0

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
        pass

    def collect(self):
        #  TODO

    def is_empty(self):
        return self.resources == {}

    def is_full(self):
        resource = 0
        for key, value in self.resources.items():
             resource += value
        if resource >= self.capacity:
            return True
        return False

class Lab(Environment)