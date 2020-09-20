#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#
# https://leetcode.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (58.14%)
# Likes:    758
# Dislikes: 28
# Total Accepted:    26.9K
# Total Submissions: 46.1K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string S, compute the score of the string based
# on the following rule:
# 
# 
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "()"
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: "(())"
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: "()()"
# Output: 2
# 
# 
# 
# Example 4:
# 
# 
# Input: "(()(()))"
# Output: 6
# 
# 
# 
# 
# Note:
# 
# 
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:

    def scoreOfParentheses(self, S: str) -> int:
        if not S:
            return 0
        stack = []
        res = 0
        for s in S:
            if s == '(':
                stack.append(res)
                res = 0
            else:
                res += stack.pop() + max(res, 1)
        return res               
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.scoreOfParentheses('(()(()))')
