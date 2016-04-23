# COMMANDS


# building in dictionary
# current resources in dictionary

class Command:
    def do(self):
        raise NotImplementedError

    def cancel(self):
        raise NotImplementedError


class Build(Command):
    #  TODO
    def __init__(self, building, location):
        self.location = location
    def do(self):
        #  TODO
        pass

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

