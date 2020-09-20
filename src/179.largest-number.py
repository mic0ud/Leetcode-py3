#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (26.90%)
# Likes:    1463
# Dislikes: 176
# Total Accepted:    157.6K
# Total Submissions: 576.3K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# Example 1:
# 
# 
# Input: [10,2]
# Output: "210"
# 
# Example 2:
# 
# 
# Input: [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
#

# @lc code=start
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: [int]) -> str:
        def compare(s1, s2) -> int:
            if s1+s2 > s2+s1:
                return 1
            elif s1+s2 == s2+s1:
                return 0
            else:
                return -1
        strNums = sorted([str(n) for n in nums], key=cmp_to_key(compare), reverse=True)
        i = 0
        while i < len(nums)-1 and strNums[i] == '0':
            i += 1 
        return ''.join(strNums[i:])
# @lc code=end

