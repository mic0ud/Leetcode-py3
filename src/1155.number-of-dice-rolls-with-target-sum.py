#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#
# algorithms
# Medium (48.67%)
# Likes:    319
# Dislikes: 22
# Total Accepted:    19.7K
# Total Submissions: 39.7K
# Testcase Example:  '1\n6\n3'
#
# You have d dice, and each die has f faces numbered 1, 2, ..., f.
# 
# Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to
# roll the dice so the sum of the face up numbers equals target.
# 
# 
# Example 1:
# 
# 
# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation: 
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
# 
# 
# Example 2:
# 
# 
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation: 
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# 
# 
# Example 3:
# 
# 
# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation: 
# You throw two dice, each with 5 faces.  There is only one way to get a sum of
# 10: 5+5.
# 
# 
# Example 4:
# 
# 
# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation: 
# You throw one die with 2 faces.  There is no way to get a sum of 3.
# 
# 
# Example 5:
# 
# 
# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation: 
# The answer must be returned modulo 10^9 + 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= d, f <= 30
# 1 <= target <= 1000
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numRollsToTarget_(self, d: int, f: int, target: int) -> int:
        dp = [[0 for i in range(target + 1)] for j in range(d + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                k = 1
                while k <= min(j, f):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % mod
                    k += 1
        return dp[d][target] % mod

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > d*f:
            return 0
        # dp[i][j]: count for target j using i dices
        dp = [[0 for _ in range(target+1)] for _ in range(d+1)]
        dp[0][0] = 1
        for i in range(1, d+1):
            for j in range(1, target+1):
                for k in range(1, min(j,f)+1): # j cannot be greater than target
                    dp[i][j] += dp[i-1][j-k]
        return dp[d][target] % (10**9+7)


    def numRollsToTarget_TLE(self, d: int, f: int, target: int) -> int:
        if target > d*f:
            return 0

        def search(i, t, res: []):
            if i > d:
                return
            if i == d and t == 0:
                res[0] += 1
                return
            for j in range(1,min(f,t)+1):
                search(i+1, t-j, res)
        res = [0]
        search(0,target,res)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.numRollsToTarget(30,30,500)
    s.numRollsToTarget(2,5,10)
