#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (42.37%)
# Likes:    1317
# Dislikes: 60
# Total Accepted:    170.8K
# Total Submissions: 399.1K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
# 
# Example:
# 
# 
# Input: 4
# Output: [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.
# 
# 
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        if n <= 0:
            return []
        # row = [False for _ in range(n)]
        board = ['.'*n for _ in range(n)]
        col = [False for _ in range(n)]
        diag1 = [False for _ in range(2*n-1)]
        diag2 = [False for _ in range(2*n-1)]
        res = []
        self.solve(board, n, 0, col, diag1, diag2, res)
        return res

    def solve(self, board, n, r, col, diag1, diag2, res) -> bool:
        if r == n:
            return True
        for j in range(n):
            if not col[j] and not diag1[r+j] and not diag2[n-1-r+j]:
                board[r] = board[r][:j]+'Q'+(board[r][j+1:] if j<n-1 else '')
                col[j] = True
                diag1[r+j] = True
                diag2[n-1-r+j] = True
                if (self.solve(board, n,r+1,col, diag1, diag2, res)):
                    res.append(list(board))
                board[r] = board[r][:j]+'.'+(board[r][j+1:] if j<n-1 else '')
                col[j] = False
                diag1[r+j] = False
                diag2[n-1-r+j] = False   
        return False            
# @lc code=end
# diag1 = i + j, diag2 = (n-1-i)+j
if __name__ == '__main__':
    s = Solution()
    s.solveNQueens(5)