# from abc import ABC, abstractmethod
#
#
# class Carrer(ABC):
#
#     def __init__(self, age):
#         self.age = age
#
#     @abstractmethod
#     def career(self):
#         pass
#
#     @abstractmethod
#     def partner(self):
#         pass
#
# class Son(Carrer):
#
#     def career(self):
#         print("I like to Code")
#
#     def partner(self):
#         print("I like Milli")
#
#
# class Daughter(Carrer):
#
#     def career(self):
#         print("I like to become a Doctor")
#
#     def partner(self):
#         print("I like Iron Man")
#
#
# son = Son(14)
# daughter = Daughter(14)
#
# son.career()
# son.partner()
#
# daughter.career()
# daughter.partner()
#


class Car:

    @staticmethod
    def run(self):
        print('I like to run the car')