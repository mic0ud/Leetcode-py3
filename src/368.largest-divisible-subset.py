#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (35.59%)
# Likes:    751
# Dislikes: 38
# Total Accepted:    56.2K
# Total Submissions: 156.5K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies:
# 
# Si % Sj = 0 or Sj % Si = 0.
# 
# If there are multiple solutions, return any subset is fine.
# 
# Example 1:

# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)

# Example 2:

# Input: [1,2,4,8]
# Output: [1,2,4,8]


# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: [int]) -> [int]:
        if not nums:
            return []
        nums.sort()
        dp = [1 for _ in range(len(nums))]
        resArr, res = [[nums[i]] for i in range(len(nums))], [nums[0]]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    resArr[i] = resArr[j]+[nums[i]]
                    if dp[i] > len(res):
                        res = resArr[i]
        return res 
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.largestDivisibleSubset([2,3,4,9,8])
    s.largestDivisibleSubset([2,3,5,7,11,13,17,19,23,31,1000000007])
    s.largestDivisibleSubset([1,2,4,8])
    s.largestDivisibleSubset([1,2,3,6,9,12,15,18])
    s.largestDivisibleSubset([1,2,3])
