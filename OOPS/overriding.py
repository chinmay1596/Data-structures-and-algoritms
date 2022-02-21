class Shape(object):
    def area(self):
        print("This is area of Shape")


class Circle(Shape):
    def area(self):
        print("this is area of circle")


obj = Circle()
# obj.area()

a = {'a':1, 'b':2}
print(a)