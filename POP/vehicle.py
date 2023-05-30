class Vehicle:
    def __init__(self, speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2):
        self.speed = speed
        self.passenger_capacity = passenger_capacity
        self.fuel_capacity = fuel_capacity
        self.characteristic1 = characteristic1
        self.characteristic2 = characteristic2

    def accelerate(self):
        print("The vehicle is accelerating.")

    def brake(self):
        print("The vehicle is braking.")
