# PLANTS

class Plant:
    # __init__: self, Str, Num, Num, Int, Int, Int
    def __init__(self, name, rog, area, numHarvest, numGrow):
        self.name = name
        self.mass = mass
        self.rog = rog
        # semi-arbitrary constant
        # units: percent growth per week

        self.area = area  # occupied area at full growth
        self.numHarvest = numHarvest
        self.numGrow = numGrow
        self.percentGrow = percentGrow

    # update_growth: self -> void
    # effects: modifies self.percentGrow, self.numHarvest, self.numGrow

    def update_growth(self):
        # assume each call to update_growth() updates per time unit of
        # rog
        if self.numGrow != 0:
            self.percentGrow += rog
            if self.percentGrow >= 100:
                self.numHarvest += self.numGrow
                self.numGrow = 0
                self.percentGrow = 0

    # harvest: self -> Int
    # harvest returns the number of plants for harvest, sets value to 0
    #	after return.
    def harvest(self):
        temp = self.numHarvest
        self.numHarvest = 0
        return temp
