from typing import Any


board_real = [i for i in range(64)]
board_full = [i for i in range(128) if ((i % 16) < 8)]

real_to_full = {k: v for k, v in zip(board_real, board_full)}
rev_dock = {v: k for k, v in zip(board_real, board_full)}



class Board:
    def __init__(self) -> None:
        pass
def main():
    pass
if __name__ == "__main__":
    main()