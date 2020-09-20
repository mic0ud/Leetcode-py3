#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#
# https://leetcode.com/problems/maximum-sum-circular-subarray/description/
#
# algorithms
# Medium (33.44%)
# Likes:    433
# Dislikes: 22
# Total Accepted:    15K
# Total Submissions: 44.8K
# Testcase Example:  '[1,-2,3,-2]'
#
# Given a circular array C of integers represented by A, find the maximum
# possible sum of a non-empty subarray of C.
# 
# Here, a circular array means the end of the array connects to the beginning
# of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and
# C[i+A.length] = C[i] when i >= 0.)
# 
# Also, a subarray may only include each element of the fixed buffer A at most
# once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not
# exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3
# 
# 
# 
# Example 2:
# 
# 
# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
# 
# 
# 
# Example 3:
# 
# 
# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
# 
# 
# 
# Example 4:
# 
# 
# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
# 
# 
# Example 5:
# 
# 
# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
# 
# 
# 
# 
# Note: 
# 
# 
# -30000 <= A[i] <= 30000
# 1 <= A.length <= 30000
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maxSum, minSum, maxNum, totalSum = self.maxSubarray(A)
        if maxNum <= 0:
            return maxNum
        return max(maxSum, totalSum - minSum)

    def maxSubarray(self, nums:[int]) -> (int, int, int, int):  
        dpMin = [None for i in range(len(nums))]      
        dpMax = [None for i in range(len(nums))]      
        dpMin[0] = nums[0]
        dpMax[0] = nums[0]
        maxSum = nums[0]
        minSum = nums[0]
        maxNum = nums[0]
        totalSum = nums[0]
        for n in range(1, len(nums)):
            dpMax[n] = nums[n] + (dpMax[n-1] if dpMax[n-1] > 0 else 0)
            dpMin[n] = nums[n] + (dpMin[n-1] if dpMin[n-1] < 0 else 0)
            maxSum = max(maxSum, dpMax[n])
            minSum = min(minSum, dpMin[n])
            maxNum = max(maxNum, nums[n])
            totalSum += nums[n]
        return (maxSum, minSum, maxNum, totalSum)
# @lc code=end

