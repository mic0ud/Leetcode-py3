#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
#
# algorithms
# Hard (56.61%)
# Likes:    247
# Dislikes: 6
# Total Accepted:    9.4K
# Total Submissions: 16.4K
# Testcase Example:  '"zzazz"'
#
# Given a string s. In one step you can insert any character at any index of
# the string.
# 
# Return the minimum number of steps to make s palindrome.
# 
# A Palindrome String is one that reads the same backward as well as
# forward.
# 
# 
# Example 1:
# 
# 
# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we don't need any
# insertions.
# 
# 
# Example 2:
# 
# 
# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# 
# 
# Example 3:
# 
# 
# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
# 
# 
# Example 4:
# 
# 
# Input: s = "g"
# Output: 0
# 
# 
# Example 5:
# 
# 
# Input: s = "no"
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# All characters of s are lower case English letters.
# 
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
            if i+1 < n:
                dp[i][i+1] = 0 if s[i] == s[i+1] else 1
        for k in range(2, n):
            for i in range(n-k):
                dp[i][i+k] = min(dp[i][i+k-1], dp[i+1][i+k]) + 1
                if s[i] == s[i+k]:
                    dp[i][i+k] = min(dp[i][i+k], dp[i+1][i+k-1])
        return dp[0][-1]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minInsertions("ml")
    s.minInsertions("leetcode")
