class TicTacToeAI:

    def __init__(self, player = "x") :
        self._squares = {}
        self._copySquares = {}
        self._winningCombos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])

    def createBoard(self) :
        for i in range(9) :
            # *** use a single character, ... easier to print
            self._squares[i] = "."
        print(self._squares)

    def showBoard(self) :
        # *** add empty line here, instead of in minimax
        print ()
        print(self._squares[0], self._squares[1], self._squares[2])
        print(self._squares[3], self._squares[4], self._squares[5])
        print(self._squares[6], self._squares[7], self._squares[8])


    def getAvailableMoves(self) :
        self._availableMoves = []
        for i in range(9) :
            # *** see above
            if self._squares[i] == "." :
                self._availableMoves.append(i)
        return self._availableMoves

    def makeMove(self, position, player) :
        self._squares[position] = player
        self.showBoard()

    def complete(self) :
        # *** see above
        if "." not in self._squares.values() :
            return True
        if self.getWinner() != None :
            return True
        return False

    def getWinner(self) :
        for player in ("x", "o") :
            for combos in self._winningCombos :
                if self._squares[combos[0]] == player and self._squares[combos[1]] == player and self._squares[combos[2]] == player :
                    return player
        # *** see above
        if "." not in self._squares.values() :
            return "tie"
        return None

    def getEnemyPlayer(self, player) :
        if player == "x" :
            return "o"
        return "x"

    # *** no need for `node` argument, nor `first`
    # *** use `self` instead of `node` in all this method
    def minimax(self, player, depth = 0) :
        # *** not needed
        # if first :
            # best = 0
            # *** not needed
            # self._copySquares = deepcopy(self._squares)
        # *** always start with initilisation of `best`, but with worst possible value
        #     for this player
        if player == "o": 
            best = -10
        else:
            best = 10
        if self.complete() :
            if self.getWinner() == "x" :
                # *** don't do this, you may still need the position to try other moves 
                # self._squares = self._copySquares
                # *** value should be closer to zero for greater depth!
                # *** expect tuple return value
                return -10 + depth, None
            elif self.getWinner() == "tie" :
                # self._squares = self._copySquares
                # *** expect tuple return value
                return 0, None
            elif self.getWinner() == "o" :
                # self._squares = self._copySquares
                # *** value should be closer to zero for greater depth!
                # *** expect tuple return value
                return 10 - depth, None
            # *** Execution can never get here
            # best = None
        for move in self.getAvailableMoves() :
            # *** don't increase depth in each iteration, instead pass depth+1 to
            #    the recursive call
            # depth += 1
            self.makeMove(move, player)
            # *** pass depth+1, no need for passing `node` nor `first`.
            # *** expect tuple return value
            val, _ = self.minimax(self.getEnemyPlayer(player), depth+1)
            print(val)
            # *** undo last move
            self.makeMove(move, ".")
            if player == "o" :
                if val > best :
                    # *** Also keep track of the actual move
                    best, bestMove = val, move
            else :
                if val < best :
                    # *** Also keep track of the actual move
                    best, bestMove = val, move
            # *** don't interrupt the loop here!
            # return best
            # *** this is dead code:
            # print()
            # print()
        # *** Also keep track of the actual move
        return best, bestMove

    def printCopy(self) :
        print(self._copySquares)

if __name__ == "__main__":

    game = TicTacToeAI()
    game.createBoard()
    game.makeMove(0, "o")
    game.makeMove(1, "x")
    game.makeMove(2, "o")
    game.makeMove(3, "x")
    # game.makeMove(4, "o")
    # game.makeMove(5, "x")
    val, bestMove = game.minimax("o")
    print('best move', bestMove) # --> 0 is a winning move.

# [MiniMax Algorithm for Tic Tac Toe (Python)](https://stackoverflow.com/a/44090652)