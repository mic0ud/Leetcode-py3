#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
#
# algorithms
# Medium (55.13%)
# Likes:    351
# Dislikes: 21
# Total Accepted:    12.7K
# Total Submissions: 22.8K
# Testcase Example:  '[0,6,5,2,2,5,1,9,4]\n1\n2'
#
# Given an array A of non-negative integers, return the maximum sum of elements
# in two non-overlapping (contiguous) subarrays, which have lengths L and M.
# (For clarification, the L-length subarray could occur before or after the
# M-length subarray.)
# 
# Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1])
# + (A[j] + A[j+1] + ... + A[j+M-1]) and either:
# 
# 
# 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
# 0 <= j < j + M - 1 < i < i + L - 1 < A.length.

# Example 1:
# 
# 
# Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with
# length 2.
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with
# length 2.
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8]
# with length 3.
# 
# 
# 
# 
# Note:
# 
# 
# L >= 1
# M >= 1
# L + M <= A.length <= 1000
# 0 <= A[i] <= 1000
# [2,1,5,6,0,9,5,0,3,8]
# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, A: [int], L: int, M: int) -> int:
        n = len(A)
        # do a CDF so that range sum can easily be calculated
        sumA = [0 for _ in range(n)]
        sumA[0] = A[0]
        for i in range(1, n):
            sumA[i] = sumA[i-1] + A[i]
        res, Lmax, Mmax = sumA[L+M-1], sumA[L-1], sumA[M-1]
        # window  | --- L --- | --- M --- |
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, sumA[i - M] - sumA[i - L - M])
            res = max(res, Lmax + sumA[i] - sumA[i - M])

        # window  | --- M --- | --- L --- |
        for i in range(L + M, len(A)):
            Mmax = max(Mmax, sumA[i - L] - sumA[i - L - M])
            res = max(res, Mmax + sumA[i] - sumA[i - L])

        return res        
        
# @lc code=end

