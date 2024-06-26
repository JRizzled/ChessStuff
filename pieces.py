#numpy/numpy/_core/src/multiarray/arrayobject.c

from __future__ import annotations
import numpy as np
import enum 
from collections import namedtuple
from typing import *
from dataclasses import dataclass
import sys


try:
	from mBoard import Board
except Exception as e:
	pass


Cord = lambda x, y : np.array([x,y]) if 0 <= x <= 7 and 0 <= y <= 7 else None


class cord():
	def __init__(self, y, x) -> None:
		self.y: int = y
		self.x: int = x

class Color(enum.Flag):
	WHITE = enum.auto()
	BLACK = enum.auto()

class Space(enum.Enum):
	FRIEND = enum.auto()
	FOE = enum.auto()
	EMPTY = enum.auto()

@dataclass
class Move:
	init_cord: cord 
	fin_cord: cord
	capture_move: bool
	castle_move: bool 
	

WHITE: Color = Color.WHITE
BLACK: Color = Color.BLACK
side_switch = namedtuple("side_switch", ["back_mult", "col", "row" ])




class Piece:
	def __init__(self, place: cord, sd: Color = WHITE):
		self.Side: Color =  sd
		self.coord: cord = cord(place.y, place.x)
		self.isAttacking: list[Piece] = []
		self.isAttackedBy: list[Piece] = []
	def get_moves(self):
		pass
	def get_threats(self):
		pass
	def isAvail(self):
		pass
class Pawn(Piece):
	#ss = (Side: (second_row, prom_row, mult))
	ss: dict[Color: tuple[int]] = {WHITE : (6,0, -2), BLACK : (1, 7, 2)}

	def __init__(self, place: cord, sd = WHITE) -> None:
		Piece.__init__(self, place, sd)
		self.switch = Pawn.ss[self.Side]
	
	def __str__(self) -> str:
		return "\u265f" if self.Side == WHITE else "\u2659"

	def get_moves(self, b: Board):
		tmp_pos = cord(self.coord.y, self.coord.x)
		tmp_init = [self.coord.y, self.coord.x]
		if tmp_init[0] == self.switch[0]:
			tmp_new = [tmp_init[0] + self.switch[2], tmp_init[1]]
			 


class King(Piece):
	def __init__(self, place: cord, sd = WHITE) -> None:
		Piece.__init__(self, place, sd)
	
	def __str__(self) -> str:
		return "\u265a" if self.Side == WHITE else "\u2654"

class Knight(Piece):
	def __init__(self, place: cord, sd = WHITE) -> None:
		Piece.__init__(self, place, sd)
	
	def __str__(self) -> str:
		return "\u265e" if self.Side == WHITE else "\u2658"

class Bishop(Piece):
	def __init__(self, place: cord, sd = WHITE) -> None:
		Piece.__init__(self, place, sd)
	
	def __str__(self) -> str:
		return "\u265d" if self.Side == WHITE else "\u2657"

class Rook(Piece):
	def __init__(self, place: cord, sd = WHITE) -> None:
		Piece.__init__(self, place, sd)
	
	def __str__(self) -> str:
		return "\u265c" if self.Side == WHITE else "\u2656"

class Queen(Piece):
	def __init__(self, place: cord, sd = WHITE) -> None:
		Piece.__init__(self, place, sd)
	
	def __str__(self) -> str:
		return "\u265b" if self.Side == WHITE else "\u2655"