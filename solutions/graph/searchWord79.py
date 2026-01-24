import unittest
from typing import List


class Helper:
    def __init__(self, board: List[List[str]], word: str):
        self.B = board
        self.W = word
        self.L = len(word) - 1
        self.M = len(board)
        self.N = len(board[0])
        self.bm = [[False] * self.N for _ in range(self.M)]

    def find(self, k: int, i: int, j: int) -> bool:
        """
        To find kTH character of the word, when at position board[i][j]
        """
        if i < 0 or j < 0 or i == self.M or j == self.N:
            return False

        if self.bm[i][j]:
            return False

        if self.B[i][j] == self.W[k] and k == self.L:
            return True

        if self.B[i][j] == self.W[k]:

            self.bm[i][j] = True

            if self.find(k + 1, i + 1, j):
                return True

            if self.find(k + 1, i, j + 1):
                return True

            if self.find(k + 1, i - 1, j):
                return True

            if self.find(k + 1, i, j - 1):
                return True

        self.bm[i][j] = False
        return False


def exist(board: List[List[str]], word: str) -> bool:
    h = Helper(board, word)
    for i in range(h.M):
        for j in range(h.N):

            if h.find(0, i, j):
                return True

    return False

class TestExist(unittest.TestCase):

    def test0(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        self.assertTrue(exist(board, word))

    def test1(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        self.assertFalse(exist(board, word))