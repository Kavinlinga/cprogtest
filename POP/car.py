from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2, seating_capacity):
        super().__init__(speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2)
        self.seating_capacity = seating_capacity

    def calculate_fare(self, distance):
        # Add your fare calculation logic here
        pass
