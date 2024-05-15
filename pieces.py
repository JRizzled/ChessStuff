import enum 
import collections 
from typing import *



class Color(enum.Flag):
	WHITE = enum.auto()
	BLACK = enum.auto()

WHITE = Color.WHITE
BLACK = Color.BLACK

class Piece:
	def __init__(self, sd = WHITE):
		self.isAttacking: list[Piece] = []
		self.isAttackedBy: list[Piece] = []
		self.coord = []
		self.Side: Color =  sd
	def get_moves():
		pass

class Pawn(Piece):
	def __init__(self, w = True) -> None:
		Piece.__init__(self, w)
    
class King(Piece):
	def __init__(self, w = True) -> None:
		Piece.__init__(self, w)

class Knight(Piece):
	def __init__(self, w = True) -> None:
		Piece.__init__(self, w)

class Bishop(Piece):
	def __init__(self, w = True) -> None:
		Piece.__init__(self, w)

class Rook(Piece):
	def __init__(self, w = True) -> None:
		Piece.__init__(self, w)

class Queen(Piece):
	def __init__(self, w = True) -> None:
		Piece.__init__(self, w)

class King(Piece):
	def __init__(self, w = True) -> None:
		Piece.__init__(self, w)

pieceDict = {""}