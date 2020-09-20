#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (24.57%)
# Likes:    1079
# Dislikes: 521
# Total Accepted:    177.3K
# Total Submissions: 712.2K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#

# @lc code=start
class Solution:
    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0] or len(board) < 3 or len(board[0]) < 3:
            return
        m = len(board)
        n = len(board[0])
        connected = [False for _ in range(m*n)]

        def visit(i: int, j: int):
            nbs = self.getNeighbours(i, j, m, n)
            for nb in nbs:
                i = nb[0]*n + nb[1]
                if board[nb[0]][nb[1]] == 'O' and not connected[i]:                   
                    connected[i] = True
                    visit(nb[0], nb[1])
        
        for i in range(n):
            if board[0][i] == 'O':
                visit(0, i)
            if board[m-1][i] == 'O':
                visit(m-1, i)
        for i in range(1, m-1):
            if board[i][0] == 'O':
                visit(i, 0)
            if board[i][n-1] == 'O':
                visit(i, n-1)
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and not connected[i*n+j]:
                    board[i][j] = 'X'

    def getNeighbours(self, i, j, m, n) -> [[int]]:
        res = []
        if 0 < i < m-1:
            res.append([i-1, j])
            res.append([i+1, j])
        elif i == 0:
            res.append([i+1, j])
        elif i == m-1:
            res.append([i-1, j])

        if 0 < j < n-1:
            res.append([i, j-1])
            res.append([i, j+1])     
        elif j == 0:
             res.append([i, j+1]) 
        elif j == n-1:
            res.append([i, j-1])   

        return res 
# @lc code=end

# [
# ["O","X","X","O","X"],
# ["X","O","O","X","O"],
# ["X","O","X","O","X"],
# ["O","X","O","O","O"],
# ["X","X","O","X","O"]]


#[
# ["O","X","X","O","X"],
# ["X","X","X","X","O"],
# ["X","X","X","O","X"],
# ["O","X","O","O","O"],
# ["X","X","O","X","O"]]

# [
# ["O","X","X","O","X"],
# ["X","X","X","X","O"],
# ["X","X","X","X","X"],
# ["O","X","O","O","O"],
# ["X","X","O","X","O"]]