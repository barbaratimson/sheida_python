from country import *
class Russia(Country):
    population = 0
    def __init__(self):
        super().__init__()
    def setPopulation(self, a):
        self.population = a
    def getPopulation(self):
        return self.population
