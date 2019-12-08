class Player:

    def __init__(self, name, sBoard, fBoard, shipList):
        self.name = name
        self.sBoard = sBoard
        self.fBoard = fBoard
        self.shipList = shipList
        self.sunkList = []

    def getName(self):
        return self.name

    def printShips(self):
        return self.shipList

    # puts destroyed ship in sunk and deletes from shipList
    def putShip(self, newShip):
        if newShip not in self.sunkList:
            self.sunkList.append(newShip)

    def printFireBoard(self):
        self.fBoard.print()

    def printBoard(self):
        self.sBoard.print()

    def printNavy(self):
        for ship in shipList:
            print("Ship name is: ", ship.name, " The hits are: ", ship.hits)