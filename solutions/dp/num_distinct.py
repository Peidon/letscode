class Solution:
    # s: rabbbit , t: rabbit
    # find sub-sequence of rabbit in rabbbit

    # f(i, j) = {
    #   max(i, j) -> if min(x, y) = 0,
    #   f(i - 1, j - 1) -> if ai = bj,
    #   min(f(i - 1, j) + 1, f(i, j - 1) + 1, f(i - 1, j - 1) + 1) -> otherwise,
    # }

    def __int__(self):
        self.start = 0

    def numDistinct(self, s: str, t: str) -> int:
        """
        dp[i,j] = {
            dp[i-1, j-1] + 1 -> if text1[i-1] == text[j-1],
            max( dp[i-1][j], dp[i][j-1] ) -> otherwise,
        }

      r  a  b  b  i  t
   r  1  0  0  0  0  0
   a  0  1  0  0  0  0
   b  0  0  1  1  0  0
   b  0  0  1  1  0  0
   b  0  0  1  1  0  0
   i  0  0  0  0  1  0
   t  0  0  0  0  0  1

      r  a  b  b  i  t
   r  1  1  0  0  0  0
   a  0  1  0  0  0  0
   b  0  0  1  1  0  0
   b  0  0  1  1  0  0
   b  0  0  1  1  0  0
   i  0  0  0  0  1  0
   t  0  0  0  0  0  1

     b  a  b  g  b  a  g
   b 1  0  1  0  1  0  0
   a 0  1  0  0  0  1  0
   g 0  0  0  1  0  0  1

       b  a  b  g  b  a  g
     0 1  1  1  1  1  1  1
   b 0 1  1  2  2  3  3  3
   a 0 0  1  1  1  1  4  4
   g 0 0  0  0  1  1  1  5

        :param s:
        :param t:
        :return:
        """
        pass


if __name__ == '__main__':
    num = Solution().numDistinct("rabbbit", "rabbit")
    print(num)
