# whats is oops   oops-object oriented programming
# programming paradigm that focuses on objects
# every instance in python is an object


class car:
    def __init__(self, year, speed):
        self.year = year
        self.speed = speed

    def getSpeed(self):
        print("maximum speed is: ", self.speed)

    def setSpeed(self, speed):
        self.speed = speed


BMW = car(2018, 155)
FORD = car(2016, 140)
# car.getSpeed(BMW)
# car.getSpeed(FORD)
BMW.setSpeed(143)
BMW.getSpeed()
FORD.getSpeed()


# inhritance is a mechanism for a new class to use the features of another class

class Sedan(car):  # child class
    def accelerate(self):
        print('137')

    def openTrunk(self):
        print('trunk has been opened')


class SUV(car):  # child class
    def accelerate(self):
        print('127')


Honda = Sedan(2018, 150)
BMW.getSpeed()
Honda.getSpeed()
Honda.openTrunk()
Honda.accelerate()


