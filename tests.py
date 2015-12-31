import connectx
import numpy as np

grid = np.flipud(np.array([
[ 0.,  0.,  0.,  0.,  1.,  0.,  0.],
[ 0.,  0.,  0., -1., -1.,  0.,  0.],
[ 0.,  0.,  0., -1., -1.,  1.,  0.],
[ 0.,  0.,  0.,  1., -1., -1.,  0.],
[ 0.,  1.,  0.,  1.,  1., -1., -1.],
[ 0.,  1.,  0., -1.,  1., -1.,  1.]
		]))
heights = [0, 2, 0, 5, 6, 4, 2]
testBoard = connectx.Board(grid = grid, heights = heights)
testBoard.printBoard()
print testBoard.hasWinner(6)