#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#
# https://leetcode.com/problems/sum-of-subarray-minimums/description/
#
# algorithms
# Medium (29.66%)
# Likes:    734
# Dislikes: 54
# Total Accepted:    17.2K
# Total Submissions: 57.4K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array of integers A, find the sum of min(B), where B ranges over
# every (contiguous) subarray of A.
# 
# Since the answer may be large, return the answer modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2],
# [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000


# @lc code=start
class Solution:
    def sumSubarrayMins(self, A: [int]) -> int:
        n, mod = len(A), 10**9 + 7
        left, right, sl, sr = [0]*n, [0]*n, [],[]
        for i in range(n):
            count = 1
            while sl and sl[-1][0] > A[i]:
                count += sl.pop()[1]
            left[i] = count
            sl.append([A[i], count])
        for i in range(n-1,-1,-1):
            count = 1
            while sr and sr[-1][0] >= A[i]:
                count += sr.pop()[1]
            right[i] = count
            sr.append([A[i], count])
        res = 0
        for i in range(n):
            res += A[i]*left[i]*right[i]
        return res % mod
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.sumSubarrayMins([71,55,82,55])
