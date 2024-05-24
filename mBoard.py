
from __future__ import annotations

import enum 
from dataclasses import dataclass

from typing import *
from pieces import *

@dataclass
class Square:
    def __init__(self, coord: cord, piece: Piece):
        self.co: cord = coord
        self.piece: Piece = piece


class Board:

    
    board_letters = ['a','b','c','d','e','f','g','h']
    WHITE_PIECES = {"R", "N", "B", "Q", "K"}

    BLACK_PIECES = {"r", "n", "b", "q", "k"}
    piece_dict = {"p": Pawn, "n": Knight, "b": Bishop, "r": Rook, "q": Queen, "k": King}
    board_real = [i for i in range(64)]
    board_full = [i for i in range(128) if ((i % 16) < 8)]

    real_to_full = {k: v for k, v in zip(board_real, board_full)}
    rev_dock = {v: k for k, v in zip(board_real, board_full)}


    
    array_board = [
                    
                    ['\u265c','\u265e','\u265d','\u265b','\u265a','\u265d','\u265e','\u265c'],
                    ['\u265f','\u265f','\u265f','\u265f','\u265f','\u265f','\u265f','\u265f'],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    ['\u2659','\u2659','\u2659','\u2659','\u2659','\u2659','\u2659','\u2659'],
                    ['\u2656','\u2658','\u2657','\u2655','\u2654','\u2657','\u2658','\u2656'],                    
                ]
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
    list_board = [
                    ['R','N','B','Q','K','B','N','R'],
                    ['P','P','P','P','P','P','P','P'],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    ['p','p','p','p','p','p','p','p'],
                    ['r','n','b','q','k','b','n','r']
                    ]
    
    def __init__(self, blist: list[list[str]] | Board | None = None): # type: ignore

        self.data = []
        if blist == None:
            for y_l, i in enumerate(Board.list_board):
                tmp_l = []
                for x_l, j in enumerate(i):
                    t = " " if j == " " else Board.piece_dict[j.lower()](cord(y_l, x_l), Color.WHITE if j.isupper() else Color.BLACK)
                    tmp_l.append(t)
                self.data.append(tmp_l)


        elif isinstance(blist, list):
            pass
        elif isinstance(blist, Board):
            pass

    def __str__(self):
        print("  -----------------------------------------")
        dt = self.data.copy()
        dt.reverse()
        for m, i in enumerate(dt):
            print(str(m), end=" ")
            for n, j in enumerate(i):
                if n == 0:
                    print("| ",end="")
                if n == 7:
                    print(str(j) + "  | " + str(8 -m),end="")
                else:
                    print(str(j) + "  | " ,end="")
            print()
            print("  -----------------------------------------")
        print("    ", end="")
        for f in range(8):
            print(chr(97+f) + "    ", end="")
        return ""

def debug():
    foo = Board()
    print(foo)
if __name__ == '__main__':
    debug()