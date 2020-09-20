#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (51.78%)
# Likes:    2867
# Dislikes: 88
# Total Accepted:    448.2K
# Total Submissions: 850.5K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        if not candidates:
            return []
        candidates = sorted(candidates, reverse=True)
        def search(target, i: int, path: [], res: []) -> bool:
            if target < 0:
                return
            elif target == 0:
                res.append(path)
                return
            else:
                for j in range(i, len(candidates)):
                    if candidates[j] <= target:
                        new_path = list(path)
                        new_path.append(candidates[j])
                        search(target-candidates[j], j, new_path, res)
        res = []
        search(target, 0, [], res)     
        return res           
# @lc code=end
# 
if __name__ == '__main__':
    s = Solution()
    s.combinationSum([2,3,6,7], 7)
