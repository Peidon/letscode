from typing import List


class Helper:
    def __init__(self, board: List[List[str]], word: str):
        self.B = board
        self.W = word
        self.L = len(word) - 1
        self.M = len(board)
        self.N = len(board[0])

    def find(self, k: int, i: int, j: int, b: List[List[bool]]) -> bool:
        if i < 0 or j < 0 or i == self.M or j == self.N:
            return False

        if b[i][j]:
            return False

        if self.B[i][j] == self.W[k] and k == self.L:
            return True

        if self.B[i][j] == self.W[k]:

            b[i][j] = True

            if self.find(k + 1, i + 1, j, b):
                return True

            if self.find(k + 1, i, j + 1, b):
                return True

            if self.find(k + 1, i - 1, j, b):
                return True

            if self.find(k + 1, i, j - 1, b):
                return True

        b[i][j] = False
        return False


def exist(board: List[List[str]], word: str) -> bool:
    h = Helper(board, word)
    for i in range(h.M):
        for j in range(h.N):
            b = [[False] * h.N for _ in range(h.M)]
            if h.find(0, i, j, b):
                return True
    return False