class Car:
    def __init__(self, make, model, year, price, available):
        self.make = make
        self.model = model
        self.year = year
        self.__price = price
        self.__available = available

    def getPrice(self):
        return self.__price

    def setPrice(self, newPrice):
        self.__price = newPrice

    def getAvailable(self):
        return self.__available

    def setAvailable(self, newAvailable):
        self.__available = newAvailable

    def __str__(self):
        return ("Make: " + self.make +
                "\nModel: " + self.model +
                "\nYear: " + str(self.year) +
                "\nPrice: " + str(self.__price) +
                "\nAvailable: " + str(self.__available) + "\n")
