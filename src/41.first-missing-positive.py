#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (30.18%)
# Likes:    2502
# Dislikes: 695
# Total Accepted:    275.5K
# Total Submissions: 901.6K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    # not O(1) space
    def firstMissingPositive(self, nums: [int]) -> int:
        n = len(nums)
        if n == 0:
            return 1
        if n == 1:
            return 2 if nums[0] == 1 else 1
        res = 1
        visited = defaultdict(bool)
        for i in nums:
            if i <= 0: continue
            visited[i] = True
            while visited[res]:
                res += 1
        return res
# @lc code=end

