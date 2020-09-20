#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (57.46%)
# Likes:    3379
# Dislikes: 285
# Total Accepted:    366.2K
# Total Submissions: 630.4K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        if not nums:
            return []
        n = len(nums)
        if n == 1:
            return nums
        res = [1 for _ in range(n)]
        # left to right
        for i in range(1,n):
            res[i] = nums[i-1] * res[i-1]
        # right to left
        tmp = nums[-1]
        for i in range(n-2, -1,-1):
            res[i] *= tmp 
            tmp *= nums[i]
        return res
# @lc code=end
# Numbers:     2    3    4     5
# Lefts:       1    2  2*3 2*3*4
# Rights:  3*4*5  4*5    5     1
if __name__ == '__main__':
    s = Solution()
    s.productExceptSelf([2,3,4,5])