class Car(Vehicle):
    def __init__(self, speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2, seating_capacity):
        super().__init__(speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2)
        self.seating_capacity = seating_capacity

    def calculate_fare(self, distance):
        # Calculate the fare based on the distance and seating capacity
        # Add your calculation logic here
        pass
car1 = Car(100, 4, 50, "Characteristic1Value", "Characteristic2Value", 5)
car2 = Car(120, 2, 60, "Characteristic1Value", "Characteristic2Value", 4)