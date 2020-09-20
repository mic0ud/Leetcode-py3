#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (55.61%)
# Likes:    2782
# Dislikes: 98
# Total Accepted:    593.2K
# Total Submissions: 1.1M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        count = 0
        for i in range(len(nums)):
            while i < len(nums) and nums[i] == 0:
                nums.pop(i)
                count += 1
        nums += [0 for _ in range(count)]
        print(nums)

# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([0,0,1])
