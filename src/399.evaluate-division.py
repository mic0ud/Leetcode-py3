#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (49.27%)
# Likes:    1871
# Dislikes: 143
# Total Accepted:    110.8K
# Total Submissions: 221.5K
# Testcase Example:  '[["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# Equations are given in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given  a / b = 2.0, b / c = 3.0.
# queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
# 
# According to the example above:
# 
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]
# ]. 
# 
# 
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: [[str]], values: [float], queries: [[str]]) -> [float]:
        memo = defaultdict(defaultdict) # {'a':{'b':3.0, 'c':1.0}}
        for i,v in enumerate(equations):
            memo[v[0]][v[1]] = values[i]
            memo[v[1]][v[0]] = 1/values[i] if values[i] != 0 else float(-1)

        def calc(i,j,curr,seen) -> float:
            seen.add(i)
            if j in memo[i]:
                return memo[i][j] * curr
            for t, v in memo[i].items():
                if t not in seen:
                    tmp = calc(t,j,curr*v,seen)
                    if tmp != -1:
                        return tmp
            return float(-1)

        res = []
        for i,j in queries:
            # if i == j:
            #     res.append(float(1))
            if i not in memo or j not in memo:
                res.append(float(-1))
            else:
                seen = set()
                res.append(calc(i,j,1,seen))
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.calcEquation([ ["a", "b"], ["b", "c"] ],[2.0, 3.0],[ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
