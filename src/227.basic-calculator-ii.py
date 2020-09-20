#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (35.08%)
# Likes:    1117
# Dislikes: 202
# Total Accepted:    156.3K
# Total Submissions: 436.6K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
# 
# Example 1:
# 
# 
# Input: "3+2*2"
# Output: 7
# 
# 
# Example 2:
# 
# 
# Input: " 3/2 "
# Output: 1
# 
# Example 3:
# 
# 
# Input: " 3+5 / 2 "
# Output: 5
# 
# 
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        stack,i,j = [],0,0
        while j < len(s):
            if s[j] in '+-':
                stack.append(int(s[i:j]))
                i, j = j, j+1
            elif s[j] in '*/':
                stack.append(int(s[i:j]))
                i, j = j, j+1
                while j < len(s) and s[i] in '*/':
                    n1,op = stack.pop(), s[i]
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    n2 = int(s[i+1:j])
                    stack.append(self.calc(n1,n2,op))
                    i, j = j, j+1
            else:
                j += 1
        if i < len(s):
            stack.append(int(s[i:]))
        return sum(stack)

    def calc(self, n1,n2,op) -> int:
        if op == '+':
            return n1+n2
        if op == '-':
            return n1-n2
        if op == '*':
            return n1*n2
        if op == '/':
            tmp = abs(n1)//abs(n2)
            return tmp if (n1 >= 0 and n2 > 0) or (n1 < 0 and n2 < 0) else -tmp
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.calculate("14-3/2")
    s.calculate("2*3*4")
    s.calculate("0")
    s.calculate("2*3+4")
    s.calculate("1-1+1")
    s.calculate("1 + 1")
    s.calculate("3+2*2")
    s.calculate(" 3+5 / 2 ")
