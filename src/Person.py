
class Person(object):

    def __init__(self, id, type):
        self.id = id
        self.type = type

    def setType(self, MyType):
        self.type = MyType

    def getId(self):
        return self.id

    def getType(self):
        return self.type