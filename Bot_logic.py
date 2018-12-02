
def Bot_logic(self.board):
    """ The whole idea is that the 
    Bot messes up the player's win 
    and completes its own win if it
    can."""
    # If Player 1 or Bot is one move away from
    # a winning position with pattern 1.
    for piecetype in [1, 2]:
        for row in range(8):
	        for col in range(1, 9):
		        if (self.board[row, col+1] == piecetype
				        and self.board[row+1, col] == piecetype
				        and self.board[row+1, col-1] == piecetype):
                    return col
                elif (self.board[row, col] == piecetype
				        and self.board[row+1, col] == piecetype
				        and self.board[row+1, col-1] == piecetype):
                    return col+1
                elif (self.board[row, col] == piecetype
					    and self.board[row, col+1] == piecetype
					    and self.board[row+1, col-1] == piecetype):
                    return col
                elif (self.board[row, col] == piecetype
					    and self.board[row, col+1] == piecetype
					    and self.board[row+1, col] == piecetype):
                    return col-1
    # If Player 1 or Bot is one move away from
    # a winning position with pattern 2.
    for piecetype in [1, 2]:
	    for row in range(8):
		    for col in range(8):
			    if (self.board[row, col] == piecetype
					    and self.board[row, col+1] == piecetype
					    and self.board[row+1, col+1] == piecetype):
				    return col+2
                elif (self.board[row, col] == piecetype
					    and self.board[row, col+1] == piecetype
				        and self.board[row+1, col+2] == piecetype):
				    return col+1
                elif (self.board[row, col+1] == piecetype
					    and self.board[row+1, col+1] == piecetype
					    and self.board[row+1, col+2] == piecetype):
                    return col
                elif (self.board[row, col] == piecetype
					    and self.board[row+1, col+1] == piecetype
					    and self.board[row+1, col+2] == piecetype):
                    return col+1
    # If Player 1 or Bot is one move away from
    # a winning position with pattern 3
    for piecetype in [1, 2]:
        for row in range(7):
		    for col in range(9):
			    if (self.board[row, col] == piecetype
					    and self.board[row+1, col] == piecetype
					    and self.board[row+1, col+1] == piecetype):
                    return col+1
                elif (self.board[row, col] == piecetype
					    and self.board[row+1, col] == piecetype
					    and self.board[row+2, col+1] == piecetype):
                    return col+1
                elif (self.board[row+1, col] == piecetype
					    and self.board[row+1, col+1] == piecetype
					    and self.board[row+2, col+1] == piecetype):
                    return col
                elif (self.board[row, col] == piecetype
					    and self.board[row+1, col+1] == piecetype
				        and self.board[row+2, col+1] == piecetype):
                    return col
    # If Player 1 or Bot is one move away from
    # a winning position with pattern 4.
    for piecetype in [1, 2]:
	    for row in range(7):
		    for col in range(1, 10):
			    if (self.board[row, col] == piecetype
					    and self.board[row+1, col] == piecetype
						and self.board[row+1, col-1] == piecetype):
                    return col-1
                elif (self.board[row, col] == piecetype
						and self.board[row+1, col] == piecetype
						and self.board[row+2, col-1] == piecetype):
                    return col-1
                elif (self.board[row, col] == piecetype
						and self.board[row+1, col-1] == piecetype
						and self.board[row+2, col-1] == piecetype)
                    return col
                elif (self.board[row+1, col] == piecetype
						and self.board[row+1, col-1] == piecetype
						and self.board[row+2, col-1] == piecetype)
                    return col

# The move by the Bot could then, instead of randomly determined, be something like:
# col = Bot_logic(self.board)
# What do you think could it work?
# Nice comment about the Bot outsmarting the player LOL, we should keep that!