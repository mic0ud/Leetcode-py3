#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#
# https://leetcode.com/problems/longest-turbulent-subarray/description/
#
# algorithms
# Medium (45.89%)
# Likes:    204
# Dislikes: 64
# Total Accepted:    19.2K
# Total Submissions: 41.6K
# Testcase Example:  '[9,4,2,10,7,8,8,1,9]'
#
# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only
# if:
# 
# 
# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is
# even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is
# odd.
# 
# 
# That is, the subarray is turbulent if the comparison sign flips between each
# adjacent pair of elements in the subarray.
# 
# Return the length of a maximum size turbulent subarray of A.

# Example 1:

# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
 
# Example 2:

# Input: [4,8,12,16]
# Output: 2

# Example 3:

# Input: [100]
# Output: 1

# Note:

# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9
# 
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, A: [int]) -> int:
        n = len(A)
        if n <= 1:
            return n
        start, end, res = 0, 2, 1
        while end < n:
            if (A[end] > A[end-1] > A[end-2]) or (A[end] < A[end-1] < A[end-2]):
                start = end-1
            elif A[end] == A[end-1]:
                start = end
            end += 1
            res = max(res, end-start)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maxTurbulenceSize([4,8,12,16])
