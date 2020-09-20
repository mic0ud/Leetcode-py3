#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/
#
# algorithms
# Medium (39.49%)
# Likes:    182
# Dislikes: 17
# Total Accepted:    10.3K
# Total Submissions: 24.8K
# Testcase Example:  '[1,2,3,4]\n1'
#
# Given an integer array arr and an integer difference, return the length of
# the longest subsequence in arr which is an arithmetic sequence such that the
# difference between adjacent elements in the subsequence equals difference.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,2,3,4], difference = 1
# Output: 4
# Explanation: The longest arithmetic subsequence is [1,2,3,4].
# 
# Example 2:
# 
# 
# Input: arr = [1,3,5,7], difference = 1
# Output: 1
# Explanation: The longest arithmetic subsequence is any single element.
# 
# 
# Example 3:
# 
# 
# Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
# Output: 4
# Explanation: The longest arithmetic subsequence is [7,5,3,1].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^5
# -10^4 <= arr[i], difference <= 10^4
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: [int], difference: int) -> int:
        if not arr:
            return 0
        exists = defaultdict(int)
        res = 1
        for i in range(len(arr)):
            tmp = exists[arr[i]-difference] + 1
            exists[arr[i]] = tmp
            res = max(res, tmp)
        return res


    def longestSubsequence_SLOW(self, arr: [int], difference: int) -> int:
        if not arr:
            return 0
        # dp[i]: the longest at i
        dp = [0 for _ in range(len(arr))]
        dp[0] = 1
        exists = {}
        res = 1
        for i in range(len(arr)):
            if arr[i]-difference in exists.keys():
                dp[i] = dp[exists[arr[i]-difference]] + 1
            else:
                dp[i] = 1
            exists[arr[i]] = i
            res = max(res, dp[i])
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.longestSubsequence([3,4,-3,-2,-4], -5)
