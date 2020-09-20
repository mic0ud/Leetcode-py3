#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (54.83%)
# Likes:    2157
# Dislikes: 185
# Total Accepted:    465.5K
# Total Submissions: 847.6K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        total = len(nums)
        for i in nums:
            if i not in count.keys():
                count[i] = 1
            else:
                count[i] += 1
            if count[i] > total // 2:
                return i
        
# @lc code=end

