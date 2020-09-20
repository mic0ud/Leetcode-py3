#
# @lc app=leetcode id=795 lang=python3
#
# [795] Number of Subarrays with Bounded Maximum
#
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
#
# algorithms
# Medium (44.42%)
# Likes:    448
# Dislikes: 39
# Total Accepted:    15.5K
# Total Submissions: 34.2K
# Testcase Example:  '[2,1,4,3]\n2\n3'
#
# We are given an array A of positive integers, and two positive integers L and
# R (L <= R).
# 
# Return the number of (contiguous, non-empty) subarrays such that the value of
# the maximum array element in that subarray is at least L and at most R.
# 
# 
# Example :
# Input: 
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2,
# 1], [3].
# 
# 
# Note:
# 
# 
# L, R  and A[i] will be an integer in the range [0, 10^9].
# The length of A will be in the range of [1, 50000].
# 
# 
#

# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, A: [int], L: int, R: int) -> int:
        if not A:
            return 0
        subArrs = []
        i, j = 0, 0
        while j < len(A):
            while j < len(A) and A[j] > R:
                j += 1
                i = j
            while j < len(A) and A[j] <= R:
                j += 1
            subArrs.append(list(A[i:j]))
            j += 1
            i = j
        res = 0
        for arr in subArrs:
            res += self.count(arr, L)
        return res
    
    def count(self, arr: [int], L: int) -> int:
        n = len(arr)
        total = sum(range(n+1))
        invalid = 0
        i, j = 0, 0
        while j < n:
            while j < n and arr[j] >= L:
                j += 1
                i = j
            while j < n and arr[j] < L:
                j += 1
            invalid += sum(range(j-i+1))
            j += 1
            i = j
        return total - invalid
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.numSubarrayBoundedMax([2, 1, 3, 4, 2, 3], 2, 3)
