from vehicle import Vehicle

class Motorbike(Vehicle):
    def __init__(self, speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2, vehicle_type):
        super().__init__(speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2)
        self.vehicle_type = vehicle_type
