import numpy as np
from string import ascii_letters
import os
import external_code as ext
from time import sleep

class Player:
	"""Creates Player Instances for the game 4-Gewinnt."""

	def __init__(self):
		self.NAME = "Default"
		self.PIECE_TYPE = None  # A player can either have 1's or 2's as pieces

	def set_playername(self):
		"""Let's the player pick his own Nickname"""
		print("What name do you want to give yourself?")
		print("(Between 4-20 Characters. Only ASCII-Letters allowed.)")
		name = input("Name: ")

		# Check if the input is within the constraints
		isAscii = [True for letter in name if letter in ascii_letters]
		while (len(name) > 20 or len(isAscii) != len(name)):
			print("Sorry. Try again.")
			name = input("Name: ")
			isAscii = [True for letter in name if letter in ascii_letters]

		self.NAME = name
	

	def bot_move(self, board):
		"""The bot tries to complete its own win if it can, while also trying
		to mess up the opponent's winning-pattern (if he's one step away
		at building one)
		"""
		# If Human or Bot is one move away from a winning position with pattern
		# 1, the bot tries to place its piece either to mess up the human's
		# winning position, or tries to win by finalizing his own pattern.
		# Winning Pattern 1:
		#	 X* X
		# X  X
		for piece in [1, 2]:
			for row in range(8):
				for col in range(1,9):
					# Center piece is missing (SUCCESSFULLY TESTED)
					if (board[row, col+1] == piece
							and board[row+1, col] == piece
							and board[row+1, col-1] == piece
                            and board[row, col] == 0):
						return col
					# Rightmost piece is missing
					elif (board[row, col] == piece
							and board[row+1, col] == piece
							and board[row+1, col-1] == piece
							and board[row+1, col+1] != 0
                            and board[row, col+1] == 0):
						return col+1
					# Leftmost piece is missing
					elif (board[row, col] == piece
							and board[row, col+1] == piece
							and board[row+1, col] == piece
                            and board[row+1, col-1] == 0):
						return col-1
		
		# Analogously winning pattern 2:
		#  X* X 
		#     X X
		for piece in [1, 2]:
			for row in range(8):
				for col in range(8):
					# Rightmost piece is missing
					if (board[row, col] == piece
							and board[row, col+1] == piece
							and board[row+1, col+1] == piece
                            and board[row+1, col+2] == 0):
						return col+2
					# Center piece is missing
					elif (board[row, col] == piece
							and board[row+1, col+2] == piece
							and board[row+1, col+1] == piece
                            and board[row, col+1] == 0):
						return col+1
					# Leftmost piece is missing
					elif (col >= 1
							and board[row, col] == piece
							and board[row+1, col] == piece
							and board[row+1, col+1] == piece
							and board[row+1, col-1] != 0):
						return col-1
		
		# Analogously winning pattern 3
		#   X* 
		#   X X
		#	  X
		for piece in [1, 2]:
			for row in range(7):
				for col in range(9):
					# Rightmost piece is missing, Tested
					if (board[row, col] == piece
						and board[row+1, col] == piece
						and board[row+2, col+1] == piece
                        and board[row+1, col+1] == 0):
						return col+1
					# Leftmost piece is missing, Tested
					if (board[row, col] == piece
						and board[row, col+1] == piece
						and board[row+1, col+1] == piece
                        and board[row+1, col] == 0):
						return col
                    # Top piece is missing, Tested
                    if (board[row, col+1] == piece
                        and board[row+1, col+1] == piece
                        and board[row+2, col+1] == piece
                        and board[row, col] == 0):
                        return col
		
		# Analogously winning pattern 4
		#  	X*
		# X X
		# X
		for piece in [1, 2]:
			for row in range(7):
				for col in range(1, 10):
					# Leftmost piece is missing, Tested
					if (board[row, col] == piece
							and board[row+1, col] == piece
							and board[row+2, col-1] == piece
                            and board[row+1, col-1] == 0):
						return col-1
					# Rightmost piece is missing, Tested
					if (board[row, col] == piece
							and board[row, col-1] == piece
							and board[row+1, col-1] == piece
                            and board[row+1, col] == 0):
						return col
		
		# If there is no winning pattern to complete, pick a random column
		# return np.random.randint(0, 10)
		return 0
						
					

