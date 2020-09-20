#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (72.28%)
# Likes:    593
# Dislikes: 49
# Total Accepted:    44K
# Total Submissions: 60.1K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.
# 
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
# 
# 
# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# Note:
# 
# 
# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of
# nodes inside one path.
# 
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: [[int]]) -> [[int]]:
        if not graph or not graph[0]:
            return []
        visiting = [False for _ in range(len(graph))]
        def dfs(i, path, res):
            path.append(i)
            if i == len(graph)-1:
                res.add(tuple(path))
            else:
                visiting[i] = True            
                for j in graph[i]:
                    if not visiting[j]:
                        dfs(j, list(path), res)
                        visiting[i] = False
        res = set()
        dfs(0,[],res)
        return [list(r) for r in res]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])
    s.allPathsSourceTarget([[1,2], [3], [3], []])
