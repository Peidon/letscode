from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [[False] * 10 for _ in range(10)]
        row = [[False] * 10 for _ in range(10)]
        box = [[False] * 10 for _ in range(10)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                box_idx = (i // 3) * 3 + (j // 3)
                num = int(board[i][j])

                if box[box_idx][num] or col[j][num] or row[i][num]:
                    return False
                else:
                    box[box_idx][num] = True
                    col[j][num] = True
                    row[i][num] = True

        return True

if __name__ == '__main__':
    b = [[".",".","5",".",".",".",".",".","6"],
         [".",".",".",".","1","4",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".","9","2",".","."],
         ["5",".",".",".",".","2",".",".","."],
         [".",".",".",".",".",".",".","3","."],
         [".",".",".","5","4",".",".",".","."],
         ["3",".",".",".",".",".","4","2","."],
         [".",".",".","2","7",".","6",".","."]]

    s = Solution()
    v = s.isValidSudoku(b)
    print(v)