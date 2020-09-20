#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (58.58%)
# Likes:    2784
# Dislikes: 89
# Total Accepted:    480.8K
# Total Submissions: 814.1K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def permute(self, nums: [int]) -> [[int]]:
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

