#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#
# https://leetcode.com/problems/advantage-shuffle/description/
#
# algorithms
# Medium (43.66%)
# Likes:    366
# Dislikes: 23
# Total Accepted:    16K
# Total Submissions: 36.2K
# Testcase Example:  '[2,7,11,15]\n[1,10,4,11]'
#
# Given two arrays A and B of equal size, the advantage of A with respect to B
# is the number of indices i for which A[i] > B[i].
# 
# Return any permutation of A that maximizes its advantage with respect to
# B.

# Example 1:
# 
# 
# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]

# Example 2:

# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]

# Note:

# 1 <= A.length = B.length <= 10000
# 0 <= A[i] <= 10^9
# 0 <= B[i] <= 10^9


# @lc code=start
from bisect import bisect_right
from collections import defaultdict
class Solution:
    def advantageCount(self, A: [int], B: [int]) -> [int]:
        sortedA = sorted(A)
        taken = defaultdict(list)
        for b in sorted(B, reverse=True):
            if sortedA[-1] > b:
                taken[b].append(sortedA.pop())
        res = [(taken[b] or sortedA).pop() for b in B]
        return res


    def advantageCount_(self, A: [int], B: [int]) -> [int]:
        res, sortedA, sortedB = [-1 for _ in range(len(A))], sorted(A), sorted(B)
        idxMap = {}
        for i, b in enumerate(B):
            idxMap[b] = i
        p, q, used, remaining = 0, len(A)-1, set(), set([i for i in range(len(A))])
        while p < len(A) and sortedA[p] <= sortedB[0]:
            idxInB = idxMap[sortedB[q]]
            res[idxInB] = sortedA[p]
            used.add(idxInB)
            remaining.discard(idxInB)
            p += 1
            q -= 1
        if p == len(A):
            return res

        for i, a in enumerate(sortedA[p:]):
            idx = bisect_right(sortedB, a) - 1
            while (idx >= 0 and a == sortedB[idx]) or idxMap[sortedB[idx]] in used:
                idx -= 1
            if idx >= 0:
                idxInB = idxMap[sortedB[idx]]
                res[idxInB] = sortedA[i+p]
                used.add(idxInB)
                remaining.discard(idxInB)
        for k in range(len(res)):
            if res[k] == -1:
                res[k] = sortedA[remaining.pop()]
        return res
# @lc code=end
# [2,0,4,1,2]\n[1,3,0,0,2], [2,0,2,1,4]
# [9,1,2,4,5]\n[6,2,9,1,4], [9,4,1,2,5]
# [5621,1743,5532,3549,9581]\n[913,9787,4121,5039,1481], [1743,9581,5532,5621,3549]
if __name__ == '__main__':
    s = Solution()
    # s.advantageCount([2,0,4,1,2], [1,3,0,0,2])
    # s.advantageCount([12,24,8,32], [13,25,32,11])
    # s.advantageCount([2,7,11,15], [1,10,4,11])
    # s.advantageCount([9,1,2,4,5], [6,2,9,1,4])
    s.advantageCount([5621,1743,5532,3549,9581], [913,9787,4121,5039,1481])
    s.advantageCount_([5621,1743,5532,3549,9581], [913,9787,4121,5039,1481])
