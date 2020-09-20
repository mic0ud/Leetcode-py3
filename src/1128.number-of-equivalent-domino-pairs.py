#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/
#
# algorithms
# Easy (46.16%)
# Likes:    99
# Dislikes: 59
# Total Accepted:    13.9K
# Total Submissions: 30K
# Testcase Example:  '[[1,2],[2,1],[3,4],[5,6]]'
#
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] =
# [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is,
# one domino can be rotated to be equal to another domino.
# 
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and
# dominoes[i] is equivalent to dominoes[j].
# 
# 
# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 1 <= dominoes.length <= 40000
# 1 <= dominoes[i][j] <= 9
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: [[int]]) -> int:
        c = defaultdict(int)
        for d in dominoes:
            c[str(min(d))+str(max(d))] += 1
        res = 0
        for v in c.values():
            res += v*(v-1)//2
        return res

    def numEquivDominoPairs_FIRST(self, dominoes: [[int]]) -> int:
        countMap = {}
        for item in dominoes:
            s = tuple(sorted(item))
            if s not in countMap.keys():
                countMap[s] = 1
            else:
                countMap[s] += 1
        res = 0
        for k, v in countMap.items():
            if v >= 2:
                res += v*(v-1)//2
        return res
# @lc code=end

