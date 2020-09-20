#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#
# https://leetcode.com/problems/two-city-scheduling/description/
#
# algorithms
# Easy (55.30%)
# Likes:    443
# Dislikes: 54
# Total Accepted:    19.5K
# Total Submissions: 35.3K
# Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
#
# There are 2N people a company is planning to interview. The cost of flying
# the i-th person to city A is costs[i][0], and the cost of flying the i-th
# person to city B is costs[i][1].
# 
# Return the minimum cost to fly every person to a city such that exactly N
# people arrive in each city.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# 
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
# interviewing in each city.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000
# 
#

# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2
        # dp[i][j] represents the cost when considering first (i + j) people in which i people assigned to city A and j people assigned to city B.
        dp = [[0] * (N+1) for _ in range(N+1)]
        for i in range(1, N+1):
            dp[i][0] = dp[i-1][0] + costs[i-1][0]
        for j in range(1, N+1):
            dp[0][j] = dp[0][j-1] + costs[j-1][1]
        for ii in range(1, N+1):
            for jj in range(1, N+1):
                dp[ii][jj] = min(dp[ii-1][jj] + costs[ii+jj-1][0], dp[ii][jj-1]+costs[ii+jj-1][1])
        return dp[N][N]

# @lc code=end

