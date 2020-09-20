#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (52.33%)
# Likes:    1364
# Dislikes: 68
# Total Accepted:    91.9K
# Total Submissions: 172.4K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
# 
# Example 1:
# 
# 
# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# Example 2:
# 
# 
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str) -> [int]:
        memo = {}
        def dfs(s) -> [int]:
            if s in memo:
                return memo[s]
            if s.isdigit():
                memo[s] = [int(s)]
                return memo[s]            
            res = []
            for i in range(len(s)):
                if s[i] in '+-*':
                    res1 = dfs(s[:i])
                    res2 = dfs(s[i+1:])
                    for r1 in res1:
                        for r2 in res2:
                            res.append(calc(r1,r2,s[i]))
            memo[s] = res
            return res

        def calc(n1,n2,op) -> int:
            if op == '+':
                return n1+n2
            if op == '-':
                return n1-n2
            if op == '*':
                return n1*n2

        res = dfs(input)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.diffWaysToCompute("2*3-4*5")
