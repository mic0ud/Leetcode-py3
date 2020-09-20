#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#
# https://leetcode.com/problems/remove-outermost-parentheses/description/
#
# algorithms
# Easy (75.71%)
# Likes:    273
# Dislikes: 412
# Total Accepted:    59.6K
# Total Submissions: 78.5K
# Testcase Example:  '"(()())(())"'
#
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
# where A and B are valid parentheses strings, and + represents string
# concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid
# parentheses strings.
# 
# A valid parentheses string S is primitive if it is nonempty, and there does
# not exist a way to split it into S = A+B, with A and B nonempty valid
# parentheses strings.
# 
# Given a valid parentheses string S, consider its primitive decomposition: S =
# P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
# 
# Return S after removing the outermost parentheses of every primitive string
# in the primitive decomposition of S.
# 
# 
# 
# Example 1:
# 
# 
# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" +
# "(())".
# After removing outer parentheses of each part, this is "()()" + "()" =
# "()()()".
# 
# 
# 
# Example 2:
# 
# 
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition
# "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" +
# "()(())" = "()()()()(())".
# 
# 
# 
# Example 3:
# 
# 
# Input: "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 10000
# S[i] is "(" or ")"
# S is a valid parentheses string
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        stack = []
        start = 0
        for i in range(len(S)):
            if not stack:
                stack.append(S[i])
            else:
                if stack[-1] == '(' and S[i] == ')':
                    stack.pop()
                else:
                    stack.append(S[i])
            if not stack and i > 0:
                res.append(S[start:i+1])
                start = i + 1
        resStr = ''
        for s in res:
            resStr += s[1:-1]
        return resStr
# @lc code=end

