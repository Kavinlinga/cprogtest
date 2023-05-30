# Vehicle Class Diagram

```plaintext
+------------------------------------+
|             Vehicle                |
+------------------------------------+
| - speed: float                     |
| - passenger_capacity: int          |
| - fuel_capacity: float             |
| - characteristic1: type            |
| - characteristic2: type            |
+------------------------------------+
| + __init__(speed, passenger_capacity, fuel_capacity, characteristic1, characteristic2) |
| + accelerate(): void               |
| + brake(): void                    |
+------------------------------------+
