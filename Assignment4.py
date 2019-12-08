from os import system, name
from ship import Ship 
from gameboard import Board
from player import Player
from random import randint

def clear(): 
    ''' This function clears the screen to make the game easier to see. '''
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def setup(player):
    checkList = []
    passcondition = False
    for i in player.shipList:
        row = int(input(player.name + "input row for: " + i.name))
        col = int(input(player.name + "input col for: " + i.name))

        orientation = int(input(player.name + "input orientation for: 0 for vertical, 1 for horizantal" + i.name))
        passcondition = player.sBoard.placeShip(i, row, col, "vertical")
        if passcondition == False:
            while passcondition == False:
                print("Unable to place Boat, Enter Again")
                row = int(input(player.name + "input row for: " + i.name))
                col = int(input(player.name + "input col for: " + i.name))
                orientation = int(input(player.name + "input orientation for: 0 for vertical, 1 for horizantal" + i.name))
                if orientation == 0:
                    passcondition = player.sBoard.placeShip(i, row, col, "vertical")
                else:
                    player.sBoard.placeShip(i, row, col, "horizantal")

def main():
    win = False
    turn = 0

    p1Ship = [Ship('Patrol Boat', 1, 2), Ship('Submarine', 2, 3), Ship('Destroyer', 3, 3), Ship('Battleship', 4, 4), Ship('Carrier', 5, 5)]
    p2Ship = [Ship('Patrol Boat', 1, 2), Ship('Submarine', 2, 3), Ship('Destroyer', 3, 3), Ship('Battleship', 4, 4), Ship('Carrier', 5, 5)]

    p1Name = input("Enter name for Player 1")
    p2Name = input("Enter name for Player 2")

    p1 = Player(p1Name, Board(10,10), Board(10,10), p1Ship)
    p2 = Player(p2Name, Board(10,10), Board(10,10), p2Ship)

    setup(p1)
    setup(p2)

    while(win == False):
        if turn%2 == 0:
            print(p1.name, " Turn-------------------\n")
            p1.fBoard.print()
            predictRow = int(input("Choose a row"))
            predictCol = int(input("Choose a col"))
            resultE = p2.sBoard.isEmpty(predictRow, predictCol)
            if resultE == True:
                p1.fBoard.placeFire(1, predictRow, predictCol)
            else:
                p1.fBoard.placeFire(9, predictRow, predictCol)
                targetShip = p2.sBoard.getShip(predictRow, predictCol)
                for ship in p2.shipList:
                    if ship.name == targetShip:
                        results = ship.setHits()
                        if results == True:
                            p2.putShip(ship)
                            print(p2.sunkList)
                        else:
                            print(ship.getHits())
            if len(p2.sunkList) == 5:
                print(p1.name, " Is the Winner")
                win == True
                break
            else:
                turn = 1
                clear()

        else:
            print(p2.name, " Turn-------------------\n")
            p2.fBoard.print()
            predictRow = int(input("Choose a row"))
            predictCol = int(input("Choose a col"))
            resultE = p1.sBoard.isEmpty(predictRow, predictCol)
            if resultE == True:
                p2.fBoard.placeFire(1, predictRow, predictCol)
            else:
                p2.fBoard.placeFire(9, predictRow, predictCol)
                targetShip = p1.sBoard.getShip(predictRow, predictCol)
                for ship in p1.shipList:
                    if ship.name == targetShip:
                        results = ship.setHits()
                        if results == True:
                            p1.putShip(ship)
                            print(p1.sunkList)
                        else:
                            print(ship.getHits())
            if len(p1.sunkList) == 5:
                print(p2.name, " Is the Winner")
                win == True
                break
            else:
                turn = 0
                clear()


if __name__ == '__main__':
    main()

