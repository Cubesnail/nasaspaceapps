# MATERIALS


class Material:
    # __init__ : self, Str, Num, Num, Num

    def __init__(self, name, mass, cost, density):
        self.name = name
        self.mass = mass
        self.cost = cost
        self.density = density

    def get_volume(self):
        return self.mass / self.density

    def __eq__(self, other):
        return self.name == other.name and self.mass == other.mass

    def __lt__(self, other):
        return self.mass < other.mass
