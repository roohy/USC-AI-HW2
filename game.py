class Cell:
    def set_state(self,st):
        self.state = st
    def get_state(self):
        return self.state

class Move:
    def __init__(self):
        pass

class State:

    points = [
        [99 , -8 , 8 , 6 , 6 , 8 , -8 , 99],
        [-8 ,-24 ,-4 ,-3 ,-3 ,-4 ,-24 , -8],
        [ 8 , -4 , 7 , 4 , 4 , 7 , -4 ,  8],
        [ 6 , -3 , 4 , 0 , 0 , 4 , -3 ,  6],
        [ 6 , -3 , 4 , 0 , 0 , 4 , -3 ,  6],
        [ 8 , -4 , 7 , 4 , 4 , 7 , -4 ,  8],
        [-8 ,-24 ,-4 ,-3 ,-3 ,-4 ,-24 , -8],
        [99 , -8 , 8 , 6 , 6 , 8 , -8 , 99],
    ]

    def __init__(self):
        self.board = []
        for i in range (0,8):
            self.board.append( [Cell() for j in range(0,8)])
        self.name = 'root'
    def getName(self):
        if self.name == 'root':
            return 'root'
        if self.name == 'pass':
            return 'pass'
        return ['a','b','c','d','e','f','g','h'][self.name[1]]+str(self.name[0]+1)
    def boardString(self):
        result = ""
        for row in self.board:
            for el in row:
                result += '*' if el.state == 0 else ( 'X' if el.state == 2 else 'O')
            result +='\n'
        return result

    def cross(self, iPace,jPace , i , j, turn , passed = False):
        target = 1 if turn == 2 else 2
        newi = i + iPace
        newj = j + jPace
        if newi >= 0 and newj >=0 and newj<8 and newi<8 and self.board[newi][newj].state == target:
            while newi >= 0 and newj >=0 and newj<8 and newi<8:
                if self.board[newi][newj].state == turn:
                    return True
                elif self.board[newi][newj].state == 0:
                    return False
                else:
                    if passed:
                        self.board[newi][newj].state = turn
                newi += iPace
                newj += jPace
        return False
        ##########################################

    def boardValue(self, turn):
        target = 1 if turn == 2 else 2
        weight = 0
        for i in range(0 , 8):
            for j in range(0,8):
                if self.board[i][j].state == turn:
                    weight += self.points[i][j]
                elif self.board[i][j].state == target:
                    weight -= self.points[i][j]
        self.point = weight
        return weight



    def makeMove(self , newPos , turn):
        print("make move func pos is ", newPos)
        nextSt = State()
        for i in range(0,8):
            for j in range(0,8):
                nextSt.board[i][j].state = self.board[i][j].state
        nextSt.board[newPos[0]][newPos[1]].state = turn
        if nextSt.cross(1,1,newPos[0] , newPos[1] , turn ):
            nextSt.cross(1,1,newPos[0] , newPos[1] , turn , True)
        if nextSt.cross(0,1,newPos[0] , newPos[1] , turn ):
            nextSt.cross(0,1,newPos[0] , newPos[1] , turn , True)
        if nextSt.cross(1,0,newPos[0] , newPos[1] , turn ):
            nextSt.cross(1,0,newPos[0] , newPos[1] , turn , True)
        if nextSt.cross(0,-1,newPos[0] , newPos[1] , turn ):
            nextSt.cross(0,-1,newPos[0] , newPos[1] , turn , True)
        if nextSt.cross(-1,0,newPos[0] , newPos[1] , turn ):
            nextSt.cross(-1,0,newPos[0] , newPos[1] , turn , True)
        if nextSt.cross(-1,1,newPos[0] , newPos[1] , turn ):
            nextSt.cross(-1,1,newPos[0] , newPos[1] , turn , True)
        if nextSt.cross(1,-1,newPos[0] , newPos[1] , turn ):
            nextSt.cross(1,-1,newPos[0] , newPos[1] , turn , True)
        if nextSt.cross(-1,-1,newPos[0] , newPos[1] , turn ):
            nextSt.cross(-1,-1,newPos[0] , newPos[1] , turn , True)
        nextSt.printState()
        return nextSt
    def printState(self):
        for i in self.board:
            print( [st.get_state() for st in i])


    def isFull(self):
        for i in range(0,8):
            for j in range(0,8):
                if self.board[i][j].state == 0:
                    return False
        return True

    def isOneSided(self):
        wCount = 0
        bCount = 0
        for i in range(0,8):
            for j in range(0,8):
                if self.board[i][j].state == 1:
                    wCount += 1
                elif self.board[i][j].state == 2:
                    bCount += 1
        if wCount == 0 or bCount == 0:
            return True
        return False
    def isEnded(self):
        if self.isOneSided() or self.isFull():
            return True
        return False
    def get_position_list(self, turn):
        result = []
        for i in range(0,8):
            for j in range(0,8):
                if self.board[i][j].get_state() == turn :
                    result.append((i,j))
        return result



    def starCheck(self,turn,pos):
        # print("**checking star moves for ", pos)
        possibleMoves = []
        target = 1 if turn == 2 else 2
        i = pos[0]+1
        j = pos[1]
        if i < 8 and self.board[i][j].state == target:
            while i < 8 :
                if self.board[i][j].state == 0 :
                    possibleMoves.append((i,j))
                    break
                if self.board[i][j].state == turn:
                    break
                i += 1

        i = pos[0]-1
        j = pos[1]
        if i>=0 and self.board[i][j].state == target:
            while i >= 0 :
                if self.board[i][j].state == 0 :
                    possibleMoves.append((i,j))
                    break
                if self.board[i][j].state == turn:
                    break
                i -= 1


        i = pos[0]
        j = pos[1]+1
        if j < 8 and self.board[i][j].state == target:
            while j < 8 :
                if self.board[i][j].state == 0 :
                    possibleMoves.append((i,j))
                    break
                if self.board[i][j].state == turn:
                    break
                j += 1

        i = pos[0]
        j = pos[1]-1

        if j>=0 and self.board[i][j].state == target:
            while j >= 0 :
                if self.board[i][j].state == 0 :
                    possibleMoves.append((i,j))
                    break
                if self.board[i][j].state == turn:
                    break
                j -= 1
        i = pos[0]-1
        j = pos[1]-1
        if j>=0 and i >= 0 and self.board[i][j].state == target:
            while j >= 0 and i >= 0 :
                if self.board[i][j].state == 0 :
                    possibleMoves.append((i,j))
                    break
                if self.board[i][j].state == turn:
                    break
                j -= 1
                i -= 1

        i = pos[0]-1
        j = pos[1]+1
        if j < 8 and i >= 0 and self.board[i][j].state == target:
            while j < 8 and i >= 0 :
                if self.board[i][j].state == 0 :
                    possibleMoves.append((i,j))
                    break
                if self.board[i][j].state == turn:
                    break
                j += 1
                i -= 1

        i = pos[0]+1
        j = pos[1]-1
        if j>=0 and i < 8 and self.board[i][j].state == target:
            while j >= 0 and i < 8 :
                if self.board[i][j].state == 0 :
                    possibleMoves.append((i,j))
                    break
                if self.board[i][j].state == turn:
                    break
                j -= 1
                i += 1

        i = pos[0]+1
        j = pos[1]+1
        if j < 8 and i < 8 and self.board[i][j].state == target:
            while j < 8 and i < 8 :
                if self.board[i][j].state == 0 :
                    possibleMoves.append((i,j))
                    break
                if self.board[i][j].state == turn:
                    break
                j += 1
                i += 1
        return possibleMoves



    def possibleMovesFor(self, turn):
        # print("///////////////////////////////")
        posArray = self.get_position_list(turn)
        # posArray.sort(key = lambda element : (element[0],element[1]))
        temp = (-1,-1)
        for i in range(0, len(posArray)):
            if posArray[i][0] == temp[0] and posArray[i][1] == temp[1]:
                posArray.pop(i)
                continue
            temp = (posArray[i][0], posArray[i][1])
        result = []
        for pos in posArray:
            tempResult = self.starCheck(turn , pos)
            for item in tempResult:
                result.append(item)
        result.sort(key = lambda  element : (element[0],element[1]))
        print("moves checked result is ",result)
        return result
