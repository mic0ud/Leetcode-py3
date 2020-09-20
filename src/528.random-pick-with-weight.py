#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#
# https://leetcode.com/problems/random-pick-with-weight/description/
#
# algorithms
# Medium (43.31%)
# Likes:    437
# Dislikes: 822
# Total Accepted:    48.4K
# Total Submissions: 111.8K
# Testcase Example:  '["Solution", "pickIndex"]\n[[[1]], []]'
#
# Given an array w of positive integers, where w[i] describes the weight of
# index i, write a function pickIndex which randomly picks an index in
# proportion to its weight.
# 
# Note:
# 
# 
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# 
# 
# Example 1:
# 
# 
# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# 
# 
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has one argument, the array w. pickIndex has no
# arguments. Arguments are always wrapped with a list, even if there aren't
# any.
# 
#

# @lc code=start
from random import randrange
from bisect import bisect_right
class Solution:

    def __init__(self, w: [int]):
        # accumulated sum
        self.ws = [w[0] for _ in range(len(w))]
        self.wsum = w[0]
        for i in range(1, len(w)):
            self.wsum += w[i]
            self.ws[i] = self.ws[i-1] + w[i]

    def pickIndex(self) -> int:
        r = randrange(self.wsum)
        return bisect_right(self.ws, r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

