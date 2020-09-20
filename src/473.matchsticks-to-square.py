#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (36.63%)
# Likes:    417
# Dislikes: 44
# Total Accepted:    30.1K
# Total Submissions: 82.1K
# Testcase Example:  '[1,1,2,2,2]'
#
# Remember the story of Little Match Girl? By now, you know exactly what
# matchsticks the little match girl has, please find out a way you can make one
# square by using up all those matchsticks. You should not break any stick, but
# you can link them up, and each matchstick must be used exactly one time.
# 
# ⁠Your input will be several matchsticks the girl has, represented with their
# stick length. Your output will either be true or false, to represent whether
# you could make one square using all the matchsticks the little match girl
# has.
# 
# Example 1:
# 
# Input: [1,1,2,2,2]
# Output: true
# 
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
# 
# 
# 
# Example 2:
# 
# Input: [3,3,3,3,4]
# Output: false
# 
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
# 
# 
# 
# Note:
# 
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
# 
# 
#

# @lc code=start
class Solution:
    def makesquare(self, nums: [int]) -> bool:
        if len(nums) < 4:
            return False
        numSum = sum(nums)
        if numSum % 4 != 0:
            return False
        targetLen = [numSum // 4 for _ in range(4)]
        nums = sorted(nums, reverse=True)
        def dfs(targets, pos) -> bool:
            if pos == len(nums):
                return True
            for i in range(4):
                if targets[i] >= nums[pos]:
                    targets[i] -= nums[pos]
                    if dfs(targets, pos+1):
                        return True
                    targets[i] += nums[pos]
            return False
        if dfs(targetLen, 0):
            return True
        return False
# @lc code=end

