# Inheritance allows one class to move attributes
# and methods from another class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"


class Sheep(Animal):
    def speak(self):
        return "bleats"


class goats(Animal):
    def speak(self):
        return "bleats"


# this are objects
mbwa = Dog("buddy")
cat = Cat("whisker")
sheep = Sheep("collins")
goat = goats("voke")
print(mbwa.speak())
print(cat.speak())
print(sheep.speak())
print(goat.speak())
