import unittest
from enum import Enum
from typing import List

class Symbol(Enum):
    water = '0'
    land = '1'
    marked = '2'


class Earth:

    def __init__(self, grid: List[List[str]]):
        self.grid = grid
        self.M = len(grid)
        self.N = len(grid[0])

    def search_land(self, i:int, j:int) -> bool:
        if i < 0 or j < 0 or i == self.M or j == self.N:
            return False

        if self.grid[i][j] == Symbol.land.value:
            self.grid[i][j] = Symbol.marked.value

            self.search_land(i + 1, j)
            self.search_land(i - 1, j)
            self.search_land(i, j + 1)
            self.search_land(i, j - 1)
            return True

        return False




def numIslands(grid: List[List[str]]) -> int:
        e = Earth(grid)
        n = 0
        for i in range(e.M):
            for j in range(e.N):
                if e.search_land(i, j):
                    n+=1
        return n


class LandTest(unittest.TestCase):

    def test_num(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]

        self.assertEqual(1,numIslands(grid))