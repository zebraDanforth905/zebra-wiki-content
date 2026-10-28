class Car:
    def __init__(self, make, model, year, price, available):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.available = available

    def __str__(self):
        return ("Make: " + self.make +
                "\nModel: " + self.model +
                "\nYear: " + str(self.year) +
                "\nPrice: " + str(self.price) +
                "\nAvailable: " + str(self.available) + "\n")