class Board:
	"""Represents a (9 X 10) board in the game"""

	def __init__(self):
		self.board = np.zeros((9, 10), dtype=np.int_)

	def check_for_winning_patterns(self):
		"""Checks whether one of the players has one of the four winning
		patterns. Returns the piecetype {1,2} of the winner."
		"""
		# Winning Pattern 1:
		#    X X
		#  X X
		for piecetype in [1, 2]:
			for row in range(8):
				for col in range(1, 9):
					if (self.board[row, col] == piecetype
							and self.board[row, col+1] == piecetype
							and self.board[row+1, col] == piecetype
							and self.board[row+1, col-1] == piecetype):
						return piecetype

		# Second winning pattern:
		#	X X
		#	  X X
		for piecetype in [1, 2]:
			for row in range(8):
				for col in range(8):
					if (self.board[row, col] == piecetype
							and self.board[row, col+1] == piecetype
							and self.board[row+1, col+1] == piecetype
							and self.board[row+1, col+2] == piecetype):
						return piecetype

		# Third winning pattern:
		#	X
		#   X X
		#	  X
		for piecetype in [1, 2]:
			for row in range(7):
				for col in range(9):
					if (self.board[row, col] == piecetype
							and self.board[row+1, col] == piecetype
							and self.board[row+1, col+1] == piecetype
							and self.board[row+2, col+1] == piecetype):
						return piecetype

		# Fourth winning pattern:
		# 		X
		#	  X X
		#	  X
		for piecetype in [1, 2]:
			for row in range(7):
				for col in range(1, 10):
					if (self.board[row, col] == piecetype
							and self.board[row+1, col] == piecetype
							and self.board[row+1, col-1] == piecetype
							and self.board[row+2, col-1] == piecetype):
						return piecetype

	def check_for_draw(self):
		""" Checks for a draw. A draw happens when the board is full and 
		nobody has had a winning pattern. Returns True if the board is full,
		False otherwise.
		"""
		# A Board is considered full when the top-row is full with pieces
		if (self.board[0, 0] != 0 
		and self.board[0, 1] != 0 
		and self.board[0, 2] != 0 
		and self.board[0, 3] != 0 
		and self.board[0, 4] != 0 
		and self.board[0, 5] != 0 
		and self.board[0, 6] != 0 
		and self.board[0, 7] != 0 
		and self.board[0, 8] != 0 
		and self.board[0, 9] != 0):
			return True
		else:
			return False

	def show(self):
		"""Prints the current board into the console."""
		ext.matprint(self.board)
		
	
	def is_valid_move(self, col):
		"""Checks whether putting a piece in column with index col is 
		a valid move. It is valid, if in the chosen column is at least one 
		zero at the top.
		"""
		if self.board[0, col] == 0:  # Move is valid
			return True
		else:
			return False
	
	def play_move(self, col, piecetype):
		"""Plays the piecetype (argument) into the given column (argument).
		The piece keeps falling down the board, until it hits another piece.
		"""
		row = 0
		while self.board[row, col] == 0:
			# If we are in the last row, then we have to put the piece there.
			if (row+1) == 9:
				self.board[row, col] = piecetype
			# If there exists a next row, and this next row has a piece (!= 0)
			# then we have to stop and put the piece into the current row.
			elif self.board[row+1, col] != 0:
				self.board[row, col] = piecetype
			else:
				row += 1
			

