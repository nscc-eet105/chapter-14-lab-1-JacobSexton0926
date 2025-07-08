#Jacob Sexton 7/8/25
class Vehicle:
    def __init__(self):
        self.__speed = 0

    def accelerate(self):
        self.__speed += 1

    def decelerate(self):
        self.__speed -= 1

    def display_speed(self):
        print("Current Speed:", self.__speed)

acc = 'Accelerating...'
dec = 'Decelerating...'

#vehicle object
my_vehicle = Vehicle()

#accelerate 2 times
print(acc)
my_vehicle.accelerate()
my_vehicle.display_speed()
print(acc)
my_vehicle.accelerate()
my_vehicle.display_speed()

#decelerate 2 times
print('\n'+dec)
my_vehicle.decelerate()
my_vehicle.display_speed()
print(dec)
my_vehicle.decelerate()
my_vehicle.display_speed()
