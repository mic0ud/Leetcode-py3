#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (58.71%)
# Likes:    1183
# Dislikes: 91
# Total Accepted:    126.6K
# Total Submissions: 212.4K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
# 
# Example:
# 
# 
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# 
# Note:
# 
# 
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: [int]) -> [int]:
        xor = 0
        for n in nums:
            xor ^= n
        mask = 1
        while xor&mask == 0:
            mask = mask << 1
        res1, res2 = 0, 0
        for n in nums:
            if n & mask == 0:
                res1 ^= n
            else:
                res2 ^= n
        return [res1, res2]

    def singleNumber_CHEAT(self, nums: [int]) -> [int]:
        res = set()
        for n in nums:
            if n not in res:
                res.add(n)
            else:
                res.remove(n)
        return list(res)
# @lc code=end

