# PEOPLE

class Person:
    # __init__: self, Str, Nat, Int, Int, Int, Str
    def __init__(self, name, age, mass, sex, job = None, health: int = 0,location = []):
        self.name = name
        self.age = age  # age in weeks
        self.mass = mass  # weight in kilo
        self.health = health  # 0 neutral, -100 dead, +100 Arnold Schwarz
        self.job = job
        self.sex = sex
        self.location = location

    def update_age(self):
        self.age += 1

    def update_health(self, factor):
        self.health += factor

    def is_ded(self):
        return self.health <= -100 or self.age >= 70*52

    def __str__(self):
        return 'Name: {}, Age: {}, Sex: {}'.format(self.name,self.age,self.sex)