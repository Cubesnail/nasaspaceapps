# PLANTS

class Plant:
    # __init__: self, Str, Num, Num, Int, Int, Int
    def __init__(self, name, rog, numGrow):
        self.name = name
        # self.mass = mass
        self.rog = rog
        # semi-arbitrary constant
        # units: percent growth per week

        # self.area = area  # occupied area at full growth
        self.numHarvest = 0 
        self.numGrow = numGrow
        self.percentGrow = 0
        self.numEatable = 0

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

    def harvest(self):
        self.numEatable = self.numHarvest
        self.numHarvest = 0


    def is_full(self):
        return self.numHarvest == 100

    def get_num_eat(self):
        return self.numEatable

