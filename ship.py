class Ship:

    def __init__(self, name, id, size):
        self.name = name
        self.id = id
        self.size = size
        self.hits = 0
        self.location = [] 

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getSize(self):
        return self.size

    def getHits(self):
        return self.hits

    def setHits(self):
        self.hits += 1
        return self.isSunk()

    def isSunk(self):
        if self.hits == self.size:
            return True
        else:
            return False

    def getLocation(self):
        return self.location