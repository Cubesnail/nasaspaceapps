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

class Wheat(Food):

    def __init__(self):
        self.carbohydrates = 0
        self.fat = 0
        self.fibre = 0
        self.protein = 0
        self.calories = 0

    pass
class Rice(Food):
    def __init__(self):
        self.carbohydrates = 0
        self.fat = 0
        self.fibre = 0
        self.protein = 0
        self.calories = 0
class Onion(Food):
    def __init__(self):
        self.carbohydrates = 0
        self.fat = 0
        self.fibre = 0
        self.protein = 0
        self.calories = 0
class Radish(Food):
    def __init__(self):
        self.carbohydrates = 0
        self.fat = 0
        self.fibre = 0
        self.protein = 0
        self.calories = 0