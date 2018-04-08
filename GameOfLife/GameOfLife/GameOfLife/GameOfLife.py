import sys;

gridSize = 1000;
timeStep = 16 #milliseconds

'''
Iterates over neighbours of cell at (xPos,yPos) and 
returns the numbers of neightbours that are currently alive
'''
def countLiveNeighbours(board, xPos, yPos):
    print("increase time")

'''
Performs a transition 
'''
def runSimulationStep(board):
    print("perform transitions")

'''
Creates the board as a square matrix with initial live cells
based on the seePattern
'''
def initBoard(gridSize, seedPattern):
    print("Create board")

def main():
    print("start program")



if __name__ == "__main__":
    main()
    #sys.exit(int(main() or 0))