#
# @lc app=leetcode id=1223 lang=python3
#
# [1223] Dice Roll Simulation
#
# https://leetcode.com/problems/dice-roll-simulation/description/
#
# algorithms
# Medium (44.97%)
# Likes:    264
# Dislikes: 93
# Total Accepted:    9.6K
# Total Submissions: 21.1K
# Testcase Example:  '2\n[1,1,2,2,2,3]'
#
# A die simulator generates a random number from 1 to 6 for each roll. You
# introduced a constraint to the generator such that it cannot roll the number
# i more than rollMax[i] (1-indexed) consecutive times. 
# 
# Given an array of integers rollMax and an integer n, return the number of
# distinct sequences that can be obtained with exact n rolls.
# 
# Two sequences are considered different if at least one element differs from
# each other. Since the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 2, rollMax = [1,1,2,2,2,3]
# Output: 34
# Explanation: There will be 2 rolls of die, if there are no constraints on the
# die, there are 6 * 6 = 36 possible combinations. In this case, looking at
# rollMax array, the numbers 1 and 2 appear at most once consecutively,
# therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2
# = 34.
# 
# 
# Example 2:
# 
# 
# Input: n = 2, rollMax = [1,1,1,1,1,1]
# Output: 30
# 
# 
# Example 3:
# 
# 
# Input: n = 3, rollMax = [1,1,1,2,2,3]
# Output: 181
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 5000
# rollMax.length == 6
# 1 <= rollMax[i] <= 15
# 
# 
#

# @lc code=start
class Solution:
    def dieSimulator(self, n: int, rollMax: [int]) -> int:
        # dp[i][j][k]: i -> length of sequence
        #              j -> last dice
        #              k -> number of consective dice at the end
        max_occur = max(rollMax)
        dp = [[[0 for _ in range(max_occur+1)] for _ in range(6)] for _ in range(n+1)]
        for j in range(6):
            dp[1][j][1] = 1
        for i in range(1, n+1):
            for j in range(6):
                for k in range(1, max_occur+1):
                    for p in range(6):
                        if p == j:
                            if k+1 <= rollMax[j]:
                                dp[i][j][k+1] = dp[i-1][p][k]
                        else:
                            dp[i][j][1] += dp[i-1][p][k]
        res = sum([dp[n][i][j] for i in range(6) for j in range(max_occur+1)])
        return res % (10**9+7)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.dieSimulator(2,[1,1,1,1,1,1])
    s.dieSimulator(4,[2,1,1,3,3,2])
    s.dieSimulator(3,[1,1,1,2,2,3])
    s.dieSimulator(2,[1,1,2,2,2,3])
