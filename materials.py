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

class Food:
    def __init__(self, ):
        self.wheat = Plant("Wheat", 20)
        self.rice = Plant("Rice", 20)
        self.onion = Plant("Onion", 15)
        self.radish = Plant("Radish", 15)
        self.totalfood = 0

    # __lt__: Food Food
    def __lt__(self, other):
        return self.wheat <= other.wheat and \
               self.rice <= other.rice and \
               self.onion <= other.onion and \
               self.radish <= other.radish and \
               self.totalfood <= other.totalfood
    def __eq__(self, other):
        return self.wheat == other.wheat and \
               self.rice == other.rice and \
               self.onion == other.onion and \
               self.radish == other.radish and \
               self.totalfood == other.totalfood
    def __gt__(self, other):
        return other < self

    def __str__(self):
        result = 'wheat: {}kg \nrice: {}kg \nonion: {}kg \nradish: {}kg \nTotal food: {}kg '.format(
            self.wheat.numinventory, self.rice.numinventory, self.onion.numinventory, self.radish.numinventory, self.totalfood )

        return result

    def __isub__(self, other):
        result = self
        result.wheat -= other.wheat
        result.rice -= other.rice
        result.onion -= other.onion
        result.radish -= other.radish
        result.totalfood -= other.totalfood
        return result

    def __iadd__(self, other):
        result = self
        result.wheat += other.wheat
        result.rice += other.rice
        result.onion += other.onion
        result.radish += other.radish
        result.totalfood += other.totalfood
        return result
