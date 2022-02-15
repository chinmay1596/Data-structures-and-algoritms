class Student:

    def __init__(self, age):
        self.age = 12


class Dancer:
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name


a = Dancer(12, 'chinmay')
