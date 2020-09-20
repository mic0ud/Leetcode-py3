#
# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#
# https://leetcode.com/problems/strange-printer/description/
#
# algorithms
# Hard (38.24%)
# Likes:    312
# Dislikes: 41
# Total Accepted:    11.5K
# Total Submissions: 30K
# Testcase Example:  '"aaabbb"'
#
# 
# There is a strange printer with the following two special requirements:
# 
# 
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending
# at any places, and will cover the original existing characters.
# 
# 
# 
# 
# 
# Given a string consists of lower English letters only, your job is to count
# the minimum number of turns the printer needed in order to print it.
# 
# 
# Example 1:
# 
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# 
# 
# 
# Example 2:
# 
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of
# the string, which will cover the existing character 'a'.
# 
# 
# 
# Hint: Length of the given string will not exceed 100.
#

# @lc code=start
from collections import defaultdict
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        # dp[i][j]: min count to print s[i:j+1]
        dp = [[0 for _ in range(n)] for _ in range(n)]

        def turn(i, j) -> int:
            if i > j:
                return 0
            if dp[i][j] > 0:
                return dp[i][j]
            tmpRes = turn(i, j-1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    tmpRes = min(tmpRes, turn(i,k)+turn(k+1,j-1))
            dp[i][j] = tmpRes
            return tmpRes

        turn(0,n-1)
        return dp[0][n-1]
# @lc code=end
# abbabca
if __name__ == '__main__':
    s = Solution()
    s.strangePrinter('abbabca')