from vehicle import Vehicle
from car import Car
from motorbike import Motorbike

# Create instances and test the classes here

# Example usage of Vehicle class
vehicle = Vehicle(100, 4, 50, "Characteristic1Value", "Characteristic2Value")
vehicle.accelerate()
vehicle.brake()

# Example usage of Car class
car1 = Car(100, 4, 50, "Characteristic1Value", "Characteristic2Value", 5)
car2 = Car(120, 2, 60, "Characteristic1Value", "Characteristic2Value", 4)
car1.calculate_fare(10)  # Calculate fare for a 10 km journey for car1
car2.calculate_fare(10)  # Calculate fare for a 10 km journey for car2

# Example usage of Motorbike class
motorbike = Motorbike(80, 1, 30, "Characteristic1Value", "Characteristic2Value", "Sport")
