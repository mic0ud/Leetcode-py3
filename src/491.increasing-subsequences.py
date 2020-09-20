#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#
# https://leetcode.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (43.29%)
# Likes:    575
# Dislikes: 100
# Total Accepted:    40.3K
# Total Submissions: 91.7K
# Testcase Example:  '[4,6,7,7]'
#
# Given an integer array, your task is to find all the different possible
# increasing subsequences of the given array, and the length of an increasing
# subsequence should be at least 2.

# Example:
# 
# 
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]

# Note:
# 
# 
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be
# considered as a special case of increasing sequence.


# @lc code=start
from collections import defaultdict
class Solution:
    def findSubsequences(self, nums: [int]) -> [[int]]:
        n = len(nums)
        if n < 2:
            return []
        res, seen = [], defaultdict(bool)
        def search(i, path:[], res):
            if i >= n:
                return
            k1, k2 = '', ''
            if path:
                k1 = ','.join([str(p) for p in path])
                k2 = k1+','+str(nums[i]) if nums[i] >= path[-1] else ''
                if len(path) > 1 and not seen[k1]:
                    seen[k1] = True
                    res.append(list(path))
                if k2 and not seen[k2]:
                    seen[k2] = True
                    res.append(list(path+[nums[i]]))
            search(i+1, list(path), res)
            if  not path or k2:
                search(i+1, list(path+[nums[i]]), res)
        search(0,[],res)
        return res

    def findSubsequences_WRONG(self, nums: [int]) -> [[int]]:
        n = len(nums)
        if n < 2:
            return []
        nums.sort()
        res, seen = [], defaultdict(bool)
        for i in range(n-1):
            for j in range(i+1, n):
                kk = ','.join([str(s) for s in nums[i:j+1]])
                if not seen[kk]:
                    res.append(list(nums[i:j+1]))
                    seen[kk] = True
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.findSubsequences([4, 3, 2, 1])
    # s.findSubsequences([4, 6, 7, 7])
    s.findSubsequences([100,90,80,70,60,50,60,70,80,90,100])
