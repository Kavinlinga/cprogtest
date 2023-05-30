from vehicle import Vehicle
from car import Car
from motorbike import Motorbike

# Create instances and test the classes here
class Car(Vehicle):
    def __init__(self, speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2, seating_capacity):
        super().__init__(speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2)
        self.seating_capacity = seating_capacity

    def calculate_fare(self, distance):
        # Calculate the fare based on the distance and seating capacity
        # Add your calculation logic here
        pass


class Motorbike(Vehicle):
    def __init__(self, speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2, vehicle_type):
        super().__init__(speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2)
        self.vehicle_type = vehicle_type


# Create instances of the Car and Motorbike classes
car1 = Car(100, 4, 50, "Characteristic1Value", "Characteristic2Value", 5)
car2 = Car(120, 2, 60, "Characteristic1Value", "Characteristic2Value", 4)
motorbike = Motorbike(80, 1, 30, "Characteristic1Value", "Characteristic2Value", "Sport")

# Test the calculate_fare() method of the Car class
car1.calculate_fare(10)  # Calculate fare for a 10 km journey for car1
car2.calculate_fare(10)  # Calculate fare for a 10 km journey for car2