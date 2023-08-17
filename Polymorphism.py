# polymorphism allows different objects to respond to the same
# method in their own way
class shape:
    def area(self):
        pass


class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 2


# creating objects
shape = [Circle(5), Square(4)]
for i in shape:
    print("Area:", i.area())
