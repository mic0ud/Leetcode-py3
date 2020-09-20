#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (33.94%)
# Likes:    710
# Dislikes: 407
# Total Accepted:    191.7K
# Total Submissions: 562.6K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# Note:
# 
# 
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
# 
# 
# Example 1:
# 
# 
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        if not tokens:
            return 0
        stack = []
        for t in tokens:
            if t in ['+','-','*','/']:
                op2 = stack.pop()
                op1 = stack.pop()
                tmp = 0                
                if t == '+':
                    tmp = op1 + op2
                elif t == '-':
                    tmp = op1 - op2
                elif t == '*':
                    tmp = op1 * op2
                else:
                    sign = 1 if (op1 > 0 and op2 > 0) or (op1 < 0 and op2 < 0) else -1
                    tmp = sign * (abs(op1) // abs(op2))
                stack.append(tmp)
            else:
                stack.append(int(t))
        return stack.pop()
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
