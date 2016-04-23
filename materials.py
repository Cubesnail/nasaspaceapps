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


class Resource:
    def __init__(self, Al=0, Fe=0, Si=0, acrylic=0, H2O=0, O2=0):
        self.Al, self.Fe, self.Si, self.acrylic, self.H2O, self.O2 = \
                Al, Fe, Si, acrylic, H2O, O2

    # __lt__: Resources Resources
    def __lt__(self, other):
        return self.Al <= other.Al and \
                self.Fe <= other.Fe and \
                self.Si <= other.Si and \
                self.acrylic <= other.acrylic and \
                self.H2O <= other.H2O and \
                self.O2 <= other.O2

    def __eq__(self, other):
        return self.Al == other.Al and \
                self.Fe == other.Fe and \
                self.Si == other.Si and \
                self.acrylic == other.acrylic and \
                self.H2O == other.H2O and \
                self.O2 == other.O2

