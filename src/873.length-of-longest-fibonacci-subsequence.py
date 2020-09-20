#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/
#
# algorithms
# Medium (47.31%)
# Likes:    544
# Dislikes: 25
# Total Accepted:    23.1K
# Total Submissions: 48.7K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# A sequence X_1, X_2, ..., X_n is fibonacci-like if:
# 
# 
# n >= 3
# X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
# 
# 
# Given a strictly increasing array A of positive integers forming a sequence,
# find the length of the longest fibonacci-like subsequence of A.  If one does
# not exist, return 0.
# 
# (Recall that a subsequence is derived from another sequence A by deleting any
# number of elements (including none) from A, without changing the order of the
# remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6,
# 7, 8].)

# Example 1:
# 
# 
# Input: [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation:
# The longest subsequence that is fibonacci-like: [1,2,3,5,8].
# 
# 
# Example 2:

# Input: [1,3,7,11,12,14,18]
# Output: 3
# Explanation:
# The longest subsequence that is fibonacci-like:
# [1,11,12], [3,11,14] or [7,11,18].

# Note:
# 
# 
# 3 <= A.length <= 1000
# 1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
# (The time limit has been reduced by 50% for submissions in Java, C, and
# C++.)


# @lc code=start
from collections import defaultdict
class Solution:
    def lenLongestFibSubseq(self, A: [int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        exits = defaultdict(bool)
        for i, a in enumerate(A):
            exits[a] = True
        # dp[(A[i], A[j])]: count at (A[i], A[j]) (j > i)
        dp = defaultdict(int)
        for j in range(n):
            for i in range(j):
                tmp = A[j] - A[i]
                if exits[tmp] and tmp < A[i]:
                    dp[(A[i],A[j])] = dp[(tmp,A[i])] + 1
        res = max(dp.values()) if dp else 0
        return res + 2 if res > 0 else 0

    def lenLongestFibSubseq_SLOW(self, A: [int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        exits = defaultdict(int)
        for i, a in enumerate(A):
            exits[a] = i
        res = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                p, q, count = i, j, 0
                while A[p] + A[q] <= A[-1] and exits[A[p] + A[q]] > 0:
                    count += 1
                    p, q = q, exits[A[p] + A[q]]
                res = max(res, count)
        return res + 2 if res > 0 else 0
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.lenLongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50])
