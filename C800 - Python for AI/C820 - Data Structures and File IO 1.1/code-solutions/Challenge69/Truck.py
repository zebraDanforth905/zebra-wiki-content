from CarClass import Car


class Truck(Car):
    # type is "Full-size" or "Midsize"; bedSize is "Long bed" or "Short bed"
    def __init__(self, make, model, year, price, available, type, bedSize):
        Car.__init__(self, make, model, year, price, available)
        self.type = type
        self.bedSize = bedSize

    # Override __str__ to add the Truck's extra attributes
    def __str__(self):
        return Car.__str__(self) + "Type: " + self.type + "\nBed Size: " + self.bedSize + "\n"
