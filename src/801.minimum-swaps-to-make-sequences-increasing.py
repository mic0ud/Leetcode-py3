#
# @lc app=leetcode id=801 lang=python3
#
# [801] Minimum Swaps To Make Sequences Increasing
#
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/
#
# algorithms
# Medium (36.69%)
# Likes:    689
# Dislikes: 44
# Total Accepted:    20.5K
# Total Submissions: 55.2K
# Testcase Example:  '[1,3,5,4]\n[1,2,3,7]'
#
# We have two integer sequences A and B of the same non-zero length.
# 
# We are allowed to swap elements A[i] and B[i].  Note that both elements are
# in the same index position in their respective sequences.
# 
# At the end of some number of swaps, A and B are both strictly increasing.  (A
# sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... <
# A[A.length - 1].)
# 
# Given A and B, return the minimum number of swaps to make both sequences
# strictly increasing.  It is guaranteed that the given input always makes it
# possible.
# 
# 
# Example:
# Input: A = [1,3,5,4], B = [1,2,3,7]
# Output: 1
# Explanation: 
# Swap A[3] and B[3].  Then the sequences are:
# A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
# which are both strictly increasing.
# 
# 
# Note:
# 
# 
# A, B are arrays with the same length, and that length will be in the range
# [1, 1000].
# A[i], B[i] are integer values in the range [0, 2000].
# 
# 
#

# @lc code=start
class Solution:
    def minSwap(self, A: [int], B: [int]) -> int:
        N = len(A)
        swap, notSwap = [N] * N, [N] * N
        swap[0], notSwap[0] = 1, 0
        for i in range(1, N):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                notSwap[i] = notSwap[i-1]
                swap[i] = swap[i-1] + 1 # swap both i-1 and i
            if A[i] > B[i-1] and B[i] > A[i-1]:
                swap[i] = min(swap[i], notSwap[i-1]+1) # swap i
                notSwap[i] = min(notSwap[i], swap[i-1]) # swap i-1
        return min(swap[-1], notSwap[-1])
# @lc code=end

