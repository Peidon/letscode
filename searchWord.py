class Solution(object):

    def __init__(self):
        self.visited = None
        self.result = False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return False

        return self.find(board, word)

    def find(self, board, word):

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    self.visited = [[False] * len(board[i]) for _ in range(len(board))]
                    self.dfs(board, i, j, word, 1)
        return self.result

    def dfs(self, board, i, j, word, k):
        if k == len(word):
            self.result = True
            return
        self.visited[i][j] = True
        if i - 1 >= 0:
            if not self.visited[i - 1][j] and word[k] == board[i - 1][j]:
                self.dfs(board, i - 1, j, word, k + 1)
        if i + 1 < len(board):
            if not self.visited[i + 1][j] and word[k] == board[i + 1][j]:
                self.dfs(board, i + 1, j, word, k + 1)
        if j - 1 >= 0:
            if not self.visited[i][j - 1] and word[k] == board[i][j - 1]:
                self.dfs(board, i, j - 1, word, k + 1)
        if j + 1 < len(board[i]):
            if not self.visited[i][j + 1] and word[k] == board[i][j + 1]:
                self.dfs(board, i, j + 1, word, k + 1)
        self.visited[i][j] = False


if __name__ == '__main__':
    ans = Solution().exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS")
    print(ans)
