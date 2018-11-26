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

class Game:
	"""The actual game of 4-Gewinnt."""

	def __init__(self):
		self.board = Board()
		self.players = []
		self.initialize_game()

	def initialize_game(self):
		"""Initialization process consists of the following steps:

		1. Ask if user wants to play Multiplayer or Singleplayer game.float
		2. Ask user if he wants to customize Nicknames. Otherwise generate
		   default names.
		3. Ask user what piece type he wants (player.piece_type). This can be
		   either 1's or 2's (zeros on the board represent empty fields).
		4. Start the game.
		"""
		