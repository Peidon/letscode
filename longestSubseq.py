def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int

    dp[i,j] = {
    dp[i-1, j-1] + 1 -> if text1[i-1] == text[j-1],
    max( dp[i-1][j], dp[i][j-1] ) -> otherwise,
    }
      r  a  b  b  i  t
   r  1  1  1  1  1  1
   a  1  2  2  2  2  2
   b  1  2  3  3  3  3
   b  1  2  3  4  4  4
   b  1  2
   i
   t

     b  a  b  g  b  a  g
   b 1  1  1
   a 1  2
   g

    """
    if not text1 or not text2:
        return 0
    m = len(text1)
    n = len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):

        for j in range(1,n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return dp[m][n]
