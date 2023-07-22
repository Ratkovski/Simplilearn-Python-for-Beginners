#the feature of preventing data from direct access is called encapsulation

class car:
    def __init__(self, year, speed):
        self.year = year
        self._speed = speed

    def getSpeed(self):
        print("maximum speed is: ", self._speed)

    def setSpeed(self, speed):
        self._speed = speed


BMW = car(2018, 155)
FORD = car(2016, 140)
BMW.getSpeed()

BMW.setSpeed(150)
BMW.getSpeed()
print(BMW._speed)



