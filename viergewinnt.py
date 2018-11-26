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

class Board:
	"""Represents a (9 X 10) board in the game"""

	def __init__(self):
		self.board = np.zeros((9, 10))

	def check_for_winning_patterns(self):
		"""Checks whether one of the players has one of the four winning
		patterns.
		"""
		pass

	def show(self):
		"""Prints the current board into the console"""
		print(self.board)
	

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

	def start_game(self):
		
	
		




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
		