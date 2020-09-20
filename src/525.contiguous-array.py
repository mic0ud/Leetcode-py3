#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (44.08%)
# Likes:    995
# Dislikes: 49
# Total Accepted:    52.6K
# Total Submissions: 118K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1. 
# 
# 
# Example 1:
# 
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
# 
# 
# 
# Example 2:
# 
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Note:
# The length of the given binary array will not exceed 50,000.
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        res, prefixSum, idxMap = 0, 0, defaultdict(int)
        idxMap[0] = -1
        for i in range(len(nums)):
            prefixSum += nums[i] if nums[i] == 1 else -1
            if prefixSum in idxMap.keys():
                res = max(res, i-idxMap[prefixSum])
            else:
                idxMap[prefixSum] = i
        return res


    def findMaxLength_(self, nums: [int]) -> int:
        if len(nums) <= 1:
            return 0
        score = res = 0
        lastScore = {}
        for i, n in enumerate(nums):
            score = score + 1 if n == 1 else score - 1
            if score == 0:
                res = i + 1
            lastScore.setdefault(score, i)            
            if score in lastScore:
                res = max(res, i-lastScore[score])
        return res
# @lc code=end
# [0,1,0,1]
