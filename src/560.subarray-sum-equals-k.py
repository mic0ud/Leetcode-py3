#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.13%)
# Likes:    3017
# Dislikes: 84
# Total Accepted:    179K
# Total Submissions: 413.1K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        preSum = defaultdict(int)
        preSum[0] = 1
        res = 0
        tmp = 0
        for n in nums:
            tmp += n
            res += preSum[tmp-k]
            preSum[tmp] += 1
        return res
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.subarraySum([1,2,3,4], 5)
