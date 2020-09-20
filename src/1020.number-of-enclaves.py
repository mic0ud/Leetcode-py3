#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#
# https://leetcode.com/problems/number-of-enclaves/description/
#
# algorithms
# Medium (55.05%)
# Likes:    164
# Dislikes: 17
# Total Accepted:    12.3K
# Total Submissions: 22.2K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# Given a 2D array A, each cell is 0 (representing sea) or 1 (representing
# land)
# 
# A move consists of walking from one land square 4-directionally to another
# land square, or off the boundary of the grid.
# 
# Return the number of land squares in the grid for which we cannot walk off
# the boundary of the grid in any number of moves.

# Example 1:
 
# Input: [
# [0,0,0,0],
# [1,0,1,0],
# [0,1,1,0],
# [0,0,0,0]]
# Output: 3
# Explanation: 
# There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed
# because its on the boundary.
# 
# Example 2:
 
# Input: [
# [0,1,1,0],
# [0,0,1,0],
# [0,0,1,0],
# [0,0,0,0]]
# Output: 0
# Explanation: 
# All 1s are either on the boundary or can reach the boundary.

# Note:

# 1 <= A.length <= 500
# 1 <= A[i].length <= 500
# 0 <= A[i][j] <= 1
# All rows have the same size.
# 
#

# @lc code=start
class Solution:
    def numEnclaves(self, A: [[int]]) -> int:
        if not A or not A[0]:
            return 0
        m = len(A)
        n = len(A[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or A[i][j] == 0 or visited[i][j]:
                return
            visited[i][j] = True
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        for i in range(m):
            if A[i][0] == 1 and not visited[i][0]:
                dfs(i,0)
            if A[i][n-1] == 1 and not visited[i][n-1]:
                dfs(i,n-1)
        for j in range(1,n-1):
            if A[0][j] == 1 and not visited[0][j]:
                dfs(0,j)
            if A[m-1][j] == 1 and not visited[m-1][j]:
                dfs(m-1,j)
        res = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if A[i][j] == 1 and not visited[i][j]:
                    res += 1
        return res
# @lc code=end
# [[0,0,1,1,0,0,0,0,0,1],[1,1,0,1,0,0,1,0,0,1],[1,1,0,0,1,0,1,1,0,0],[1,0,0,1,0,0,0,0,0,1],[0,0,1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,0,1,0,1,1,1,0,1,0],[0,1,1,1,0,0,1,0,0,1],[0,1,1,0,0,1,0,1,1,0],[1,0,1,1,0,0,1,1,0,0],[1,0,1,0,1,1,1,0,0,1]]
