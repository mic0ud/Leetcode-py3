#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (44.10%)
# Likes:    1140
# Dislikes: 139
# Total Accepted:    108.9K
# Total Submissions: 244.7K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an integer array with all positive numbers and no duplicates, find the
# number of possible combinations that add up to a positive integer target.
# 
# Example:
# 
# 
# nums = [1, 2, 3]
# target = 4
# 
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 
# Note that different sequences are counted as different combinations.
# 
# Therefore the output is 7.
# 
# 
# 
# 
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
# 
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test
# cases.


# @lc code=start
class Solution:
    def combinationSum4(self, nums: [int], target: int) -> int:
        if not nums:
            return 0
        memo = {}
        def search(t) -> int:
            if t in memo:
                return memo[t]
            if t < 0:
                return 0
            if t == 0:
                return 1
            res = 0
            for n in nums:
                res += search(t-n)
            memo[t] = res
            return memo[t]
        search(target)
        return memo[target]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.combinationSum4([1, 2, 3],4)
    s.combinationSum4([4,2,1],32)
