import connectx
# from pretty_print import *
import random
#comp is red


class Agent(object):
	def __init__(self, color, numIters = 5):
		self.numIters = numIters
		self.color = color
	
	def getNextMove(self, board):
		raise NotImplementedError


class Human(Agent):

	def playNextMove(self, board):

		while True:
			try:
				col = int(raw_input('ENTER A COLUMN NUMBER [0-' + str(int(board.cols-1)) + ']: '))
				if board.move(col,connectx.BLK): break
			except ValueError:
				print 'INVALID MOVE, TRY AGAIN'
		return col

class Solver(Agent):

	def playNextMove(self, board):
		maxVal = float("-infinity")
		maxCol = -1
		print sum(board.heights)
		for col in range(board.cols):
			testBoard = connectx.Board(grid = board.grid, heights = board.heights)
			if not testBoard.move(col,self.color): continue
			d = 0
			if sum(board.heights) > 10: d = 3
			if sum(board.heights) > 15: d = 4
			if sum(board.heights) > 25: d = 6

			val = self.__minimax(testBoard,d,self.color*-1)
			print col, val
			if val > maxVal:
				maxVal = val
				maxCol = col
		if not board.move(maxCol,self.color):
			for col in range(board.cols):
				if board.move(col,self.color): break
		return maxCol

	def __minimax(self, board, depth, player):
	    #maximize for red
	    #minimize for black
	    winner = board.lastMoveWon()
	    if winner == self.color:
	    	return float("infinity")
	    elif winner == (self.color*-1):
	    	return float("-infinity")

	    if depth <= 0 and player == self.color:
	        wins = 1.0
	        losses = 1.0
	        const = 2000
	        if sum(board.heights) > 10: const = 80
	        if sum(board.heights) > 15: const = 9
	        
	        iters = (int((sum(board.heights)*.08)**2))+const
	        for i in range(iters):
				res = self.__playRandomGame(random.choice(range(board.cols)), board)
				if res == self.color: wins += 1
				if res == (self.color*-1): losses += 1

	        return wins/losses




	    if player == self.color:
	       bestValue = float("-infinity")
	    else:
	       bestValue = float("infinity")
	    
	    for col in range(board.cols):
	        testBoard = connectx.Board(grid = board.grid, heights = board.heights)
	        if not testBoard.move(col, player): continue
	        val = self.__minimax(testBoard, depth - 1, player*(-1))
	        if player == self.color:
	            bestValue = max(bestValue, val)
	            if bestValue == float("infinity"): return bestValue
	        else:
	            bestValue = min(bestValue, val)
	            if bestValue == float("-infinity"): return bestValue

	    return bestValue

	def __playRandomGame(self, col, board):
		#play game starting with move from RED at col
		testBoard = connectx.Board(grid = board.grid, heights = board.heights)

		colChoices = range(testBoard.cols)
		if not testBoard.move(col, self.color): return self.color*-1
		if testBoard.lastMoveWon(): return testBoard.winner
		
		while not testBoard.isTie():

			if colChoices:
				blkMove = random.choice(colChoices)
				while not testBoard.move(blkMove,self.color*-1):
					colChoices.remove(blkMove)
					if colChoices:
						blkMove = random.choice(colChoices)
					else:
						break
			winner = testBoard.lastMoveWon()
			if winner: return winner
			if colChoices:
				redMove = random.choice(colChoices)
				while not testBoard.move(redMove,self.color):
					colChoices.remove(redMove)
					if colChoices:
						redMove = random.choice(colChoices)
					else:
						break
			winner = testBoard.lastMoveWon()
			if winner: return winner	
		return 0		



