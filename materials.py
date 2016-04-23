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


class Resources:
    def __init__(self, Al=0, Fe=0, Si=0, acrylic=0, H2O=0, O2=0, food=0):
        self.Al, self.Fe, self.Si, self.acrylic, self.H2O, self.O2, self.food = \
            Al, Fe, Si, acrylic, H2O, O2, food

    # __lt__: Resources Resources
    def __lt__(self, other):
        return self.Al <= other.Al and \
               self.Fe <= other.Fe and \
               self.Si <= other.Si and \
               self.acrylic <= other.acrylic and \
               self.H2O <= other.H2O and \
               self.O2 <= other.O2 and \
               self.food <= other.food

    def __eq__(self, other):
        return self.Al == other.Al and \
               self.Fe == other.Fe and \
               self.Si == other.Si and \
               self.acrylic == other.acrylic and \
               self.H2O == other.H2O and \
               self.O2 == other.O2 and \
               self.food == other.food

    def __gt__(self, other):
        return other < self

    def __str__(self):
        result = 'Al: {}kg \nFe: {}kg \nSi: {}kg \nAcrylic: {}kg \nH2O: {}kg \nO2: {}kg \nFood: {}kg'.format(
            self.Al, self.Fe, self.Si, self.acrylic, self.H2O, self.O2, self.food
        )
        return result

    def __isub__(self, other):
        result = self
        result.Al -= other.Al
        result.Fe -= other.Fe
        result.Si -= other.Si
        result.acrylic -= other.acrylic
        result.H2O -= other.H2O
        result.O2 -= other.O2
        result.food -= other.food
        return result

    def __iadd__(self, other):
        result = self
        result.Al += other.Al
        result.Fe += other.Fe
        result.Si += other.Si
        result.acrylic += other.acrylic
        result.H2O += other.H2O
        result.O2 += other.O2
        result.food += other.food
        return result


