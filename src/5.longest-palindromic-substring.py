#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        dp = [[False] * len(s)  for i in range(s_len)]
        res = ""
        for i in range(s_len-1,-1,-1):
            for j in range(i,s_len):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])
                if(dp[i][j] and j - i + 1 > len(res)):
                    res = s[i:j+1]
        return res
# @lc code=end

