from vehicle import Vehicle

def test_vehicle():
    vehicle = Vehicle(100, 4, 50, "Characteristic1Value", "Characteristic2Value")
    assert vehicle.speed == 100
    assert vehicle.passenger_capacity == 4
    assert vehicle.fuel_capacity == 50
    assert vehicle.characteristic1 == "Characteristic1Value"
    assert vehicle.characteristic2 == "Characteristic2Value"

    vehicle.accelerate()
    vehicle.brake()

test_vehicle()
