class Vehicle:

    def start(self):
        print("Vehicle is starting")

class Bike(Vehicle):

    def ride(self):
        print("Bike is riding")

    def starting(self):
        super().start()
    

v = Bike()
v.ride()
v.starting()
