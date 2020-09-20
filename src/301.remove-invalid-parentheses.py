#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (40.95%)
# Likes:    1951
# Dislikes: 81
# Total Accepted:    165.6K
# Total Submissions: 401.2K
# Testcase Example:  '"()())()"'
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
# 
# Note: The input string may contain letters other than the parentheses ( and
# ).
# 
# Example 1:
# 
# 
# Input: "()())()"
# Output: ["()()()", "(())()"]
# 
# 
# Example 2:
# 
# 
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# 
# 
# Example 3:
# 
# 
# Input: ")("
# Output: [""]
# 
#

# @lc code=start
from queue import Queue
class Solution:
    def removeInvalidParentheses(self, s: str) -> [str]:
        if not s or self.isValid(s):
            return [s]
        q = Queue()
        q.put([s])
        res = set()
        while not q.empty():
            inputs = q.get()
            next_ = set()
            found = False
            for ss in inputs:                
                for i in range(len(ss)):
                    if ss[i] == '(' or ss[i] == ')':
                        tmp = ss[:i]+ss[i+1:]
                        if self.isValid(tmp):
                            res.add(tmp)
                            found = True
                        next_.add(tmp)
            if found:
                return list(res)
            if next_:
                q.put(next_)
        return list(res)

    def isValid(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == '(':
                count += 1
            if c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0    
# @lc code=end
# ["k()","(k)"]
if __name__ == '__main__':
    s = Solution()
    # print(s.isValid(''))
    print(s.removeInvalidParentheses("(((k()(("))
