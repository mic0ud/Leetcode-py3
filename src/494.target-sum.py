#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (45.99%)
# Likes:    1851
# Dislikes: 85
# Total Accepted:    126.3K
# Total Submissions: 273.4K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# ⁠
# 
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.  
# 
# 
# Example 1:
# 
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# 
# 
# Note:
# 
# The length of the given array is positive and will not exceed 20. 
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
# 
# 
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: [int], S: int) -> int:
        return self.dp_optimaized(nums,S)
        # return self.from1049(nums,S)

    def from1049_TLE(self, nums: [int], S: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [[] for _ in range(n)]
        dp[0].append(nums[0])
        dp[0].append(-nums[0])
        for i in range(1,n):
            for j in dp[i-1]:
                dp[i].append(j+nums[i])
                dp[i].append(j-nums[i])
        return dp[-1].count(S)

    def findTargetSumWays_DP(self, nums: [int], S: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        numSum = sum(nums)
        if abs(S) > numSum:
            return 0
        dp = [[0 for _ in range(2*numSum+1)] for _ in range(n+1)]        
        dp[0][numSum] = 1
        for i in range(1, n+1):
            for j in range(2*numSum+1):
                if dp[i-1][j-numSum] > 0:
                    dp[i][(j-numSum)+nums[i-1]] += dp[i-1][j-numSum]
                    dp[i][(j-numSum)-nums[i-1]] += dp[i-1][j-numSum]
                # dp[i][(j-numSum)] = dp[i-1][(j-numSum)+nums[i-1]] + dp[i-1][(j-numSum)-nums[i-1]]
        return dp[n][S+numSum]

    def dp_optimaized(self, nums: [int], S: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        numSum = sum(nums)
        if abs(S) > numSum or (S+numSum) % 2 != 0:
            return 0
        # subset P (+), N (-), P - N = S
        # P - N + P + N = S + P + N
        # 2P = S + sum(nums)
        # P = (S + sum(nums)) / 2
        # -> find P
        # dp[i][j] -> ways of using the first i numbers to sum up to j
        dp = [[0 for _ in range(numSum+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(numSum+1):
                dp[i][j] = dp[i-1][j] + (0 if j < nums[i-1] else dp[i-1][j-nums[i-1]])
        return dp[n][(S+numSum)//2]

    def findTargetSumWaysDFS(self, nums: [int], S: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        N = [[nums[i], -nums[i]] for i in range(n)]
        
        def dfs(i: int, target: int, res: [int]):
            if i == n:
                if target == 0:
                    res[0] += 1
                return
            dfs(i+1, target-N[i][0], res)            
            dfs(i+1, target-N[i][1], res)

        res = [0]
        dfs(0,S,res)
        return res[0]
# @lc code=end
# [1,0]\n1
# [2,20,24,38,44,21,45,48,30,48,14,9,21,10,46,46,12,48,12,38]\n48
if __name__ == '__main__':
    s = Solution()
    s.findTargetSumWays([1, 1, 1, 1, 1],3)