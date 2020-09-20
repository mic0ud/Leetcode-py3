#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (58.46%)
# Likes:    1835
# Dislikes: 94
# Total Accepted:    136.1K
# Total Submissions: 232.3K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# 
# Note:
# 
# 
# The input string length won't exceed 1000.
# 
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        sl = len(s)
        dp = [[False for _ in range(sl+1)] for _ in range(sl+1)]
        count = sl
        for i in range(sl-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, sl):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        return count
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.countSubstrings("aaaaaa")