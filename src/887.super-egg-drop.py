#
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#
# https://leetcode.com/problems/super-egg-drop/description/
#
# algorithms
# Hard (25.78%)
# Likes:    645
# Dislikes: 68
# Total Accepted:    14.3K
# Total Submissions: 54.2K
# Testcase Example:  '1\n2'
#
# You are given K eggs, and you have access to a building with N floors from 1
# to N. 
# 
# Each egg is identical in function, and if an egg breaks, you cannot drop it
# again.
# 
# You know that there exists a floor F with 0 <= F <= N such that any egg
# dropped at a floor higher than F will break, and any egg dropped at or below
# floor F will not break.
# 
# Each move, you may take an egg (if you have an unbroken one) and drop it from
# any floor X (with 1 <= X <= N). 
# 
# Your goal is to know with certainty what the value of F is.
# 
# What is the minimum number of moves that you need to know with certainty what
# F is, regardless of the initial value of F?

# Example 1:
# 
# 
# Input: K = 1, N = 2
# Output: 2
# Explanation: 
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty
# that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with
# certainty.

# Example 2:
# 
# 
# Input: K = 2, N = 6
# Output: 3
# 
# 
# 
# Example 3:
# 
# 
# Input: K = 3, N = 14
# Output: 4

# Note:
# 
# 
# 1 <= K <= 100
# 1 <= N <= 10000


# @lc code=start
from collections import defaultdict
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # dp[M][K]means that, given K eggs and M moves,
        # what is the maximum number of floor that we can check.

        # The dp equation is:
        # dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
        # which means we take 1 move to a floor,
        # if egg breaks, then we can check dp[m - 1][k - 1] floors.
        # if egg doesn't breaks, then we can check dp[m - 1][k] floors.

        # dp[m][k] is the number of combinations and it increase exponentially to N
        dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, K+1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1
                if dp[i][j] >= N:
                    return i

    def superEggDrop_LTE(self, K: int, N: int) -> int:
        dp = [[float('inf') for _ in range(K+1)] for _ in range(N+1)]
        for i in range(K+1):
            dp[1][i] = 1
        for i in range(N+1):
            dp[i][1] = i
        for j in range(2,K+1):
            for i in range(2,N+1):    
                tmp = float('inf')        
                for k in range(1, i+1):
                    tmp = min(tmp, max(dp[k-1][j-1],dp[i-k][j])+1)
                dp[i][j] = tmp
        return dp[N][K]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.superEggDrop(100,10000)
    s.superEggDrop(3,14)
