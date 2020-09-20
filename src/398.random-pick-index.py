#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#
# https://leetcode.com/problems/random-pick-index/description/
#
# algorithms
# Medium (52.01%)
# Likes:    339
# Dislikes: 548
# Total Accepted:    68.1K
# Total Submissions: 129.4K
# Testcase Example:  '["Solution","pick"]\n[[[1,2,3,3,3]],[3]]'
#
# Given an array of integers with possible duplicates, randomly output the
# index of a given target number. You can assume that the given target number
# must exist in the array.
# 
# Note:
# The array size can be very large. Solution that uses too much extra space
# will not pass the judge.
# 
# Example:
# 
# 
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
# 
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should
# have equal probability of returning.
# solution.pick(3);
# 
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
# 
# 
#

# @lc code=start
from collections import defaultdict
from random import randrange
class Solution:

    def __init__(self, nums: [int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                res = i if randrange(count) % count == 0 else res
        return res

    # memory limit exceeded
    # def __init__(self, nums: [int]):
    #     self.g = defaultdict(list)
    #     for i in range(len(nums)):
    #         self.g[nums[i]].append(i)

    # def pick(self, target: int) -> int:
    #     if target not in self.g:
    #         return -1
    #     n = len(self.g[target])
    #     i = randrange(n)
    #     return self.g[target][i]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

