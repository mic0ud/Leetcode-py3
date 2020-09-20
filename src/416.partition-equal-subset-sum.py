#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (41.83%)
# Likes:    1815
# Dislikes: 55
# Total Accepted:    129.8K
# Total Submissions: 308.3K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# Note:
# 
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def canPartition(self, nums: [int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if n <= 1 or s % 2 != 0:
            return False
        # the sum of nums would not exceed 20000
        smap = defaultdict(bool)
        smap[0] = True
        for i in range(len(nums)):
            keys = list(smap.keys())
            for d in keys:
                smap[nums[i]+d] = True

        return smap[s//2]
# @lc code=end

