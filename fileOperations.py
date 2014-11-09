from game import State,Cell
from gameClass import Game

def ReadFile(filename):
    print("********************READIND FILE********")
    FILE = open(filename, 'r')
    game = Game()
    mode = int(FILE.readline())
    print('mode is ',mode)
    turn = FILE.readline()[0]
    print('turn is',turn)
    cuttingDepth = int(FILE.readline())
    print('cutting depth is',cuttingDepth)
    for i in range(0,8):
        line = FILE.readline()
        for j in range(0,8):
            #print(line[i])
            game.state.board[i][j].set_state(( 0 if line[j] == '*' else (1 if line[j]=='O' else 2)))
    game.mode = mode
    game.turn = 1 if turn == 'O' else 2
    game.depth = cuttingDepth
    return game


def WriteFile(filename , content):
    FILE = open(filename , 'w')
    FILE.write(content)