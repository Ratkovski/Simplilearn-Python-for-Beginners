# polymorphism   is the feature of using the same function in multiple ways
class Car:  # parent class
    def __init__(self, name):
        self.name = name


class Sedan(Car):  # child class
    def accelerate(self):
        print('150')


class SUV(Car):  # child class
    def accelerate(self):
        print('180')


objL = [Sedan("Camry"), SUV("Scorpio")]

for obj in objL:
    print(obj.name + ": ", end="")
    obj.accelerate()
