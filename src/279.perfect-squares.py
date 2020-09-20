#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (43.46%)
# Likes:    1921
# Dislikes: 161
# Total Accepted:    226.8K
# Total Submissions: 519.4K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

# @lc code=start
import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            minVal = float('inf')
            j = 1
            while j*j <= i:
                minVal = min(minVal, dp[i-j*j]+1) 
                j += 1
            dp[i] = minVal
        return dp[n]
            
    def isSquare(self, i: int) -> bool:
        return i == math.isqrt(i) ** 2
        
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.numSquares(12)