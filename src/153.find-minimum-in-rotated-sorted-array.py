#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (43.85%)
# Likes:    1366
# Dislikes: 191
# Total Accepted:    345.5K
# Total Submissions: 787.3K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2,3]
# Output: 0
# 
# 
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.bs(nums, 0, len(nums) - 1)

    def bs(self, nums, l, r):
        if l >= r:
            return nums[l]
        mid = (l+r) // 2
        if nums[mid] < nums[l] and nums[mid] < nums[r]:
            return min(self.bs(nums, l, mid), self.bs(nums, mid+1, r))
        else:
            if nums[l] < nums[r]:
                return self.bs(nums, l, mid)
            else:
                return self.bs(nums, mid+1, r)

# @lc code=end

