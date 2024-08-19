class Vehicle:
    wheel = 4

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


Vehicle.wheel = 6
School_bus = Bus("School Volvo", 12, 50)

result = (type(School_bus))
print(result)
print(School_bus.wheel)
check = isinstance(School_bus, Vehicle)
if check: print("yes intance")
