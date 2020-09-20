#
# @lc app=leetcode id=1262 lang=python3
#
# [1262] Greatest Sum Divisible by Three
#
# https://leetcode.com/problems/greatest-sum-divisible-by-three/description/
#
# algorithms
# Medium (36.85%)
# Likes:    210
# Dislikes: 6
# Total Accepted:    6.9K
# Total Submissions: 16.4K
# Testcase Example:  '[3,6,5,1,8]'
#
# Given an array nums of integers, we need to find the maximum possible sum of
# elements of the array such that it is divisible by three.
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum
# divisible by 3).
# 
# Example 2:
# 
# 
# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum
# divisible by 3).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxSumDivThree(self, nums: [int]) -> int:
        if not nums:
            return 0
        mod_0, mod_1, mod_2 = [], [], []
        for n in nums:
            if n % 3 == 0:
                mod_0.append(n)
            elif n % 3 == 1:
                mod_1.append(n)
            elif n % 3 == 2:
                mod_2.append(n)
        res = sum(mod_0)
        tmp = sum(mod_1) + sum(mod_2)
        if tmp % 3 == 0:
            return res + tmp
        cut = float('inf')
        mod_1.sort()
        mod_2.sort()
        if tmp % 3 == 1:
            if mod_1:
                cut = min(cut, mod_1[0])
            if len(mod_2) > 1:
                cut = min(cut, mod_2[0]+mod_2[1])
        if tmp % 3 == 2:
            if mod_2:
                cut = min(cut, mod_2[0])
            if len(mod_1) > 1:
                cut = min(cut, mod_1[0]+mod_1[1])
        return res + tmp - cut
# @lc code=end

