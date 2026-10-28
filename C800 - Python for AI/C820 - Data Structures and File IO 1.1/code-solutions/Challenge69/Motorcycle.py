from CarClass import Car


class Motorcycle(Car):
    # type is "Standard" or "Sport Bike"
    def __init__(self, make, model, year, price, available, type):
        Car.__init__(self, make, model, year, price, available)
        self.type = type

    # Override __str__ to add the Motorcycle's extra attribute
    def __str__(self):
        return Car.__str__(self) + "Type: " + self.type + "\n"
