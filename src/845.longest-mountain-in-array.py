#
# @lc app=leetcode id=845 lang=python3
#
# [845] Longest Mountain in Array
#
# https://leetcode.com/problems/longest-mountain-in-array/description/
#
# algorithms
# Medium (35.45%)
# Likes:    444
# Dislikes: 17
# Total Accepted:    25.6K
# Total Submissions: 71.6K
# Testcase Example:  '[2,1,4,7,3,2,5]'
#
# Let's call any (contiguous) subarray B (of A) a mountain if the following
# properties hold:
# 
# 
# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] <
# B[i] > B[i+1] > ... > B[B.length - 1]
# 
# 
# (Note that B could be any subarray of A, including the entire array A.)
# 
# Given an array A of integers, return the length of the longest mountain. 
# 
# Return 0 if there is no mountain.
# 
# Example 1:
# 
# 
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# 
# 
# Example 2:
# 
# 
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 
# 
# Follow up:
# 
# 
# Can you solve it using only one pass?
# Can you solve it in O(1) space?
# 
# 
#

# @lc code=start
class Solution:
    def longestMountain(self, A: [int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        res, start, i = 0, 0, 0
        while i < n-1:
            if A[i+1] == A[i]:
                i += 1
                start = i
                continue
            # increasing 
            while i < n-1 and A[i+1] > A[i]:
                i += 1
            if i >= n-1:
                break
            if A[i+1] == A[i] or i == start: 
                i += 1
                start = i
                continue
            # decreasing
            while i < n-1 and A[i+1] < A[i]:
                i += 1            
            res = max(res, i-start+1)
            start = i
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.longestMountain([2,1,4,7,3,2,5])
    # s.longestMountain([0,1,2,3,4,5,4,3,2,1,0])
    # s.longestMountain([9,8,7,6,5,4,3,2,1,0])
    s.longestMountain([3,3,1])
    # s.longestMountain([875,884,239,731,723,685])
