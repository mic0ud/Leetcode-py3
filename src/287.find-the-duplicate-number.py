#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (51.63%)
# Likes:    3334
# Dislikes: 405
# Total Accepted:    250.3K
# Total Submissions: 480.1K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# Example 1:
# 
# 
# Input: [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,3,4,2]
# Output: 3
# 
# Note:
# 
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        if len(nums) <= 1:
            return -1
        slow, fast = nums[0], nums[nums[0]]
        # running until slow and fast meet
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]] 
        # put slow to the beginning
        # let slow and fast go 1 step by 1 step until they meet
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findDuplicate([3,1,3,4,2])