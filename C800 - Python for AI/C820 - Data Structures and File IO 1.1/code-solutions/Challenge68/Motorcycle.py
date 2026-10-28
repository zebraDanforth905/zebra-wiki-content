from CarClass import Car


class Motorcycle(Car):
    # type is "Standard" or "Sport Bike"
    def __init__(self, make, model, year, price, available, type):
        Car.__init__(self, make, model, year, price, available)
        self.type = type
