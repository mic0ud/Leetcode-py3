#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
# https://leetcode.com/problems/minimum-falling-path-sum/description/
#
# algorithms
# Medium (59.79%)
# Likes:    441
# Dislikes: 44
# Total Accepted:    32.9K
# Total Submissions: 54.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a square array of integers A, we want the minimum sum of a falling path
# through A.
# 
# A falling path starts at any element in the first row, and chooses one
# element from each row.  The next row's choice must be in a column that is
# different from the previous row's column by at most one.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: 12
# Explanation: 
# The possible falling paths are:
# 
# 
# 
# [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
# 
# 
# The falling path with the smallest sum is [1,4,7], so the answer is 12.
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length == A[0].length <= 100
# -100 <= A[i][j] <= 100
# 
#
# [1,2,3],
# [4,5,6],
# [7,8,9]]
# @lc code=start
class Solution:
    def minFallingPathSum(self, A: [[int]]) -> int:
        m = len(A)
        n = len(A[0])
        # dp[i][j]: minimun sum ending at A[i][j]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i] = A[0][i]
        for i in range(1,m):
            for j in range(n):
                dp[i][j] = min(dp[i-1][j-1] if j >= 1 else float('inf'), dp[i-1][j], dp[i-1][j+1] if j < n-1 else float('inf')) + A[i][j]
        return min(dp[-1])
# @lc code=end

