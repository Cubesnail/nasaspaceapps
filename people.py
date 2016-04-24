# PEOPLE

class Person:
    """Person class. Able to work within the buildings

    """
    def __init__(self, name, age, mass, sex, job = None, health: int = 0,location = []):
        """Initialize a person object.

        :param name: str
        :param age: int
        :param mass: int
        :param sex: 'M'/'F'
        :param job: None
        :param health: 0
        :param location: None
        :return:
        """
        self.name = name
        self.age = age  # age in weeks
        self.mass = mass  # weight in kilo
        self.health = health  # 0 neutral, -100 dead, +100 Arnold Schwarz
        self.job = job
        self.sex = sex
        self.location = location

    def update_age(self):
        """Update the age of the person on a weekly basis.

        :rtype: None
        """
        self.age += 1

    def is_ded(self):
        return self.health <= -100 or self.age >= 70*52

    def __str__(self):
        return 'Name: {}, Age: {}, Sex: {}'.format(self.name,self.age,self.sex)