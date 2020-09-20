#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (39.59%)
# Likes:    1257
# Dislikes: 78
# Total Accepted:    156.2K
# Total Submissions: 390.3K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# 
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
# 
# 
# Empty cells are indicated by the character '.'.
# 
# 
# A sudoku puzzle...
# 
# 
# ...and its solution numbers marked in red.
# 
# Note:
# 
# 
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) != 9 or len(board[0]) != 9:
            return
        rowCount = [defaultdict(int) for _ in range(9)]
        colCount = [defaultdict(int) for _ in range(9)]
        subgridCount = [defaultdict(int) for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                c = board[i][j]
                if c != '.':
                    rowCount[i][c] += 1
                    colCount[j][c] += 1
                    subgridCount[self.getSubgridId(i,j)][c] += 1
        self.solve(board,0,0,rowCount, colCount, subgridCount)


    def solve(self, board: [[str]], i, j, rowCount, colCount, subgridCount) -> bool:
        if i == 9:
            return True
        nexti = i+1 if j == 8 else i
        nextj = j+1 if j < 8 else 0        
        if board[i][j] != '.':
            return self.solve(board, nexti, nextj, rowCount, colCount, subgridCount)
        else:
            for k in range(1,10):
                strK = str(k)
                if rowCount[i][strK] == 0 and colCount[j][strK] == 0 and subgridCount[self.getSubgridId(i,j)][strK] == 0:
                    board[i][j] = strK
                    rowCount[i][strK] += 1
                    colCount[j][strK] += 1
                    subgridCount[self.getSubgridId(i,j)][strK] += 1
                    if(self.solve(board, nexti, nextj, rowCount, colCount, subgridCount)):
                        return True
                    board[i][j] = '.'
                    rowCount[i][strK] -= 1
                    colCount[j][strK] -= 1
                    subgridCount[self.getSubgridId(i,j)][strK] -= 1
        return False

    def getSubgridId(self, i, j):
        if 0 <= i <= 2:
            if 0 <= j <= 2:
                return 0
            elif 3 <= j <= 5:
                return 1
            else:
                return 2
        if 3 <= i <= 5:
            if 0 <= j <= 2:
                return 3
            elif 3 <= j <= 5:
                return 4
            else:
                return 5
        else:
            if 0 <= j <= 2:
                return 6
            elif 3 <= j <= 5:
                return 7
            else:
                return 8
# @lc code=end
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
if __name__ == '__main__':
    s = Solution()
    a = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    a = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    s.solveSudoku(a)
