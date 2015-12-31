import connectx
# from pretty_print import *
import random
#comp is red


class Agent(object):
	def getNextMove(self, board):
		raise NotImplementedError

class Human(Agent):

	def playNextMove(self, board):
		print "THE CURRENT BOARD: "
		board.printBoard()
		while True:
			try:
				col = int(raw_input('ENTER A COLUMN NUMBER [0-' + str(int(board.cols-1)) + ']: '))
				if board.move(col,connectx.BLK): break
			except ValueError:
				print 'INVALID MOVE, TRY AGAIN'
		return col

class Solver(Agent):
	def __init__(self, numIters = 1000):
		self.numIters = numIters
		

	def playNextMove(self, board):
		maxWinLoss = float("-infinity")
		maxCol = -1
		for col in range(board.cols):
			wins = 1.0
			losses = 1.0
			print col,
			for i in range(self.numIters):
				res = self.__playRandomGame(col, board)
				if res == connectx.RED: wins += 1
				if res == connectx.BLK: losses += 1
			print "w-l:", wins-losses, "w/l:", wins/losses, "w:", wins, "l:", losses
			if wins-losses > maxWinLoss:
				maxWinLoss = wins-losses
				maxCol = col
		if not board.move(maxCol,connectx.RED):
			for col in range(board.cols):
				if board.move(col,connectx.RED): break
		return maxCol

	def __minimax(board, depth, player):
	    #maximize for red
	    #minimize for black
	    winner = board.lastMoveWon()
	    if depth <= 0 and not winner and player == connectx.RED:
	        wins = 1.0
	        losses = 1.0
	        for i in range(self.numIters):
				res = self.__playRandomGame(random.choice(range(board.cols)), board)
				if res == connectx.RED: wins += 1
				if res == connectx.BLK: losses += 1

	        return wins-losses
	    if winner == connectx.RED:
	    	return float("infinity")
	    elif winner == connectx.BLACK:
	    	return float("-infinity")


	    if player == connectx.RED:
	       bestValue = float("-infinity")
	    else:
	       bestValue = float("infinity")
	    
	    for col in range(board.cols):
	        testBoard = connectx.Board(grid = board.grid, heights = board.heights)
	        if not testBoard.move(col, player): return bestValue*-1
	        val = minimax(testBoard, depth - 1, player*(-1))
	        if player == connectx.RED:
	            bestValue = max(bestValue, val)
	        else:
	            bestValue = min(bestValue, val)
	    return bestValue

	def __playRandomGame(self, col, board):
		#play game starting with move from RED at col
		testBoard = connectx.Board(grid = board.grid, heights = board.heights)

		colChoices = range(testBoard.cols)
		if not testBoard.move(col, connectx.RED): return connectx.BLK
		if testBoard.lastMoveWon(): return testBoard.winner
		
		while not testBoard.isTie():

			if colChoices:
				blkMove = random.choice(colChoices)
				while not testBoard.move(blkMove,connectx.BLK):
					colChoices.remove(blkMove)
					if colChoices:
						blkMove = random.choice(colChoices)
					else:
						break
			winner = testBoard.lastMoveWon()
			if winner: return winner
			if colChoices:
				redMove = random.choice(colChoices)
				while not testBoard.move(redMove,connectx.RED):
					colChoices.remove(redMove)
					if colChoices:
						redMove = random.choice(colChoices)
					else:
						break
			winner = testBoard.lastMoveWon()
			if winner: return winner	
		return 0		



