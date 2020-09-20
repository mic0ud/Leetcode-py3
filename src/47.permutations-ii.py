#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (43.04%)
# Likes:    1439
# Dislikes: 50
# Total Accepted:    295.6K
# Total Submissions: 681.2K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        if not nums:
            return []
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        res = []
        level = 0
        self.nextPermute(count, level, [None for _ in range(len(nums))], res)
        return res
        
    def nextPermute(self, count: {int:int}, level: int, curr: [int], res: [int]):
        if level >= len(curr):
            res.append(list(curr))
            return
        for c in count:
            if count[c] > 0:
                curr[level] = c
                count[c] -= 1
                self.nextPermute(count, level+1, curr, res)
                count[c] += 1
# @lc code=end

