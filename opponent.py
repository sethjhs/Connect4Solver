import connectx
# from pretty_print import *
import random
#comp is red




class Solver(object):
	def __init__(self, cols, numIters = 3000):
		self.numIters = numIters
		

	def nextMove(self, board):
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
		return maxCol

	def __playRandomGame(self, col, board):
		#play game starting with move from RED at col
		testBoard = connectx.Board(grid = board.grid, heights = board.heights)

		colChoices = range(testBoard.cols)
		if not testBoard.move(col, connectx.RED): return connectx.BLK
		if testBoard.hasWinner(col): return testBoard.winner
		while not testBoard.isTie():
			if colChoices:
				blkMove = random.choice(colChoices)
				while not testBoard.move(blkMove,connectx.BLK):
					colChoices.remove(blkMove)
					if colChoices:
						blkMove = random.choice(colChoices)
					else:
						break
			winner = testBoard.hasWinner(blkMove)
			if winner: return winner
			if colChoices:
				redMove = random.choice(colChoices)
				while not testBoard.move(redMove,connectx.RED):
					colChoices.remove(redMove)
					if colChoices:
						redMove = random.choice(colChoices)
					else:
						break
			winner = testBoard.hasWinner(redMove)
			if winner: return winner	
		return 0		



