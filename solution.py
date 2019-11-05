class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        self.find(board, word)

    def find(self, board, word):
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited = [[False] * len(board[i]) for _ in range(len(board))]
                    self.dfs(board, i, j, word, 1, visited)


    def dfs(self, board, i, j, word, k, visited):
        if k == len(word): return True
        if i - 1 >= 0 and not visited[i - 1][j]:
            if word[k] == board[i - 1][j]:
                visited[i - 1][j] = True
                self.dfs(board, i - 1, j, word, k + 1, visited)
        if i + 1 < len(board) and not visited[i + 1][j]:
            if word[k] == board[i + 1][j]:
                visited[i + 1][j] = True
                self.dfs(board, i + 1, j, word, k + 1, visited)
        if j - 1 >= 0 and not visited[i][j - 1]:
            if word[k] == board[i][j - 1]:
                visited[i][j - 1] = True
                self.dfs(board, i, j - 1, word, k + 1, visited)
        if j + 1 < len(board[i]) and not visited[i][j + 1]:
            if word[k] == board[i][j + 1]:
                visited[i][j + 1] = True
                self.dfs(board, i, j + 1, word, k + 1, visited)
        return False

Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")