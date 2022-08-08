



class Piece:
	def __init__(self, w = True):
		self.isAttacking = []
		self.isAttackedBy = []
		self.coord = []
		self.WHITE = w 
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

