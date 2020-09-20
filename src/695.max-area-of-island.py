#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (59.52%)
# Likes:    1423
# Dislikes: 67
# Total Accepted:    115.7K
# Total Submissions: 192.7K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
# 
# Example 1:
# 
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Given the above grid, return 6. Note the answer is not 11, because the island
# must be connected 4-directionally.
# 
# Example 2:
# 
# 
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# 
# Note: The length of each dimension in the given grid does not exceed 50.
# 
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i, j) -> int:
            if visited[i][j] or grid[i][j] == 0:
                return 0
            visited[i][j] = True
            area = 1
            if i+1 < m:
                area += dfs(i+1,j)
            if i-1>=0:
                area += dfs(i-1,j)
            if j+1 < n:
                area += dfs(i,j+1)
            if j-1>=0:
                area += dfs(i,j-1)
            return area
            
        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = max(area, dfs(i,j))
        return area
# @lc code=end
# [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
# [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]

# [1,1,0,1,1],
# [1,0,0,0,0],
# [0,0,0,0,1],
# [1,1,0,1,1]]

