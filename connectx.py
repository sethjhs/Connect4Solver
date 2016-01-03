import numpy as np

RED = -1
BLK = 1


class Board(object):

	def __init__(self, rows = 6, cols = 7, toWin = 4, grid = None, heights = None):
		self.rows = rows
		self.cols = cols
		self.toWin = toWin
		self.grid = np.copy(grid) if grid is not None else np.zeros((rows,cols))
		self.winner = 0
		self.heights = np.copy(heights) if heights is not None else [0 for i in range(cols)]
		self.lastMove = -1

	def isTie(self):
		return sum(self.heights) == self.cols*self.rows

		
	def move(self, col, player):
		if self.heights[col] >= self.rows: return False
		self.grid[self.heights[col], col] = player
		self.heights[col] += 1
		self.lastMove = col
		return True

	def printBoard(self):
		fliped = np.flipud(self.grid)
		for col in range(self.cols):
			print col,
		print
		for row in range(self.rows):
			for col in range(self.cols):
				if fliped[row][col] == RED:
					print '\033[91m' + u'\u25CF' + '\033[0m',
				elif fliped[row][col] == BLK:
					print  u'\u25CF',
				else:
					print u'\u25CB',
			print

	def lastMoveWon(self):
		if not self.winner:
			pos = (self.heights[self.lastMove]-1, self.lastMove)
			self.winner = self.__winFromPosition(pos)
		return self.winner

	def __winFromPosition(self, pos):
		row = pos[0]
		col = pos[1]
		player = self.grid[row][col]
		assert player, "__winFromPosition was called on unoccupied position " + str(row) + " , " + str(col)
		up = 0
		dn = 0
		i = 1
		while row+i < self.rows and self.grid[row+i,col] == player:
			up += 1
			i  += 1
		i = 1
		while row-i >= 0 and self.grid[row-i,col] == player:
			dn += 1
			i  += 1
		if up + dn + 1 >= self.toWin: return player

		rt = 0
		lf = 0
		i = 1
		while col+i < self.cols and self.grid[row,col+i] == player:
			rt += 1
			i  += 1
		i = 1
		while col-i >= 0 and self.grid[row,col-i] == player:
			lf += 1
			i  += 1
		if rt + lf + 1 >= self.toWin: return player

		uprt = 0
		dnlf = 0
		i = 1
		while col+i < self.cols and row+i < self.rows and self.grid[row+i,col+i] == player:
			uprt += 1
			i    += 1
		i = 1
		while col-i >= 0 and row-i >= 0 and self.grid[row-i, col-i] == player:
			dnlf += 1
			i    += 1
		if uprt + dnlf + 1 >= self.toWin: return player

		uplf = 0
		dnrt = 0
		i = 1
		while col-i >= 0 and row+i < self.rows and self.grid[row+i,col-i] == player:
			uplf += 1
			i    += 1
		i = 1
		while col+i < self.cols and row-i >= 0 and self.grid[row-i, col+i] == player:
			dnrt += 1
			i    += 1
		if uplf + dnrt + 1 >= self.toWin: return player
		return 0

