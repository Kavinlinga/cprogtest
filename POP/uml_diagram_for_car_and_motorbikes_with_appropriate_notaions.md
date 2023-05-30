+------------------------------------+
|              Vehicle               |
+------------------------------------+
| - speed: float                     |
| - passenger_capacity: int          |
| - fuel_capacity: float             |
| - characteristic1: type            |
| - characteristic2: type            |
+------------------------------------+
| + __init__(speed: float, passenger_capacity: int, fuel_capacity: float, characteristic1: type, characteristic2: type) |
| + accelerate(): void               |
| + brake(): void                    |
+------------------------------------+
            ^
            |
+-------------------+ +-------------------+
|        Car        | |     Motorbike     |
+-------------------+ +-------------------+
| - seating_capacity: int              |
| - car_specific_attribute: type       |
+-------------------+ +-------------------+
| + __init__(speed: float, passenger_capacity: int, fuel_capacity: float, characteristic1: type, characteristic2: type, seating_capacity: int, car_specific_attribute: type) |
| + accelerate(): void               |
| + brake(): void                    |
+-------------------+ +-------------------+
