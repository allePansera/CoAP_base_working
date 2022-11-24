import random


class TemperatureSensor:
    """The class defines a temperature sensor"""
    def __init__(self, id="", description="", value="", unit_of_measure="", jsonSerialized=None):
        self.id = id
        self.description = description
        self.value = value
        self.unit_of_measure = unit_of_measure
        if jsonSerialized is not None:
            self.__dict__ = jsonSerialized

    def generateRandom(self):
        """This method create random data to insert inside value and unit_of_measure"""
        self.value = random.randrange(-30,30,1)
        self.unit_of_measure = "C°"