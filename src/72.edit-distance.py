#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (40.21%)
# Likes:    2887
# Dislikes: 44
# Total Accepted:    218.3K
# Total Submissions: 534.3K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following 3 operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        m = len(word1)
        n = len(word2)
        # dp[i][j]: minimum cost (or steps) required to convert first i characters of word1 to first j characters of word2
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1],dp[i-1][j]) + 1
        return dp[-1][-1]
# @lc code=end

