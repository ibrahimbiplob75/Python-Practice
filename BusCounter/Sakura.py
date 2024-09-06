class Bus:
    company = "Sakura Transport"

    def __init__(self, route, licence, driver):
        self.route = route
        self.licence = licence
        self.driver = driver
        self.trips = []

    def start_trip(self, trip_time):
        self.trip_time = trip_time


class Driver:
    def __init__(self, name, number, licence, salary):
        self.name = name
        self.number = number
        self.licence = licence
        self.salary = salary

    def drive(self, start, end):
        pass

    def vacation(self, off_day):
        pass

    def withdrew_money(self, money):
        pass


class Passenger:
    def __init__(self, name, number, destination):
        self.name = name
        self.number = number
        self.destination = destination


class Manager:
    def __init__(self, name, number, department):
        pass


Biplob = Passenger("Biplob", "015******", "Singapore")

print(Biplob.name, Biplob.number, Biplob.destination)
