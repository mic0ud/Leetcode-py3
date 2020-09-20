#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
# https://leetcode.com/problems/4sum-ii/description/
#
# algorithms
# Medium (51.75%)
# Likes:    943
# Dislikes: 68
# Total Accepted:    93.1K
# Total Submissions: 177.8K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j,
# k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
# 
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤
# N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is
# guaranteed to be at most 2^31 - 1.
# 
# Example:
# 
# 
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# Output:
# 2
# 
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


# @lc code=start
from bisect import bisect_left, bisect_right
from collections import Counter
class Solution:
    def fourSumCount(self, A: [int], B: [int], C: [int], D: [int]) -> int:
        ab = Counter([a+b for a in A for b in B])
        cd = Counter([c+d for c in C for d in D])
        res = 0
        for k, v in ab.items():
            res += v*cd[-k]
        return res

    def fourSumCount_SLOW(self, A: [int], B: [int], C: [int], D: [int]) -> int:
        res, N, ab, cd = 0, len(A), [], []
        for i in range(N):
            for j in range(N):
                ab.append(A[i]+B[j])
                cd.append(C[i]+D[j])
        ab.sort()
        cd.sort()
        lab = bisect_left(ab, 0)
        rab = bisect_right(ab, 0)
        lcd = bisect_left(cd, 0)
        rcd = bisect_right(cd, 0)
        res += (rab-lab)*(rcd-lcd)
        tmp1 = ab[:lab]+cd[rcd:]
        tmp2 = cd[:lcd]+ab[rab:]
        i, j = 0, len(tmp1)-1
        while i < j:
            if tmp1[i] + tmp1[j] > 0:
                j -= 1
            elif tmp1[i] + tmp1[j] < 0:
                i += 1
            else:                
                ci, cj = 1, 1
                while i+ci < j and tmp1[i+ci] == tmp1[i]:
                    ci += 1
                while j-cj > i and tmp1[j-cj] == tmp1[j]:
                    cj += 1
                res += ci*cj
                i += ci
                j -= cj
        i, j = 0, len(tmp2)-1
        while i < j:
            if tmp2[i] + tmp2[j] > 0:
                j -= 1
            elif tmp2[i] + tmp2[j] < 0:
                i += 1
            else:
                ci, cj = 1, 1
                while i+ci < j and tmp2[i+ci] == tmp2[i]:
                    ci += 1
                while j-cj > i and tmp2[j-cj] == tmp2[j]:
                    cj += 1
                res += ci*cj
                i += ci
                j -= cj
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.fourSumCount([0,1,-1],[-1,1,0],[0,0,1],[-1,1,1])
    s.fourSumCount([1, 2],[-2,-1],[-1, 2],[0, 2])
    s.fourSumCount([-1,-1],[-1,1],[-1,1],[1,-1])
