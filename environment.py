class Building:

    def time_pass(self):
        raise NotImplementedError

    def is_built(self):
        raise NotImplementedError

class NatStruct:

    def is_buildable(self):
        return self.buildable

    def is_explored(self):
        return self.explored

    def has_resources(self):
        return self.has_resources



class Environment:
    pass
