#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#
# https://leetcode.com/problems/number-of-closed-islands/description/
#
# algorithms
# Medium (59.75%)
# Likes:    145
# Dislikes: 9
# Total Accepted:    8.3K
# Total Submissions: 13.8K
# Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
#
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
# 4-directionally connected group of 0s and a closed island is an island
# totally (all left, top, right, bottom) surrounded by 1s.
# 
# Return the number of closed islands.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid =
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water
# (group of 1s).
# 
# Example 2:
# 
# 
# 
# 
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,1,1,1,1,1,1],
# [1,0,0,0,0,0,1],
# [1,0,1,1,1,0,1],
# [1,0,1,0,1,0,1],
# [1,0,1,1,1,0,1],
# [1,0,0,0,0,0,1],
# ⁠              [1,1,1,1,1,1,1]]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
# 
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: [[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
                return 
            visited[i][j] = True
            if grid[i][j] == 0:
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
        
        res = 0
        for i in range(m-1):
            if not visited[i][0] and grid[i][0] == 0:
                dfs(i, 0)
            if not visited[i][n-1] and grid[i][n-1] == 0:
                dfs(i, n-1)           
        for j in range(n):
            if not visited[0][j] and grid[0][j] == 0:
                dfs(0, j)
            if not visited[m-1][j] and grid[m-1][j] == 0:
                dfs(m-1, j)
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not visited[i][j] and grid[i][j] == 0:
                    dfs(i, j)
                    res += 1
        return res
# @lc code=end
# [0,0,1,0,0],
# [0,1,0,1,0],
# [0,1,1,1,0]

# [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]

# [1,1,1,1,1,1,1],
# [1,0,0,0,0,0,1],
# [1,0,1,1,1,0,1],
# [1,0,1,0,1,0,1],
# [1,0,1,1,1,0,1],
# [1,0,0,0,0,0,1],
# [1,1,1,1,1,1,1]]