class MultiplayerGame:
	"""The PLAYER vs PLAYER (Multiplayer) version of 4-Gewinnt."""

	def __init__(self):
		self.PLAYERS = []		# Setup a list that contains all players
		self.WINNER = None		# Player object => The winning player
		
		self.board = Board()	# First we create the board
		self.set_player_names()	# Initiate customized player names
		self.start_game()		# starts the main game-loop

	def winning_screen(self, player):
		"""Prints a winning screen into the console."""
		os.system('cls')
		print("\n")
		print("---------------------------------------------------")
		print("\t CONGRATULATIONS, {}".format(player.NAME))
		print("\t YOU HAVE WON!")
		print("---------------------------------------------------")
		print("\n")
		INPUT = input("Press ENTER to exit.")
		exit()


	def console_layout(self, player):
		"""The game interface a player sees at each round."""
		os.system('cls')
		print("---------------------------------------------------")
		print("\t\t\t\t [E]xit ")
		print("---------------------------------------------------")
		print("\t\tTHE CURRENT BOARD  ")
		print("--------------------------------------------------- \n")
		ext.matprint(self.board.board)
		print("---------------------------------------------------")
		print(" {}'s TURN".format(player.NAME))
		print(" PIECE TYPE: {}".format(player.PIECE_TYPE))
		print("---------------------------------------------------")
		print("\t\tCHOOSE A COLUMN INDEX")
		print("---------------------------------------------------")
		print("    [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] \n")
		print("    Note: Type in the Integer, then press ENTER")
		print("---------------------------------------------------")


	def set_player_names(self):
		"""Let's user decide whether he wants to choose custom nicknames. If
		he doesn't, we produce default names 'Player1' and 'Player2'.
		 """
		os.system('cls')
		print("\n")
		print("\t\t\t\t\t [E]xit")
		print("---------------------------------------------------")
		print("\t MULTI-PLAYER MODE")
		print("---------------------------------------------------")
		print("Do you want custom nicknames?")
		FLAG = True
		VALID_INPUTS = "YNEyne"
		while FLAG:
			WANTS_NICKNAMES = input("[Y]/[N]: ")
			if WANTS_NICKNAMES in VALID_INPUTS:
				FLAG = False
		
		# User wants to exit the game
		if WANTS_NICKNAMES in "eE":
			exit()
		
		player1 = Player()
		player2 = Player()

		player1.PIECE_TYPE = 1  
		player2.PIECE_TYPE = 2  

		if WANTS_NICKNAMES in "Yy":
			os.system('cls')
			print("\n")
			print("Player 1:")
			player1.set_playername()
			print("\n")
			print("Player 2: \n")
			player2.set_playername()

		else:
			player1.NAME = "Player 1"
			player2.NAME = "Player 2"
		
		self.PLAYERS = [player1, player2]

	def start_game(self):
		# Start with player 1
		curr_player_idx = 0
		winner = False

		while not winner:
			# Select the player whose turn it is via his player-list-index.
			curr_player = self.PLAYERS[curr_player_idx]
			
			# Print the game interface to console.
			self.console_layout(curr_player)

			# Ask player in which column he wants to put his next piece. Check
			# whether this input is in the range of column indexes (0-9)
			FLAG = True 
			while FLAG:
				col = input("ACTION: ")
				if col in [str(i) for i in range(10)]:
					col = int(col)
					# Further check if column isn't full
					if self.board.is_valid_move(col):
						FLAG = False
					else:  # Column is full. The user has to choose another idx
						self.console_layout(curr_player)
						print("Invalid input. Try again.")
				elif col in ["E", "e"]:  # User wants to exit
					exit()
				else: 
					self.console_layout(curr_player)
					print("Invalid input. Try again.")
			col = int(col)
			
			# If the user has chosen a valid move, we are ready to play it.
			self.board.play_move(col, curr_player.PIECE_TYPE)

			# Check if the move led to a win of for the current player
			winning_pieces = self.board.check_for_winning_patterns()
			if (winning_pieces == 1 or winning_pieces == 2):
				winner = True
				if winning_pieces == 1:
					winner_player = self.PLAYERS[0]
					self.winning_screen(winner_player)
				elif winning_pieces == 2:
					WINNER_player = self.player[1]
					self.winning_screen(WINNER_player)

			# Check if the move led to a draw (board full with pieces)
			is_draw = self.board.check_for_draw()
			if is_draw:
				os.system('cls')
				print("\n")
				print("----------------------------------------------")
				INPUT = input("The game ended in a draw. Press any key to exit")
				print("----------------------------------------------")
				exit()

			# If nobody won, update the player idx
			curr_player_idx += 1
			if curr_player_idx == 2:  # return back to player 1
				curr_player_idx = 0
			

