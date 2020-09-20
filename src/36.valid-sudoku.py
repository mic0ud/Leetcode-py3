#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (45.54%)
# Likes:    1168
# Dislikes: 390
# Total Accepted:    293.7K
# Total Submissions: 640.2K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
# 
# 
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without
# repetition.
# 
# 
# 
# A partially filled sudoku which is valid.
# 
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠ ["5","3",".",".","7",".",".",".","."],
# ⁠ ["6",".",".","1","9","5",".",".","."],
# ⁠ [".","9","8",".",".",".",".","6","."],
# ⁠ ["8",".",".",".","6",".",".",".","3"],
# ⁠ ["4",".",".","8",".","3",".",".","1"],
# ⁠ ["7",".",".",".","2",".",".",".","6"],
# ⁠ [".","6",".",".",".",".","2","8","."],
# ⁠ [".",".",".","4","1","9",".",".","5"],
# ⁠ [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# [
# ["8","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being 
# ⁠   modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is
# invalid.
# 
# 
# Note:
# 
# 
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        if len(board) != 9 or len(board[0]) != 9:
            return False
        rowCount = [defaultdict(int) for _ in range(9)]
        colCount = [defaultdict(int) for _ in range(9)]
        subgridCount = [defaultdict(int) for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                c = board[i][j]
                if c != '.' and (rowCount[i][c] >= 1 or colCount[j][c] >= 1 or subgridCount[self.getSubgridId(i,j)][c] >= 1):
                    return False
                else:
                    rowCount[i][c] += 1
                    colCount[j][c] += 1
                    subgridCount[self.getSubgridId(i,j)][c] += 1
        return True

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

