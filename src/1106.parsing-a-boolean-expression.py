#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#
# https://leetcode.com/problems/parsing-a-boolean-expression/description/
#
# algorithms
# Hard (57.57%)
# Likes:    156
# Dislikes: 10
# Total Accepted:    6.9K
# Total Submissions: 12K
# Testcase Example:  '"!(f)"'
#
# Return the result of evaluating a given boolean expression, represented as a
# string.
# 
# An expression can either be:
# 
# 
# "t", evaluating to True;
# "f", evaluating to False;
# "!(expr)", evaluating to the logical NOT of the inner expression expr;
# "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner
# expressions expr1, expr2, ...;
# "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner
# expressions expr1, expr2, ...
# 
# 
# 
# Example 1:
# 
# 
# Input: expression = "!(f)"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: expression = "|(f,t)"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: expression = "&(t,f)"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: expression = "|(&(t,f,t),!(t))"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= expression.length <= 20000
# expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f',
# ','}.
# expression is a valid expression representing a boolean, as given in the
# description.
# 
# 
#

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for s in expression:
            if s == ')':
                e = []
                while stack[-1] != '(':
                    e.append(stack.pop())
                stack.pop()
                op = stack.pop()
                oneExpRes = all(e) if op == '&' else any(e) if op == '|' else not e[-1]
                stack.append(oneExpRes)
            elif s != ',':
                stack.append(True if s == 't' else False if s == 'f' else s)
        return stack.pop()
    
    def cheat(self, expression: str) -> bool:
        e = expression.replace('t', ' True ').replace('f', ' False ').replace('&(', ' all([').replace('!', ' not |').replace('|(', ' any([').replace(')', '])')
        return eval(e)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.cheat("!(f)")
