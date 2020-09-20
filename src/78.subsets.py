#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (56.28%)
# Likes:    2707
# Dislikes: 63
# Total Accepted:    460.3K
# Total Submissions: 808.2K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        # return self.bfs(nums)
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def bfs(self, nums: [int]) -> [[int]]:
        res = [[]]
        for n in nums:
            tmp = []
            for r in res:
                tmp.append(r+[n])
            res += tmp
        return res

    def dfs(self, nums: [int], n: int, path: [int], res: [[int]]):
        res.append(path)
        for i in range(n, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
# @lc code=end

