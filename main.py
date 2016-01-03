import agents
import connectx

print "WELCOME TO CONNECTX" 
board = connectx.Board()
solver = agents.Solver(connectx.RED)
human = agents.Human(connectx.BLK)
print  "SETUP COMPLETE, YOU ARE BLACK" 

while True:
	print "THE CURRENT BOARD: "
	board.printBoard()
	human.playNextMove(board)
	if board.lastMoveWon(): break
	print "THE CURRENT BOARD: "
	board.printBoard()
	solver.playNextMove(board)
	if board.lastMoveWon(): break

winnerStr = "RED" if board.winner == connectx.RED else "BLACK"
print "THE CURRENT BOARD: "
board.printBoard()
print 
print '\033[1m' + winnerStr, "WINS" + '\033[0m'
print 