class Palindrome:
    """
    最长回文子串
    """


    def __init__(self):
        self.result = ""
        self.left = 0
        self.right = 0

    def echo(self, s):
        self.result = s[self.left:self.right + 1]

    def build_around(self, i):
        self.left = i - 1
        self.right = i + 1

    def build_on_left(self, i):
        self.left = i
        self.right = i + 1

    def _rewind(self):
        self.left += 1
        self.right -= 1

    def _next(self):
        self.left -= 1
        self.right += 1

    def _palindrome_len(self, s: str) -> int:

        while self.left >= 0 and self.right < len(s) and s[self.left] == s[self.right]:
            self._next()

        self._rewind()
        return self.right - self.left + 1

    def longestPalindrome(self, s: str) -> str:

        max_len = 0

        for i, _ in enumerate(s):

            self.build_around(i)
            cur = self._palindrome_len(s)
            if max_len < cur:
                max_len = cur
                self.echo(s)

            self.build_on_left(i)
            cur = self._palindrome_len(s)
            if max_len < cur:
                max_len = cur
                self.echo(s)

        return self.result


if __name__ == '__main__':
    p = Palindrome()
    r = p.longestPalindrome("a")

    print(r)
