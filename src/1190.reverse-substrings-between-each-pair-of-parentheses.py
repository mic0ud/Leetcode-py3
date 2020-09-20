#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
#
# algorithms
# Medium (57.84%)
# Likes:    201
# Dislikes: 8
# Total Accepted:    10.9K
# Total Submissions: 18.4K
# Testcase Example:  '"(abcd)"'
#
# You are given a string s that consists of lower case English letters and
# brackets. 
# 
# Reverse the strings in each pair of matching parentheses, starting from the
# innermost one.
# 
# Your result should not contain any brackets.
# 
# 
# Example 1:
# 
# 
# Input: s = "(abcd)"
# Output: "dcba"
# 
# 
# Example 2:
# 
# 
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is
# reversed.
# 
# 
# Example 3:
# 
# 
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally,
# the whole string.
# 
# 
# Example 4:
# 
# 
# Input: s = "a(bcdefghijkl(mno)p)q"
# Output: "apmnolkjihgfedcbq"
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 2000
# s only contains lower case English characters and parentheses.
# It's guaranteed that all parentheses are balanced.
# 
# 
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        opened = []
        pair = {}
        for i in range(len(s)):
            if s[i] == '(':
                opened.append(i)
            elif s[i] == ')':
                j = opened.pop()
                pair[i], pair[j] = j, i
        res = []
        i, d = 0, 1 # d is the direction: left -> 1, right <- -1
        while i < len(s):
            if s[i] in '()':
                i = pair[i] # go the end/begginning of the pair
                d = -d # every time there is '(' or ')', change the direction
            else:
                res.append(s[i])
            i += d
        return ''.join(res)

    def reverseParentheses_SLOW(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            else:
                tmp = []
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                if stack: stack.pop()
                for t in tmp:
                    stack.append(t)
        return ''.join(stack)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.reverseParentheses("a(bcdefghijkl(mno)p)q")
