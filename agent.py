__author__ = 'roohy'

from fileOperations import ReadFile,WriteFile

game = ReadFile('input.txt')
print('************starting the game*************')
print('game state is: ')
game.state.printState()

print('getting next move:')
result = game.getNextMove()
print("final result for best move is ")

result.printState()
print(game.log)
WriteFile('output.txt', result.boardString() + game.log)
#game.state.possibleMovesFor(2)