#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.57%)
# Likes:    3702
# Dislikes: 179
# Total Accepted:    771.9K
# Total Submissions: 2M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for c2 in s:
            c1 = stack[-1] if stack else None
            if self.isClosing(c1, c2):
                stack.pop()
            else:
                stack.append(c2)
        return len(stack) == 0

    def isClosing(self, c1, c2) -> bool:
        if (c1 == '(' and c2 == ')') or (c1 == '{' and c2 == '}') or (c1 == '[' and c2 == ']'):
            return True
        return False
# @lc code=end
# "()[]{}"
if __name__ == '__main__':
    s = Solution()
    s.isValid("()[]{}")