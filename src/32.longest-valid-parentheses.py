#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (26.74%)
# Likes:    2678
# Dislikes: 119
# Total Accepted:    242.6K
# Total Submissions: 894.2K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return n
        tmp1 = n
        res = 0
        while stack:
            tmp2 = stack.pop()
            res = max(res, tmp1-tmp2-1)
            tmp1 = tmp2
        res = max(res, tmp2)
        return res 

    def longestValidParentheses_WRONG(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        # dp[i][j]: if s[i:j] is valid parentheses
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = 0
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if s[i] == '(' and s[j] == ')' and (j - i == 1 or dp[i+2][j] or dp[i+1][j-1]):
                    dp[i][j] = True
                if dp[i][j] and j-i+1 > res:
                    res = j-i+1
        return res
# @lc code=end
# ")()())"
# "((()))())"
if __name__ == '__main__':
    s = Solution()
    s.longestValidParentheses(")()())")