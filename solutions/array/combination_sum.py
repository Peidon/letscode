from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.n = 0
        self.candidates = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.n = len(candidates)
        self.candidates = candidates

        self.dfs(0, target, [])
        return self.ans

    def dfs(self, i: int, c: int, path: List[int]):

        p = path[:]
        if c == 0:
            self.ans.append(p)
            return

        if i == self.n:
            return

        if c < self.candidates[i]:
            return

        for j in range(i, self.n):
            if j > i and self.candidates[j] == self.candidates[j-1]:
                continue

            p.append(self.candidates[j])
            self.dfs(j+1, c - self.candidates[j], p)
            p.pop()
