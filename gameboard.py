
class Board:

    def __init__(self, rows, cols):
        self.board = [[0 for i in range(rows)] for j in range(cols)]

    def isEmpty(self, row, col):
        if self.board[row][col] == 0:
            return True
        else:
            return False

    def placeFire(self, HoM, row, col):
        self.board[row][col] = HoM

    def getShip(self, row, col):
        if self.board[row][col]==1:
            return 'Patrol Boat'
        if self.board[row][col]==2:
            return 'Submarine'
        if self.board[row][col]==3:
            return 'Destroyer'
        if self.board[row][col]==4:
            return 'Battleship'
        if self.board[row][col]==5:
            return 'Carrier'

    def placeShip(self, myship, row, col, orientation):
        ''' placeShip will place the ident of the ship at row, col, and takes
        the orientation. 
        DO NOT MODIFY THIS FUNCTION'''
        shipId = myship.getId()
        #allow = []
        shipSize = myship.getSize()
        loc = []
        a = row + shipSize
        b = col + shipSize
        if orientation == 'vertical':
            for i in range(shipSize):
                if a > 9:
                    return(False)
                if self.isEmpty(row+i, col) == False:  
                    return(False)
        else:
            for i in range(shipSize):
                if b > 9:
                    return(False)
                if self.isEmpty(row, col+i) == False:
                    return(False)
        if orientation == 'vertical':
            for i in range(shipSize):
                self.board[row+i][col] = shipId
                loc.append([row+i, col])
        else:
            for i in range(shipSize):
                self.board[row][col+i] = shipId
                loc.append([row, col+i])
                
        myship.location = loc.copy()
        return(True)
    
    def print(self):
        print('     ','0',' | ','1',' | ','2',' | ','3',' | ','4',' | ','5',' | ','6',' | ','7',' | ','8',' | ','9', ' | ')
        print('----------------------------------------------------------------')
        for row in range(0,10):                
            print(row, ' | ',
                  self.board[row][0], ' | ',
                  self.board[row][1], ' | ',
                  self.board[row][2], ' | ',
                  self.board[row][3], ' | ',
                  self.board[row][4], ' | ',
                  self.board[row][5], ' | ',
                  self.board[row][6], ' | ',
                  self.board[row][7], ' | ',
                  self.board[row][8], ' | ',
                  self.board[row][9], ' | ',)
        
        print('----------------------------------------------------------------')

        