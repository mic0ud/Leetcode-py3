#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (37.96%)
# Likes:    1228
# Dislikes: 77
# Total Accepted:    123.5K
# Total Submissions: 324K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 18, 20, 24, 27, 30, 32
#

# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        i2, i3, i5 = 1, 1, 1
        for i in range(2, n+1):
            n2 = 2*dp[i2]
            n3 = 3*dp[i3]
            n5 = 5*dp[i5]
            dp[i] = min(n2,n3,n5)
            if dp[i] == n2:
                i2 += 1
            if dp[i] == n3:
                i3 += 1
            if dp[i] == n5:
                i5 += 1
        return dp[-1]
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.nthUglyNumber(10)