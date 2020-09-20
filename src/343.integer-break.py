#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (48.87%)
# Likes:    737
# Dislikes: 195
# Total Accepted:    92.4K
# Total Submissions: 188.8K
# Testcase Example:  '2'
#
# Given a positive integer n, break it into the sum of at least two positive
# integers and maximize the product of those integers. Return the maximum
# product you can get.
# 
# Example 1:

# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# 
# 
# Example 2:
# 
# 
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# 
# Note: You may assume that n is not less than 2 and not larger than 58.


# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [i-1 for i in range(59)]
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        dp[5] = 6
        for i in range(6,59):
            for j in range(2, i//2+1):
                dp[i] = max(dp[i], max(j,dp[j])*max(i-j,dp[i-j]))
        return dp[n]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.integerBreak(10)
