# PEOPLE


class Person:
    # __init__: self, Str, Nat, Int, Int, Int, Str
    def __init__(self, ):
        self.name = name
        self.age = age  # age in weeks
        self.weight = weight  # weight in kilo
        self.health = health  # 0 neutral, -100 dead, +100 Arnold Schwarz
        self.job = job

    def update_age(self):
        self.age += 1

    def update_health(self, factor):
        self.health += factor
