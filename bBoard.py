from copy import deepcopy
from typing import *
""" 
class lilArray:
    pass 
class lilBoard:
    pass """

class lilArray():
    def __init__(self, l: list[str]) -> None:
        self.data = deepcopy(l)
    def __getitem__(self, key: str | int | int):
        if type(key) == int:
            if key in range(7):
                return self.data[key]
            else:
                return None
    def __setitem__(self, key: str, value: str) -> None:
            pass

class lilBoard():
    def __init__(self, bb: list[list[str]] | list[lilArray]) -> None:
        if isinstance(bb, lilBoard):
            self.data = deepcopy(bb.data)
        elif isinstance(bb, str):
            self.data = deepcopy(bb)
    def __getitem__(self, key: str) -> str | None:
        pass
    def __setitem__(self, key: str | int, value: str) -> None:
        pass


def stuff(a: lilBoard):
    pass
num_board = [
                ['R','N','B','Q','K','B','N','R'],
                ['P','P','P','P','P','P','P','P'],
                [' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' '],
                ['p','p','p','p','p','p','p','p'],
                ['r','n','b','q','k','b','n','r']
                ]



