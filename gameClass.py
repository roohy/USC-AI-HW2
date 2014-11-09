__author__ = 'roohy'
from game import State,Move
import sys
MAXINT = 9999999999
MININT = -9999999999

def printPoint(point):
    if point == MAXINT:
        return 'Infinity'
    if point == MININT:
        return '-Infinity'
    return str(point)

class Game:



    def __init__(self):
        self.state = State()
        self.log = ""

    def getNextMove(self):
        if self.mode == 1:
            return self.getNextGreedyMove()
        if self.mode == 2:
            self.log += "Node,Depth,Value"
            return self.miniMaxNextMove(self.state , self.turn, True, self.depth , True)
        if self.mode == 3:
            self.log += "Node,Depth,Value,Alpha,Beta"
            alpha = State()
            alpha.point = MININT
            beta = State()
            beta.point = MAXINT
            return self.alphaBetaNextMove(self.state , self.turn , True , self.depth , True , alpha , beta)



    def printGreedy(self, state ):
        print("*********print greedy function is called******")
        print("result is \n " , state.boardString())
        return state.boardString()
    def getNextGreedyMove(self):
        movesArray = self.state.possibleMovesFor(self.turn)

        if len(movesArray) == 0 :
            return self.printGreedy(self.state)
        max = State()
        max.point = MININT
        for move in movesArray:
            tempState = self.state.makeMove(move, self.turn)
            tempState.point = tempState.boardValue(self.turn)
            if tempState.point > max.point:
                max = tempState

        return self.printGreedy(max)

    def miniMaxNextMove(self, state, turn , max , depthLeft , root , doublepass = False):
        print("**************************************")
        print("***starting search for depth",depthLeft,"********")
        print("*** turn is ",turn," *****************")
        if depthLeft == 0 or state.isEnded() or doublepass :
            # print("double pass is "+str(doublepass))
            self.log += "\n"+state.getName()+','+str(self.depth-depthLeft)+','
            state.point = state.boardValue(self.turn)
            self.log += printPoint(state.point)
            return state
        movesArray = state.possibleMovesFor(turn)
        if len(movesArray) == 0:
            self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','+('-Infinity' if max else 'Infinity')
            tempName = state.name
            state.name = 'pass'
            dpas = (state.name == 'pass' and tempName == 'pass')
            tempState =  self.miniMaxNextMove(state , 1 if turn == 2 else 2 , not max , depthLeft-1 , False , dpas)
            self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','
            self.log += printPoint(state.point)
            state.point = tempState.point
            state.printState()
            return state
        minimax = State()
        minimax.point = MININT if max == True else MAXINT
        for move in movesArray:
            self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','+printPoint(minimax.point)
            print("making move ", move)
            tempState = state.makeMove(move , turn)
            tempState.name = move
            tempState.point = self.miniMaxNextMove(tempState , 1 if turn == 2 else 2 , not max , depthLeft-1 , False,).point
            print("temp point is ",tempState.point)
            if max and tempState.point > minimax.point :
                minimax = tempState
                continue
            if (not max) and tempState.point < minimax.point:
                minimax = tempState
        print("----------------------------------")
        print("--------------",minimax.point)
        self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','+printPoint(minimax.point)
        return minimax

    def alphaBetaNextMove(self, state, turn , max , depthLeft , root , alpha , beta, doublepass = False):

        print("**************************************")
        print("***starting search for depth",depthLeft,"********")
        print("*** turn is ",turn," *****************" , max)
        if depthLeft == 0 or state.isEnded() or doublepass:
            self.log += "\n"+state.getName()+','+str(self.depth-depthLeft)+','
            state.point = state.boardValue(self.turn)
            self.log += printPoint(state.point)+"," + printPoint(alpha.point) +','+ printPoint(beta.point)
            return state
        movesArray = state.possibleMovesFor(turn)
        if len(movesArray) == 0:
            self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','+('-Infinity' if max else 'Infinity')+','+printPoint(alpha.point)+','+printPoint(beta.point)
            tempName = state.name
            state.name = 'pass'
            dpas = (state.name == 'pass' and tempName == 'pass')
            tempState =  self.alphaBetaNextMove(state , 1 if turn == 2 else 2 , not max , depthLeft-1 , False , alpha , beta , dpas)


            state.point = tempState.point
            state.name = tempName
            if max :
                print("ghergher1")
                if state.point >= beta.point:
                    print("herher1")
                    self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','
                    self.log += printPoint(state.point) +','+ printPoint(alpha.point)+','+printPoint(beta.point)
                    return beta
                if state.point > alpha.point:
                    alpha = state

            else:
                print("ghergher2 , ",printPoint(alpha.point), "  ",printPoint(state.point))
                if state.point <= alpha.point:
                    print("herher2")
                    self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','
                    self.log += printPoint(state.point) +','+ printPoint(alpha.point)+','+printPoint(beta.point)
                    return alpha
                if state.point < beta.point:
                    beta = state
            print("ollaaaaaa")
            self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','
            self.log += printPoint(state.point) +','+ printPoint(alpha.point)+','+printPoint(beta.point)
            return state
        minimax = State()
        minimax.point = MININT if max == True else MAXINT
        for move in movesArray:
            self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','+printPoint(minimax.point)+','+printPoint(alpha.point)+','+printPoint(beta.point)
            print("making move ", move)
            tempState = state.makeMove(move , turn)
            tempState.name = move

            tempState.point = self.alphaBetaNextMove(tempState , 1 if turn == 2 else 2 , not max , depthLeft-1 , False, alpha , beta).point
            print("temp point is ",tempState.point)
            if max and tempState.point > minimax.point :
                print("hoohooooo hoyyy")
                minimax = tempState
                if minimax.point >= beta.point:
                    self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','+printPoint(minimax.point)+','+printPoint(alpha.point)+','+printPoint(beta.point)
                    return beta
                if alpha.point <= minimax.point:
                    alpha = minimax
                continue
            if (not max) and tempState.point < minimax.point:
                minimax = tempState
                # self.log += "ARRRRRRRRRR (((("+str(tempState.point)+"))))"


                if alpha.point >= minimax.point:
                    self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','+printPoint(minimax.point)+','+printPoint(alpha.point)+','+printPoint(beta.point)
                    return alpha
                if beta.point >= minimax.point:
                    beta = minimax
        print("----------------------------------")
        print("--------------",minimax.point)
        self.log += '\n'+state.getName()+','+str(self.depth-depthLeft)+','+printPoint(minimax.point)+','+printPoint(alpha.point)+','+printPoint(beta.point)
        return minimax