class SingleplayerGame:

	def __init__(self):
		self.board = Board()
		self.PLAYERS = []
		
		self.initialize()
		self.start_game()  # analog zu MultiplayerGame

	def console_layout(self, player):
		"""The game interface a player sees at each round."""
		os.system('cls')
		print("---------------------------------------------------")
		print("\t\t\t\t [E]xit ")
		print("---------------------------------------------------")
		print("\t\tTHE CURRENT BOARD  ")
		print("--------------------------------------------------- \n")
		ext.matprint(self.board.board)
		print("---------------------------------------------------")
		print(" {}'s TURN".format(player.NAME))
		print(" PIECE TYPE: {}".format(player.PIECE_TYPE))
		print("---------------------------------------------------")
		print("\t\tCHOOSE A COLUMN INDEX")
		print("---------------------------------------------------")
		print("    [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] \n")
		print("    Note: Type in the Integer, then press ENTER")
		print("---------------------------------------------------")

	def initialize(self):
		"""Initializes the Single-Player game by setting up all the variables
		needed for playing. For example, setting custom player name.
		"""
		os.system('cls')
		print("\n")
		print("\t\t\t\t\t\t [E]xit")
		print("---------------------------------------------------")
		print("\t SINGLE-PLAYER MODE")
		print("---------------------------------------------------")
		print("Human, do you want a custom nickname?")

		FLAG = True
		VALID_INPUTS = "YNEyne"
		while FLAG:
			WANTS_NICKNAMES = input("[Y]/[N]: ")
			if WANTS_NICKNAMES in VALID_INPUTS:
				FLAG = False

		# User wants to exit the game
		if WANTS_NICKNAMES in "eE":
			exit()
		
		player1 = Player()
		player2 = Player()
		player2.NAME = "Bot"

		player1.PIECE_TYPE = 1  
		player2.PIECE_TYPE = 2  

		if WANTS_NICKNAMES in "Yy":
			os.system('cls')
			print("\n")
			print("Player 1:")
			player1.set_playername()
			print("\n")
		
		else:
			player1.NAME = "Player 1"
		
		self.PLAYERS = [player1, player2]

	def winning_screen(self, player):
		"""Prints a winning screen into the console."""
		os.system('cls')
		print("\n")
		print("---------------------------------------------------")
		print("\t CONGRATULATIONS, {}".format(player.NAME))
		print("\t YOU HAVE WON!")
		print("---------------------------------------------------")
		print("\n")
		INPUT = input("Press ENTER to exit.")
		exit()

	def start_game(self):
		""" This plays the actual game """
		curr_player_idx = 0
		winner = False
		
		while not winner:
			curr_player = self.PLAYERS[curr_player_idx]

			# HUMAN ACTION
			if curr_player_idx == 0:  # Then it's the human's turn
				self.console_layout(curr_player)
				# Ask player in which column he wants to put his next piece. Check
				# whether this input is in the range of column indexes (0-9)
				FLAG = True 
				while FLAG:
					col = input("ACTION: ")
					if col in [str(i) for i in range(10)]:
						col = int(col)
						# Further check if column isn't full
						if self.board.is_valid_move(col):
							FLAG = False
						else:  # Column is full. The user has to choose another idx
							self.console_layout(curr_player)
							print("Invalid input. Try again.")
					elif col in ["E", "e"]:  # User wants to exit
						exit()
					else: 
						self.console_layout(curr_player)
						print("Invalid input. Try again.")
				col = int(col)
				
			# BOT ACTION
			elif curr_player_idx == 1:
				flag = True
				while flag:
					col = curr_player.bot_move(self.board.board)
				
					# Check if column is full
					if self.board.is_valid_move(col):
						flag = False
				
				# Pause the screen, to give the human a visual clue that the bot
				# made a move
				os.system('cls')
				print("\n")
				print("-------------------------------------------------")
				print(" THE BOT IS CHOOSING HIS MOVE")
				print(" Please wait while he is outsmarting you.")
				print("-------------------------------------------------")
				# sleep(1)

			# If the move is valid, we are ready to play it with the 
			# respective player's piece_type
			self.board.play_move(col, curr_player.PIECE_TYPE)

			# Check if the move led to a win of for the current player
			winning_pieces = self.board.check_for_winning_patterns()
			if (winning_pieces == 1 or winning_pieces == 2):
				winner = True
				if winning_pieces == 1:
					winner_player = self.PLAYERS[0]
					self.winning_screen(winner_player)
				elif winning_pieces == 2:
					WINNER_player = self.player[1]
					self.winning_screen(WINNER_player)

			# Check if the move led to a draw (board full with pieces)
			is_draw = self.board.check_for_draw()
			if is_draw:
				os.system('cls')
				print("\n")
				print("----------------------------------------------")
				INPUT = input("The game ended in a draw. Press any key to exit")
				print("----------------------------------------------")
				exit()

			# If nobody won, update the player idx
			curr_player_idx += 1
			if curr_player_idx == 2:  # return back to player 1
				curr_player_idx = 0

#######################################################
### Outside Loop
#######################################################

def main():
	print("\n")
	print("\n")
	print("---------------------------------------------------")
	print("Welcome to a game of 4-Gewinnt - Special Version")
	print("---------------------------------------------------")
	print("Choose one of the following options:\n")
	print("[S]ingleplayer 4-Gewinnt (you versus computer)")
	print("[M]ultiplayer 4-Gewinnt (you versus friend")
	print("[E]xit")
	print("---------------------------------------------------")
	print("\n")

	VALID_INPUTS = "SMEsme"
	flag = True
	while flag:
		INPUT = input("Action: ")
		if INPUT in VALID_INPUTS:
			flag = False
	
	if INPUT in "Ss":
		SingleplayerGame()
	elif INPUT in "Mm":
		MultiplayerGame()
	elif INPUT in "Ee":
		exit()


main()
