#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (34.58%)
# Likes:    1892
# Dislikes: 47
# Total Accepted:    169.5K
# Total Submissions: 487.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rowLength = len(matrix)
        colLength = len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(colLength)] for i in range(rowLength)]
        for i in range(1, rowLength):
            for j in range(1, colLength):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        res = max([max(row) for row in dp])
        return res ** 2
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])

