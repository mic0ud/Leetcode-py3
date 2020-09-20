#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (33.51%)
# Likes:    891
# Dislikes: 29
# Total Accepted:    39.7K
# Total Submissions: 117.4K
# Testcase Example:  '"()"'
#
# 
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
# 
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
# 
# 
# 
# Example 1:
# 
# Input: "()"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "(*)"
# Output: True
# 
# 
# 
# Example 3:
# 
# Input: "(*))"
# Output: True
# 
# 
# 
# Note:
# 
# The string size will be in the range [1, 100].


# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        # cmin: '(' must be closed, cmax: '(' could be closed
        # conditions: 1. cmin == 0, 2. cmax >= 0
        cmin, cmax = 0, 0 
        for c in s:
            if c == '(':
                cmin += 1
                cmax += 1
            elif c == ')':
                cmin = max(cmin-1, 0)
                cmax -= 1
            elif c == '*':
                cmin = max(cmin-1, 0)
                cmax += 1
            if cmax < 0:
                return False
        return cmin == 0
# @lc code=end

