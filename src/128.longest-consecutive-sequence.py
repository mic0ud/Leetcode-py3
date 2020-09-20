#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (43.17%)
# Likes:    2362
# Dislikes: 134
# Total Accepted:    244.7K
# Total Submissions: 566.1K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        numSet = set(nums)
        res = 1
        for n in numSet:
            if n-1 not in numSet:
                tmp = 1 
                while n+tmp in numSet:
                    tmp += 1
                res = max(res, tmp)
        return res


    def longestConsecutive_2(self, nums: [int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        boundary = defaultdict(int)
        res = 1
        for n in nums:
            if boundary[n] > 0: continue
            left = boundary[n-1]
            right = boundary[n+1]
            tmp = left + right + 1
            boundary[n-left], boundary[n], boundary[n+right] = tmp, tmp, tmp
            res = max(res, tmp)
        return res
# @lc code=end

