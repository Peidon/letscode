class Solution:
    """
    n = 1
    0 1
    n = 2
    00 01 11 10
    n = 3
    000 001 011 010 110 111 101 100
    """

    def gray(self, n):
        """

        :param n:  int [0...16]
        :return: list[Type[int]]
        """
        res = [0]
        for i in range(n):

            for num in reversed(res):
                res.append(num + (1 << i))

        return res
