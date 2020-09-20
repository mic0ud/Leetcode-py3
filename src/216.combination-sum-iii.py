#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (53.67%)
# Likes:    862
# Dislikes: 47
# Total Accepted:    151.1K
# Total Submissions: 276.2K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> [[int]]:
        res = []
        def dfs(i,curr,t,path,res):
            if i < 0 or t < 0:
                return
            if i == 0 and t == 0:
                res.append(path)
                return
            for j in range(curr, min(t+1,10)):
                dfs(i-1, j+1, t-curr, path+[curr], res)
        for i in range(1, min(n+1, 10)):
            dfs(k,i,n,[],res)
        return res

    def combinationSum3_SLOW(self, k: int, n: int) -> [[int]]:
        low, high = sum([i for i in range(1,k+1)]), sum([i for i in range(n,n-k,-1)])
        if n < low or n > high:
            return []
        # dp[i][j]: i nums sum to j
        dp = [[set() for _ in range(n+1)] for _ in range(k+1)]
        for j in range(min(n,9)+1):
            dp[1][j].add(str(j))
        for i in range(2,k+1):
            low, high = sum([a for a in range(1,i+1)]), sum([a for a in range(n,n-i,-1)])
            for j in range(n+1):
                if low <= j <= high:
                    for b in range(1, j//2+1):
                        for c in range(1, i//2+1):
                            tmp1, tmp2 = dp[c][b], dp[i-c][j-b]
                            for t1 in tmp1:
                                t1 = t1.split(',')
                                for t2 in tmp2:
                                    t2 = t2.split(',')
                                    tmpRes = list(set(t1).union(set(t2)))
                                    if len(tmpRes) == (len(t1) + len(t2)):
                                        dp[i][j].add(','.join(sorted(tmpRes)))
        res = [[int(i) for i in item.split(',')] for item in dp[k][n]]
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.combinationSum3(3,9)
    s.combinationSum3(9,45)
