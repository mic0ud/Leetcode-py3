#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (49.49%)
# Likes:    1785
# Dislikes: 46
# Total Accepted:    279.9K
# Total Submissions: 565.1K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0] * col for k in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, len(grid[0])):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range (1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[row-1][col-1]
# @lc code=end

