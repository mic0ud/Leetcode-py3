#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.37%)
# Likes:    3263
# Dislikes: 375
# Total Accepted:    521.4K
# Total Submissions: 1.6M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums)-1, target)

    def binarySearch(self, nums, start, end, target) -> int:
        if start > end:
            return -1

        mid = (end+start) // 2
        if target == nums[mid]:
            return mid

        if target > max(nums[start], nums[mid], nums[end]) or target < min(nums[start], nums[mid], nums[end]):
            return max(self.binarySearch(nums, start, mid-1,target), self.binarySearch(nums, mid+1, end, target))

        elif target < nums[mid]:
            if target == nums[start]:
                return start
            elif target < nums[start]:
                return self.binarySearch(nums, mid+1, end, target)
            else:
                return self.binarySearch(nums, start, mid-1, target)

        else: 
            if target == nums[end]:
                return end
            elif target < nums[end]:
                return self.binarySearch(nums, mid+1, end, target)
            else:
                return self.binarySearch(nums, start, mid-1, target)

# @lc code=end

