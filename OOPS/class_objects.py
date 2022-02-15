class Student:
    population = 0

    # we can access the static variable by this and class name both
    # bu accessing it with self static variable will be available to that object instance only
    def __init__(self, age, roll_no, name):
        self.age = age
        self.roll_no = roll_no
        self.name = name
        self.population += 1


a = Student(14, 12, 'chinmay')
b = Student(14, 12, 'chinmay')
print(a.population)
print(b.population)
