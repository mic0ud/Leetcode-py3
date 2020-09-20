#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (43.65%)
# Likes:    3802
# Dislikes: 138
# Total Accepted:    510.9K
# Total Submissions: 1.2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i: int, j: int):
            if i >= m or i < 0 or j >= n or j < 0 or visited[i][j] or grid[i][j] == '0':
                return
            visited[i][j] = True
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    res += 1
                    dfs(i, j)
        return res
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
