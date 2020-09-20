#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#
# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (47.61%)
# Likes:    332
# Dislikes: 763
# Total Accepted:    71.7K
# Total Submissions: 149.8K
# Testcase Example:  '2'
#
# Given a non-negative integer n, count all numbers with unique digits, x,
# where 0 ≤ x < 10^n.

# Example:

# Input: 2
# Output: 91 
# Explanation: The answer should be the total numbers in the range of 0 ≤ x <
# 100, 
# excluding 11,22,33,44,55,66,77,88,99


# @lc code=start
from collections import defaultdict
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        digits = [9,9]+[i for i in range(8,0,-1)]
        dp = [0 for _ in range(11)]
        dp[0], dp[1], dp[2] = 1, 10, 91
        for i in range(3, 11):
            tmp = 1
            for j in range(i):
                tmp *= digits[j]
            dp[i] = tmp + dp[i-1]
        return dp[n] if n <= 10 else dp[-1]     
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.countNumbersWithUniqueDigits(3)
