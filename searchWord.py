class Solution(object):
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
                    visited = [[False] * len(board[i]) for _ in range(len(board))]
                    if self.dfs(board, i, j, word, 1, visited):
                        return True
        return False

    def dfs(self, board, i, j, word, k, visited):
        if k == len(word): return True
        visited[i][j] = True
        if i - 1 >= 0 and not visited[i - 1][j]:
            if word[k] == board[i - 1][j]:
                if self.dfs(board, i - 1, j, word, k + 1, visited):
                    return True
        if i + 1 < len(board) and not visited[i + 1][j]:
            if word[k] == board[i + 1][j]:
                if self.dfs(board, i + 1, j, word, k + 1, visited):
                    return True
        if j - 1 >= 0 and not visited[i][j - 1]:
            if word[k] == board[i][j - 1]:
                if self.dfs(board, i, j - 1, word, k + 1, visited):
                    return True
        if j + 1 < len(board[i]) and not visited[i][j + 1]:
            if word[k] == board[i][j + 1]:
                if self.dfs(board, i, j + 1, word, k + 1, visited):
                    return True
        return False

ans = Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS")
print(ans)