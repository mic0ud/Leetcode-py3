#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#
# https://leetcode.com/problems/satisfiability-of-equality-equations/description/
#
# algorithms
# Medium (41.84%)
# Likes:    304
# Dislikes: 3
# Total Accepted:    12.6K
# Total Submissions: 29.8K
# Testcase Example:  '["a==b","b!=a"]'
#
# Given an array equations of strings that represent relationships between
# variables, each string equations[i] has length 4 and takes one of two
# different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not
# necessarily different) that represent one-letter variable names.
# 
# Return true if and only if it is possible to assign integers to variable
# names so as to satisfy all the given equations.
 
# Example 1:

# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is
# satisfied, but not the second.  There is no way to assign the variables to
# satisfy both equations.
 
# Example 2:

# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

# Example 3:
 
# Input: ["a==b","b==c","a==c"]
# Output: true

# Example 4:

# Input: ["a==b","b!=c","c==a"]
# Output: false
 
# Example 5:
 
# Input: ["c==c","b==d","x!=z"]
# Output: true

# Note:

# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] and equations[i][3] are lowercase letters
# equations[i][1] is either '=' or '!'
# equations[i][2] is '='


# @lc code=start
from collections import defaultdict
class Solution:
    def equationsPossible(self, equations: [str]) -> bool:
        equals = {}
        for e in equations:
            if '==' in e:
                a,b = e.split('==')
                self.union(equals, a, b)
        for e in equations:
            if '!=' in e:
                a,b = e.split('!=')
                if self.find(equals, a) == self.find(equals, b):
                    return False
        return True     

    def union(self, root: {}, i, j):
        rooti = self.find(root, i)
        rootj = self.find(root, j)
        root[rootj] = rooti

    def find(self, root: {}, i):
        if i not in root:
            root[i] = i
        else:
            while root[i] != i:
                i = root[i]
        return i
# @lc code=end
# ["a==b","b!=c","c==a"]
if __name__ == '__main__':
    s = Solution()
    s.equationsPossible(["a==b","b!=c","c==a"])
