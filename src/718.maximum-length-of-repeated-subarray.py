#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (47.87%)
# Likes:    858
# Dislikes: 37
# Total Accepted:    46.4K
# Total Submissions: 96.4K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
# 
# Example 1:
# 
# 
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def findLength(self, A: [int], B: [int]) -> int:
        if not A or not B:
            return 0
        # longest common suffix ending at i for A, j for B
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        res = 0
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findLength([0,0,0,0,0], [0,0,0,0,0])
