# MATERIALS


class Material:
    """Currently unused class

    """

    def __init__(self, name, mass, cost, density):
        """

        :param name:
        :param mass:
        :param cost:
        :param density:
        :return:
        """
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
        """Initialize a list of resources and the amounts.

        :param Al: int
        :param Fe: int
        :param Si: int
        :param acrylic: int
        :param H2O: int
        :param O2: int
        :param food: int
        :rtype: None
        """
        self.Al, self.Fe, self.Si, self.acrylic, self.H2O, self.O2, self.food = \
            Al, Fe, Si, acrylic, H2O, O2, food

    def __lt__(self, other):
        """Return true if self is less than other and false otherwise

        :param other:
        :rtype: bool
        """
        return self.Al <= other.Al and \
               self.Fe <= other.Fe and \
               self.Si <= other.Si and \
               self.acrylic <= other.acrylic and \
               self.H2O <= other.H2O and \
               self.O2 <= other.O2 and \
               self.food <= other.food

    def __eq__(self, other):
        """Return true if other is equal to self and false otherwise.

        :param other:
        :rtype: bool
        """
        return self.Al == other.Al and \
               self.Fe == other.Fe and \
               self.Si == other.Si and \
               self.acrylic == other.acrylic and \
               self.H2O == other.H2O and \
               self.O2 == other.O2 and \
               self.food == other.food

    def __gt__(self, other):
        """Return true if other is greater than self and false otherwise

        :param other:
        :rtype: bool
        """
        return other < self

    def __str__(self):
        """Return a user-readable string representation of the resources object.

        :rtype: str
        """
        result = 'Al: {}kg \nFe: {}kg \nSi: {}kg \nAcrylic: {}kg \nH2O: {}kg \nO2: {}kg \nFood: {}kg'.format(
            self.Al, self.Fe, self.Si, self.acrylic, self.H2O, self.O2, self.food
        )
        return result

    def __isub__(self, other):
        """Subtract the other resource from self and return the resulting resources object.

        :param other:
        :rtype: Resources
        """
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
        """Add the other resource object to self and return the resulting resources object.

        :param other:
        :rtype: Resources
        """
        result = self
        result.Al += other.Al
        result.Fe += other.Fe
        result.Si += other.Si
        result.acrylic += other.acrylic
        result.H2O += other.H2O
        result.O2 += other.O2
        result.food += other.food
        return result

