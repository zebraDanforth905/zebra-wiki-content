from CarClass import Car


class Truck(Car):
    # type is "Full-size" or "Midsize"; bedSize is "Long bed" or "Short bed"
    def __init__(self, make, model, year, price, available, type, bedSize):
        Car.__init__(self, make, model, year, price, available)
        self.type = type
        self.bedSize = bedSize
