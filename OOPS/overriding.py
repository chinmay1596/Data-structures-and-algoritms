class Shape(object):
    l = []
    def area(self, data):
        self.l.append(data)


class Circle(Shape):
    def area(self):
        print("this is area of circle")


obj = Circle()
# obj.area()

a = {'a':1, 'b':2}
print(a)