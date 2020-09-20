#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (58.13%)
# Likes:    4039
# Dislikes: 224
# Total Accepted:    463.2K
# Total Submissions: 777.9K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if n == 0:
            return []
        count = [0, 0]
        def dfs(i, s, res: ()):
            if i == 2*n:
                res.add(s)
                return
            if i == 0:
                count[0] += 1
                dfs(i+1, '(', res)
                count[0] -= 1
            elif i == 2*n-1:
                count[1] += 1
                dfs(i+1, s+')', res)
                count[1] -= 1
            else:
                if count[0] == n:
                    count[1] += 1
                    dfs(i+1, s+')', res)
                    count[1] -= 1
                elif count[0] == count[1]:
                    count[0] += 1
                    dfs(i+1, s+'(', res)
                    count[0] -= 1
                elif count[0] > count[1]:
                    count[0] += 1
                    dfs(i+1, s+'(', res)
                    count[0] -= 1
                    count[1] += 1
                    dfs(i+1, s+')', res)
                    count[1] -= 1

        res = set()
        dfs(0, '', res)
        return list(res)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.generateParenthesis(3)
