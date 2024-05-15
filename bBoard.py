from copy import deepcopy
from typing import *
from typing import Any
class lilBoard:
    pass
class lilBoard():
    def __init__(self, bb: list[list[str]] | lilBoard) -> None:
        if isinstance(bb, lilBoard):
            self.data = deepcopy(bb.data)
        elif isinstance(bb, str):
            self.data = deepcopy(bb)
    def __getitem__(self, key: str | int, value: Any) -> str | None:
        pass
    def __setitem__(self, key: str, value: Any) -> None:
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



class lilBoard():
    def __init__(self, bb: list[list[str]]) -> None:
        self.data = deepcopy(bb)

    def __getitem__(self, key: str | int) -> str | None:
        return self.data[key]
    def __setitem__(self, key: str, value: str | int) -> None:
        self.data[key] = value

