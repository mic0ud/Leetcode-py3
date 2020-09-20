#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (32.07%)
# Likes:    2094
# Dislikes: 732
# Total Accepted:    402.7K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# Note:
# 
# 
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
#

# @lc code=start
class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        k = k if k <= len(nums) else k-len(nums)
        tmp = nums[-k:]
        for i in range(len(nums)-1,k-1,-1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = tmp[i]


    def rotate_TLE(self, nums: [int], k: int) -> None:
        k = k if k <= len(nums) else k-len(nums)
        while k > 0:
            tmp = nums[-1]
            for i in range(len(nums)-1,0,-1):                
                nums[i] = nums[i-1]
            nums[0] = tmp
            k -= 1


    def rotate_(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k if k <= len(nums) else k-len(nums)
        tmp = nums[-k:]+nums[:len(nums)-k]
        for i in range(len(nums)):
            nums[i] = tmp[i]
# @lc code=end
# [1,2,3]\n4
