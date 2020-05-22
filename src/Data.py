from random import randint

from src.Person import Person

class Data(object):
    data =[]

    def __init__(self, size):
        self.data = self.GenerateData(size)

    def GenerateData(self, size):
        generatedData= []
        for i in range(size):
            x= randint(1,101)
            print(x)
            generatedData.append(x)

        return generatedData
