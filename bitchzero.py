
from tkinter.ttk import PanedWindow
from pieces import *
import enum 






piece_map = {'r': Rook(False)}
class bitboard:
    board_letters = ['a','b','c','d','e','f','g','h']
    
    array_board = [
                    
                    ['\u2656','\u2658','\u2657','\u2655','\u2654','\u2657','\u2658','\u2656'],                    
                    ['\u2659','\u2659','\u2659','\u2659','\u2659','\u2659','\u2659','\u2659'],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    ['\u265f','\u265f','\u265f','\u265f','\u265f','\u265f','\u265f','\u265f'],
                    ['\u265c','\u265e','\u265d','\u265b','\u265a','\u265d','\u265e','\u265c']
                    ]
    num_board = [
                    'r','n','b','q','k','b','n','r',
                    'p','p','p','p','p','p','p','p',
                    ' ',' ',' ',' ',' ',' ',' ',' ',
                    ' ',' ',' ',' ',' ',' ',' ',' ',
                    ' ',' ',' ',' ',' ',' ',' ',' ',
                    ' ',' ',' ',' ',' ',' ',' ',' ',
                    'P','P','P','P','P','P','P','P',
                    'R','N','B','Q','K','B','N','R'
                    ]
    
    def __init__(self):
        self.array_board = bitboard.array_board
        self.num_board = bitboard.num_board
        
    def make_move(self, rank1, file1, rank2, file2):
    
        temp = self.array_board[rank1][file1]
        self.array_board[rank2][file2] = temp
        self.array_board[rank1][file1] = ' '
        temp_2 = self.num_board[(rank1 * 8) + file1]
        self.num_board[(rank2 * 8) + file2] = temp_2
        self.num_board[(rank1 * 8) + file1] = ' ' 
    def conv_coord(coord):
        return (8 - int(coord[1]), bitboard.board_letters.index(coord[0]))
    def coord_conv(self, coord):
        return str(self.board_letters(coord[1])) + str(8 - coord[0])
    def make_coord_move(self, cood):
        initial = bitboard.conv_coord(cood[0:2])
        fin = bitboard.conv_coord(cood[2:4])
        self.make_move(initial[0],initial[1], fin[0], fin[1])

    def legal_moves(self):
        straight_check = [(1, 0,), (-1, 0), (0, 1), (0, -1)]
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
               

    def __str__(self):
        print(" ---- ---- ---- ---- ---- ---- ---- ----")
        
        for i in self.array_board:
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
        self.board = bitboard()
        self.GAME_ON = True
        self.whiteMove = True
        


    def game_loop(self):
        
        while(self.GAME_ON):
            pass 
    def isInCheck(self):
        pass
    def getLegalMoves(self):
        pass 

    

def main():
    bitshit = bitboard()
    print(bitshit)
    inp = input("Coords: ")
    while inp.lower() != "quit" and inp.lower() != "exit":
        
        bitshit.make_coord_move(inp)
        print(bitshit)
        inp = input("Coords: ")
        
    

if __name__ == '__main__':
    main()
