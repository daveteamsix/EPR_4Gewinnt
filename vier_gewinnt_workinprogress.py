import numpy as np
from string import ascii_letters

class Player:
	"""Creates Player Instances for the game 4-Gewinnt."""

	def __init__(self):
		self.name = "Default"
		self.piece_type = None

	def set_playername(self):
		"""Let's the player pick his own Nickname"""
		name = input("What name do you want to give yourself? " + 
					 "(between 4 and 20 characters; only ASCII-Letters): ")
		
		isAscii = [True for letter in name if letter in ascii_letters]
		while (len(name)>20 or len(isAscii) != len(name)):
			print("Sorry. Try again.")
			name = input("What name do you want to give yourself? " + 
					 	"(between 4 and 20 characters; only ASCII-Letters): ")
			isAscii = [True for letter in name if letter in ascii_letters]
		
		self.name = name

	def move(self, col):
		"""Let's the player choose the column in which he wants to put his
		piece. Then checks whether this move is valid. If yes, it updates
		the board.
		"""
		

	def piece_type(self):



class Board:
	"""Represents a (9 X 10) board in the game"""

	def __init__(self):
        """ We need to flip the board if we want the pieces to go to the loweat row"""
		self.board = np.zeros((9, 10))


	def show(self):
		"""Prints the current board into the console"""
		print(np.flip(self.board, 0))


class MultiplayerGame:
	"""The actual game of 4-Gewinnt."""

	def __init__(self):
		self.board = Board()
		self.players = []
		self.set_player_names()
		self.start_game()

	def set_player_names(self):
		"""Let's user decide whether he wants to choose custom nicknames. If
		he doesn't, we produce default names 'Player1' and 'Player2' """
		print("Do you want custom nicknames?")
		FLAG = True
		VALID_INPUTS = ["Y", "N"]
		while FLAG:
			WANTS_NICKNAMES = input("Type Y for Yes, and N for No: ")
			if WANTS_NICKNAMES in VALID_INPUTS:
				FLAG = False
		
		player1 = Player()
		player2 = Player()

		player1.piece_type = 1  # Zeros in the np.array indicate empty fields
		player2.piece_type = 2  

		if WANTS_NICKNAMES == "Y":
			player1.set_playername()
			player2.set_playername()

		else:
			player1.name = "Player 1"
			player2.name = "Player 2"
		
		self.players = [player1, player2]

# Instead of the incorrect Player.piece_type would this work?: self.players.piece_type  ? Provided that we keep
# it in this class. These criteria for the winning patterns are not the most elegant way to code it, but that's all
# I could come up with for now. The method would have to have the player's piece types as an additional argument, the
# below shown way (self, piece_type) being incorrect.  
# What do you think? Can you find a way to integrate the general logic with the architecture of the various classes?
	def checks_for_winning_patterns(self, piece_type):
        # First winning pattern.
        for r in range(NUMBER_ROWS-1):
            for c in range(NUMBER_COLUMNS-2):
                if (self.board[r][c] == Player.piece_type and self.board[r][c+1] == Player.piece_type and
                    self.board[r+1][c+1] == Player.piece_type and self.board[r+1][c+2] == Player.piece_type):
                    return True

        # Second winning pattern.
        for r in range(1, NUMBER_ROWS):
        	for c in range(NUMBER_COLUMNS-2):
        		if (self.board[r][c]== Player.piece_type and self.board[r][c+1] == Player.piece_type and
        			self.board[r-1][c+1] == Player.piece_type and self.board[r-1][c+2] == Player.piece_type):
        			return True

        #Third winning pattern.
        for r in range(2, NUMBER_ROWS+1):
        	for c in range(NUMBER_COLUMNS-1):
        		if (self.board[r][c] == Player.piece_type and self.board[r-1][c] == Player.piece_type and
        			self.board[r-1][c+1] == Player.piece_type and self.board[r-2][c+1] == Player.piece_type):
        			return True

        #Fourth winning pattern.
        for r in range(NUMBER_ROWS-2):
        	for c in range(NUMBER_COLUMNS-1):
        		if (self.board[r][c] == Player.piece_type and self.board[r+1][c] == Player.piece_type and
        			self.board[r+1][c+1] == Player.piece_type and self.board[r+2][c+1] == Player.piece_type):
        			return True




# In order to see if a move is valid the top row of the column has to be a 0. So the method return either True
# or False. col refers to the column the player selected in his move. It would probably be player1.move / player2.move 
# the above move method returns a number for col, so maybe col = player1.move etc. ??
    def checks_move_validity(self, board, col):
    	return board[8][col] == 0
# If the column is not full yet and the move therefore valid, this function finds the correctt row for the player piece.
# col is the selected move by the player. The function checks from the lowest row up and returns the first empty row spot.
    def finds_row_for_piece(self, board, col):
    	for r in range(NUMBER_ROWS):
    		if board[r][col] == 0:
    			return r
# Finally the function that fills in the player piece into the correct spot. The piece argument would then be either 1 or 0.
	def fills_in_piece(self, board, row, col, piece):
		board[row][col] == piece
# So a player move could look like:
	if checks_move_validity(board, col):
		row = finds_row_for_piece(board, col)
		fills_in_piece(board, row, col, piece)

# This is only an idea for how a move could work. If you have a better way to implement it, I think we should go with your
# way of implementing. 
# Of course the functions would still need to go in the right class(es) and have the correct arguments. Do you think you could
# help with that?  



	def start_game(self):
		pass
	
		




###############################################################################
	# def set_game_mode(self):
	# 	print("Do you want to play in Singleplayer or Multiplayer-Mode?")
	# 	FLAG = True
	# 	VALID_INPUTS = ["S", "M"]
	# 	while FLAG:
	# 		GAME_MODE = input("Type S for Singleplayer or M for Multiplayer: ")
	# 		if GAME_MODE in VALID_INPUTS:
	# 			FLAG = False

	# 	if GAME_MODE == "M":  # User chose Singleplayer Mode
	# 		self.start_multiplayer()	