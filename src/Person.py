
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

    def estSain(self):
        if self.type=='S':
            return True
        else:
            return False

    def estInfecte(self):
        if self.type=='I':
            return True
        else:
            return False

    def estDecede(self):
        if self.type=='D':
            return True
        else:
            return False

    def estGueri(self):
        if self.type=='G':
            return True
        else:
            return False