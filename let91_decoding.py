class Solution(object):
    """
    dp[i] = number of ways to parse s[1: i+1]
    dp[0] = 1
    e.g. "2315"
    when i = 1,     "2"
    dp[1] = s[1] == 0 ? 0 : 1 = 1
    when i == 2,    "23"
    dp[2] = 2, {2,3} {23}
    when i == 3,    "231"
    dp[3] = 2, {2,3,1} {23,1} {2,31}
    when i == 4
    dp[4] = 4, {2,3,1,5} {23,1,5} {2,31,5} {2,3,15} {23,15}

    dp[i+1] = dp[i-1](if s[i]!=0) + dp[i](if 26 >= s[i-1:i] > 0)
    """

    def _set_s(self, s: str):
        """
        :param s: str
        :return:
        """
        self.s = s

    def _check(self, i: int, j: int) -> bool:
        """
        :param i: int
        :return:  bool
        """
        n = int(self.s[i:j])
        if 26 >= n >= 10 and j == i+2:
            return True

        if n > 0 and j == i+1:
            return True

        return False

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        le = len(s)
        if le < 1:
            return 0

        if int(s[0]) == 0:
            return 0

        dp = [0] * (le+1)
        dp[0], dp[1] = 1, 1
        self._set_s(s)

        for i in range(2, len(dp)):
            if self._check(i-1, i):
                dp[i] = dp[i-1]

            if self._check(i-2, i):
                dp[i] += dp[i-2]

        return dp[le]


if __name__ == '__main__':
    n = Solution().numDecodings("27")
    assert n==1

    n = Solution().numDecodings("10")
    assert n == 1

    n = Solution().numDecodings("100")
    assert n == 0

    n = Solution().numDecodings("066")
    assert n == 0

    n = Solution().numDecodings("226")
    assert n == 3

    n = Solution().numDecodings("123123")
    assert n == 9

    print("Success")