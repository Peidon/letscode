from typing import List


def _maxProfit(prices: List[int]) -> int:
    m = 0
    for i, p in enumerate(prices[:-1]):
        m += max(prices[i + 1] - p, 0)
    return m


class Solution:

    def __init__(self):
        self.func = _maxProfit

    def maxProfit(self, prices: List[int]) -> int:
        return self.func(prices)


if __name__ == '__main__':
    so = Solution()
    ans = so.maxProfit([1, 2, 3, 5])
    print(ans)
