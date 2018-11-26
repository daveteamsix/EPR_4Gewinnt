import numpy as np

class Player:
	"""Creates Player Instances for the game 4-Gewinnt"""

	def __init__(self):
		self.name = "Default"
		self.piece_type = None  # Player has either 1's or 2's as pieces he throws into the board. 0's indicate empty
    
	def set_playername(self):
		"""Let's the user choose his own playernickname"""
    	pass
    
	def move(self, col):
		"""Let's the player choose the column in which he wants to put his
		piece. Then checks whether this is a valid move. If yes, it updates the
		board.
		"""
    	pass
  
class Board:
	"""Represents a board in the game 4-Gewinnt"""

  	def __init__(self):
		self.board = np.zeros((9, 10))
		

	def check_for_winning_patterns(self):
		"""Checks whether one of the players one of the four winning patterns.
		"""
	
class Game:
	"""The actual game of 4-Gewinnt"""

	def __init__(self):
		self.board = Board()	# Creates a Board for the game
		self.players = []  		# List that contains players
		self.initialize_game()	
		
	def initialize_game(self):
		"""Initialization process of the game consists of x steps:
		1. Ask whether user wants to start a Multiplayer or Singleplayer Game.
		2. Ask whether user(s) want DEFAULT playernames or want to set custom
		   nicknames.
		3. Either way, we have to ask the first player what type of piece
		   he prefers (player.piece_type). He can choose between 1 and 2. The
		   other player then get's the piece_type that is left.
		4. Starts the game.
		"""