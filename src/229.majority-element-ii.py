#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (33.55%)
# Likes:    1275
# Dislikes: 149
# Total Accepted:    127.3K
# Total Submissions: 371.2K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: [int]) -> [int]:
        c1,c2,n1,n2 = 0, 0, 0, 1
        for n in nums:
            if n == n1:
                c1 += 1
            elif n == n2:
                c2 += 1
            elif c1 == 0:
                c1, n1 = 1, n
            elif c2 == 0:
                c2, n2 = 1, n
            else:
                c1 -= 1
                c2 -= 1
        return [i for i in (n1,n2) if nums.count(i) > len(nums)//3]
# @lc code=end

