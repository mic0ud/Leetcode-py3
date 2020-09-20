#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#
# https://leetcode.com/problems/maximum-width-ramp/description/
#
# algorithms
# Medium (43.37%)
# Likes:    413
# Dislikes: 10
# Total Accepted:    14.1K
# Total Submissions: 32.2K
# Testcase Example:  '[6,0,8,2,1,5]'
#
# Given an array A of integers, a ramp is a tuple (i, j) for which i < j and
# A[i] <= A[j].  The width of such a ramp is j - i.
# 
# Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

# Example 1:
# 
# 
# Input: [6,0,8,2,1,5]
# Output: 4
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] =
# 5.

# Example 2:
# 
# 
# Input: [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.

# Note:
# 
# 
# 2 <= A.length <= 50000
# 0 <= A[i] <= 50000


# @lc code=start
from bisect import bisect_left
class Solution:
    def maxWidthRamp(self, A: [int]) -> int:
        stack = []
        for i in range(len(A)):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)
        res = 0
        for j in range(len(A)-1,-1,-1):
            while stack and A[stack[-1]] <= A[j]:
                res = max(res, j-stack.pop())
        return res

    def maxWidthRamp_NlogN(self, A: [int]) -> int:
        stack = []
        res = 0
        for i, a in enumerate(A):
            if not stack or -stack[-1][0] > a:
                stack.append([-a, i])
            else:
                idx = bisect_left(stack, [-a,-1]) # [val, idx], idx disabled from bisect by -1
                res = max(res, i-stack[idx][1])
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maxWidthRamp([9,8,1,0,1,9,4,0,4,1])
    # s.maxWidthRamp([6,0,8,2,1,5])
