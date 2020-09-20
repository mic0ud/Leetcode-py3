#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (19.35%)
# Likes:    1425
# Dislikes: 331
# Total Accepted:    73.9K
# Total Submissions: 381.1K
# Testcase Example:  '[4,2,3]'
#
# 
# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
# 
# 
# 
# We define an array is non-decreasing if array[i]  holds for every i (1 
# 
# Example 1:
# 
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
# 
# 
# 
# Example 2:
# 
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
# 
# 
# 
# Note:
# The n belongs to [1, 10,000].
# 
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: [int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        if n == 1:
            return True
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                if i == n-1:
                    return True
                for j in range(i, n-1):
                    if nums[j+1] < nums[j]:
                        return False
                return i==1 or nums[i] >= nums[i-2] or nums[i+1] >= nums[i-1]
        return True
# @lc code=end
# [2,3,3,2,4]
