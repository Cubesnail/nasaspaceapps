class Materials:
    def __init__(self,mass,volume):
        self.mass = mass

        self.volume = volume
    def get_volume(self):
        return mass * volume
aluminum = Materials(1,2)
aluminum.mass += 1