#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (49.35%)
# Likes:    1264
# Dislikes: 155
# Total Accepted:    84.3K
# Total Submissions: 169.7K
# Testcase Example:  '"bbbab"'
#
# 
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
# 
# 
# Example 1:
# Input: 
# 
# "bbbab"
# 
# Output: 
# 
# 4
# 
# One possible longest palindromic subsequence is "bbbb".
# 
# 
# Example 2:
# Input:
# 
# "cbbd"
# 
# Output:
# 
# 2
# 
# One possible longest palindromic subsequence is "bb".
# 
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:        
        if s == s[::-1]:
            return len(s)
        sl = len(s)
        dp = [[0 for _ in range(sl+1)] for _ in range(sl+1)]
        res = 1
        for i in range(sl-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, sl):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                res = max(res, dp[i][j])
        return res
# @lc code=end
# "bbbab"
if __name__ == '__main__':
    s = Solution()
    s.longestPalindromeSubseq("bzycsdcxb")
