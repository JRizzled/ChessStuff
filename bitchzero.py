

import enum 
from dataclasses import dataclass
from typing import *
from pieces import Piece, cord



@dataclass
class Square:
    def __init__(self, coord: cord, piece: Piece):
        self.co: cord = coord
        self.piece: Piece = piece




class Board:

    
    board_letters = ['a','b','c','d','e','f','g','h']
    WHITE_PIECES = {"R", "N", "B", "Q", "K"}

    BLACK_PIECES = {"r", "n", "b", "q", "k"}

    board_real = [i for i in range(64)]
    board_full = [i for i in range(128) if ((i % 16) < 8)]

    real_to_full = {k: v for k, v in zip(board_real, board_full)}
    rev_dock = {v: k for k, v in zip(board_real, board_full)}


    
    array_board = [
                    
  w
    num_board = [
                    'R','N','B','Q','K','B','N','R',
                    'P','P','P','P','P','P','P','P',
                    ' ',' ',' ',' ',' ',' ',' ',' ',
                    ' ',' ',' ',' ',' ',' ',' ',' ',
                    ' ',' ',' ',' ',' ',' ',' ',' ',
                    ' ',' ',' ',' ',' ',' ',' ',' ',
                    'p','p','p','p','p','p','p','p',
                    'r','n','b','q','k','b','n','r',
                    ]
    
    def __init__(self):
        self.array_board = Board.array_board
        self.num_board = Board.num_board
        
    def make_move(self, rank1, file1, rank2, file2):
    
        temp = self.array_board[rank1][file1]

        temp_num = (rank1 * 8) + file1

        self.array_board[rank2][file2] = temp
        self.array_board[rank1][file1] = ' '
        temp_2 = self.num_board[(rank1 * 8) + file1]
        self.num_board[(rank2 * 8) + file2] = temp_2
        self.num_board[(rank1 * 8) + file1] = ' ' 
    def conv_coord(coord):
        return (int(coord[1]) - 1, Board.board_letters.index(coord[0]))
    def coord_conv(self, coord):
        return str(self.board_letters(coord[1])) + str(8 - coord[0])
    def make_coord_move(self, cood):
        initial = Board.conv_coord(cood[0:2])
        fin = Board.conv_coord(cood[2:4])
        self.make_move(initial[0],initial[1], fin[0], fin[1])
    def is_avail(self, sq_start_num, sq_dest_num):
        sq_start_piece, sq_dest_piece = self.num_board[sq_start_num], self.num_board[sq_dest_num]
        if ((sq_start_piece in self.WHITE_PIECES) ^ (sq_dest_piece in self.WHITE_PIECES)):
            return True
        
    def legal_moves(self, sq_start_num, sq_dest_num):
        sq_start_piece = self.num_board[sq_start_num]
        sq_start_ext_num = self.real_to_full[sq_start_num]

        if (sq_start_piece.lower() == "k"):
            pass

        """ straight_check = [(1, 0,), (-1, 0), (0, 1), (0, -1)]
        diag_check = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        mv_list = []
        for i in range(8):
            for j in range(8): 
                if self.num_board[i][j] == "p":
                    if self.num_board[i+1][j] == " ":
                        if i == 1:
                            if self.num_board[i+2][j] == " ":
                                mv_list.append((i+2, j))
                        mv_list.append(i+1, j)

                if self.num_board[i][j] == "r":
                    for ch in straight_check:
                        tmp_check = ch
                        loop = True
                        while loop:
                            if i+ch[0] < 0 or j+ch[1] > 7: 
                                if self.num_board([i+ch[0],j+ch[1]]) == " ":
                                    i += ch[0]
                                    j += ch[1] 
                            else:
                                loop = False 
                if self.num_board[i][j] == "b":
                    pass 
                if self.num_board[i][j] == "k":
                    pass 
                """

    def __str__(self):
        print(" ---- ---- ---- ---- ---- ---- ---- ----")
        tmp_arr = self.array_board.copy()
        tmp_arr.reverse()
        for i in tmp_arr:
            for n, j in enumerate(i):
                if n == 0:
                    print("| ",end="")
                print(j + "  | ",end="")
            print()
            print(" ---- ---- ---- ---- ---- ---- ---- ----")
        return ""

class Game:
    
    def __init__(self) -> None:
        self.move = 0
        self.PLAYERS = 1
        self.board = Board()
        self.GAME_ON = True
        self.whiteMove = True
        


    def game_loop(self):
        
        while(self.GAME_ON):
            pass 
    def isInCheck(self):
        pass
    def getLegalMoves(self):
        pass 

    
def foo(shit):
    return shit.reverse()
    
def main():
    bitshit = Board()
    print(bitshit)
    inp = input("Coords: ")
    while inp.lower() != "quit" and inp.lower() != "exit":
        
        bitshit.make_coord_move(inp)
        print(bitshit)
        inp = input("Coords: ")
        
    

if __name__ == '__main__':
    main()
