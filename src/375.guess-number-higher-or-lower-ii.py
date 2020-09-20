#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/
#
# algorithms
# Medium (39.00%)
# Likes:    688
# Dislikes: 1013
# Total Accepted:    55.1K
# Total Submissions: 139.2K
# Testcase Example:  '1'
#
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number I picked is
# higher or lower.
# 
# However, when you guess a particular number x, and you guess wrong, you pay
# $x. You win the game when you guess the number I picked.
# 
# Example:
# 
# 
# n = 10, I pick 8.
# 
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
# 
# Game over. 8 is the number I picked.
# 
# You end up paying $5 + $7 + $9 = $21.
# 
# 
# Given a particular n ≥ 1, find out how much money you need to have to
# guarantee a win.
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j]: min for n in [i:j+1], both i and j included
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        # for i in range(1,n):
        #     dp[i][i+1] = i
        #     if i < n-1:
        #         dp[i][i+2] = i+1
        for l in range(1,n):
            for s in range(1, n-l+1):
                dp[s][s+l] = float('inf')
                for k in range(s,s+l+1):
                    dp[s][s+l] = min(dp[s][s+l], k + max((dp[s][k-1] if k > s else 0),(dp[k+1][s+l] if k < s+l else 0)))
        return dp[1][n]  
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.getMoneyAmount(10)
    s.getMoneyAmount(5)
    s.getMoneyAmount(6)
