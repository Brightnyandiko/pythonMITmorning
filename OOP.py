# A class is a blue


class students:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def sayhello(self):
        print("My name is ", self.name, "i'm", self.age, "years and a", self.gender)


myobject = students(name="Ronald", gender="male", age=20)

myobject.sayhello()
