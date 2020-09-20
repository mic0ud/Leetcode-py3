#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#
# https://leetcode.com/problems/132-pattern/description/
#
# algorithms
# Medium (27.87%)
# Likes:    894
# Dislikes: 56
# Total Accepted:    39.4K
# Total Submissions: 140.1K
# Testcase Example:  '[1,2,3,4]'
#
# 
# Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a
# subsequence ai, aj, ak such
# that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n
# numbers as input and checks whether there is a 132 pattern in the list.
# 
# Note: n will be less than 15,000.
# 
# Example 1:
# 
# Input: [1, 2, 3, 4]
# 
# Output: False
# 
# Explanation: There is no 132 pattern in the sequence.
# 
# 
# 
# Example 2:
# 
# Input: [3, 1, 4, 2]
# 
# Output: True
# 
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# 
# 
# 
# Example 3:
# 
# Input: [-1, 3, 2, 0]
# 
# Output: True
# 
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1,
# 3, 0] and [-1, 2, 0].
# 
# 
#

# @lc code=start
class Solution:
    def find132pattern(self, nums: [int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        stack, mid = [], float('-inf')
        for i in range(n-1,-1,-1):
            if nums[i] < mid:
                return True
            while stack and nums[i] > stack[-1]:
                mid = stack.pop()
            stack.append(nums[i])
        return False

    def find132pattern_(self, nums: [int]) -> bool:
        stack = []
        mid = float('-inf')
        for n in nums[::-1]:
            if n < mid:
                return True
            while stack and n > stack[-1]:
                mid = stack.pop()
            stack.append(n)
        return False
# @lc code=end

