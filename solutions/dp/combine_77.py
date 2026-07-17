from typing import List


class Solution:
    """
    n=1, k=1
    [[1]]

    n=2, k=2
    [[1,2]]

    n=3, k=2
    [[1,3], [2,3], [1,2]] = [*f(2,1), 3]  and f(2,2)

    n=4, k=2
    [*f(3,1), 4] and f(3,2)

    """

    def combine(self, n: int, k: int) -> List[List[int]]:

        if k == 0:
            return []

        if k == 1:
            return [[x] for x in range(1, n + 1)]

        sublist = self.combine(n - 1, k - 1)
        result = [[*comb, n] for comb in sublist]

        if n - k >= 1:
            sub = self.combine(n - 1, k)
            result.extend(sub)
        return result