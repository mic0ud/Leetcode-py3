#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (30.37%)
# Likes:    2764
# Dislikes: 120
# Total Accepted:    261.2K
# Total Submissions: 859.3K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # (max, min)
        dp = [(nums[0], nums[0]) for n in range(len(nums))]
        res = nums[0]
        for i in range(1, len(nums)):
            imax = max(nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1])
            imin = min(nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1])
            dp[i] = (imax, imin)
            res = max(res, imax)
        return res
# @lc code=end

