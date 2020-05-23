from random import randint

from src.Person import Person

class Data(object):
    data =[]

    def __init__(self, size):
        self.data = self.generateData(size)

    def generateData(self, size):
        generatedData= []

        for i in range(size//100+1):
            p= Person(i, "I")
            generatedData.append(p)

        for i in range(size // 100+1, size):
            p = Person(i, "S")
            generatedData.append(p)

        return generatedData

    def getData(self):
        return  self.data