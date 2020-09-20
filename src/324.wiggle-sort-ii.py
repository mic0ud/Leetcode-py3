#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (28.82%)
# Likes:    869
# Dislikes: 474
# Total Accepted:    74.9K
# Total Submissions: 256.7K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] >
# nums[2] < nums[3]....
# 
# Example 1:
# 
# 
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# 
# Example 2:
# 
# 
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
# 
# Note:
# You may assume all input has valid answer.
# 
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: [int]) -> None:
        # put the smaller half of the numbers on the even indexes and the larger half on the odd indexes, both from right to left:

        # Example nums = [1,2,...,7]      Example nums = [1,2,...,8] 

        # Small half:  4 . 3 . 2 . 1      Small half:  4 . 3 . 2 . 1 .
        # Large half:  . 7 . 6 . 5 .      Large half:  . 8 . 7 . 6 . 5
        # --------------------------      --------------------------
        # Together:    4 7 3 6 2 5 1      Together:    4 8 3 7 2 6 1 5
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

    def wiggleSort_SLOW(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        res, n = [], len(nums)
        l,r = 0, n // 2 if n%2 == 0 else n // 2 + 1
        while r < n:
            res = [nums[l],nums[r]] + res if res and nums[l] >= res[-1] else res + [nums[l],nums[r]]
            l += 1
            r += 1
        if n%2 > 0:
            res.append(nums[l])
        for i in range(len(nums)):
            nums[i] = res[i]
# @lc code=end

