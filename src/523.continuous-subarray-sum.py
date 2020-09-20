#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (24.36%)
# Likes:    899
# Dislikes: 1251
# Total Accepted:    91.6K
# Total Submissions: 375.3K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to a multiple of k, that is, sums up to n*k where n is also an
# integer.
# 
# 
# 
# Example 1:
# 
# 
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
# 
# 
# Example 2:
# 
# 
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
# 
# 
# 
# 
# Note:
# 
# 
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: [int], k: int) -> bool:
        if len(nums) < 2:
            return False

        k = abs(k)
        if k == 1:
            return True
        if k == 0:
            for i in range(len(nums)-1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False

        preSum, m = 0, defaultdict(int)
        m[0] = -1
        for i in range(len(nums)):
            preSum += nums[i]
            mod = preSum % k
            if mod not in m:
                m[mod] = i
            else:
                if i-m[mod] > 1:
                    return True
        return False
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.checkSubarraySum([23, 2, 4, 6, 7], 7)
