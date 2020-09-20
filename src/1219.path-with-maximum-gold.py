#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#
# https://leetcode.com/problems/path-with-maximum-gold/description/
#
# algorithms
# Medium (61.61%)
# Likes:    232
# Dislikes: 11
# Total Accepted:    14.6K
# Total Submissions: 23.2K
# Testcase Example:  '[[0,6,0],[5,8,7],[0,9,0]]'
#
# In a gold mine grid of size m * n, each cell in this mine has an integer
# representing the amount of gold in that cell, 0 if it is empty.
# 
# Return the maximum amount of gold you can collect under the conditions:
# 
# 
# Every time you are located in a cell you will collect all the gold in that
# cell.
# From your position you can walk one step to the left, right, up or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has
# some gold.
# 
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
# ⁠[5,8,7],
# ⁠[0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# Explanation:
# [[1,0,7],
# ⁠[2,0,6],
# ⁠[3,4,5],
# ⁠[0,3,0],
# ⁠[9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length, grid[i].length <= 15
# 0 <= grid[i][j] <= 100
# There are at most 25 cells containing gold.
# 
#

# @lc code=start
class Solution:
    def getMaximumGold(self, grid: [[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        visiting = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i, j) -> int:
            # if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visiting[i][j]:
            if grid[i][j] == 0:
                return 0         
            visiting[i][j] = True 
            tmp = 0
            if i-1 >= 0 and not visiting[i-1][j]:
                tmp = max(tmp, dfs(i-1,j))
            if i+1 < m and not visiting[i+1][j]:
                tmp = max(tmp, dfs(i+1,j))
            if j-1 >= 0 and not visiting[i][j-1]:
                tmp = max(tmp, dfs(i,j-1))
            if j+1 < n and not visiting[i][j+1]:
                tmp = max(tmp, dfs(i,j+1))
            # tmp1 = dfs(i-1,j)
            # tmp2 = dfs(i+1,j)
            # tmp3 = dfs(i,j-1)
            # tmp4 = dfs(i,j+1)
            visiting[i][j] = False
            return tmp + grid[i][j]
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:                    
                    res = max(res, dfs(i,j))
        return res
# @lc code=end
# [7, 38,0, 9, 40,39],
# [0, 32,0, 25,37,6],
# [9, 0, 18,34,14,0],
# [32,2, 0, 2, 21,29],
# [12,0, 0, 0, 0, 3],
# [20,20,8, 20,26,0]]
if __name__ == '__main__':
    s = Solution()
    s.getMaximumGold([[7,38,0,9,40,39],[0,32,0,25,37,6],[9,0,18,34,14,0],[32,2,0,2,21,29],[12,0,0,0,0,3],[20,20,8,20,26,0]])
