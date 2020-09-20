#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
# https://leetcode.com/problems/minimum-height-trees/description/
#
# algorithms
# Medium (31.09%)
# Likes:    1506
# Dislikes: 85
# Total Accepted:    84K
# Total Submissions: 266.7K
# Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
#
# For an undirected graph with tree characteristics, we can choose any node as
# the root. The result graph is then a rooted tree. Among all possible rooted
# trees, those with minimum height are called minimum height trees (MHTs).
# Given such a graph, write a function to find all the MHTs and return a list
# of their root labels.
# 
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be
# given the number n and a list of undirected edges (each edge is a pair of
# labels).
# 
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
# 
# Example 1 :
# 
# 
# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
# 
# ⁠       0
# ⁠       |
# ⁠       1
# ⁠      / \
# ⁠     2   3 
# 
# Output: [1]
# 
# 
# Example 2 :
# 
# 
# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# 
# ⁠    0  1  2
# ⁠     \ | /
# ⁠       3
# ⁠       |
# ⁠       4
# ⁠       |
# ⁠       5 
# 
# Output: [3, 4]
# 
# Note:
# 
# 
# According to the definition of tree on Wikipedia: “a tree is an undirected
# graph in which any two vertices are connected by exactly one path. In other
# words, any connected graph without simple cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.


# @lc code=start
from collections import defaultdict
from queue import Queue
class Solution:
    def findMinHeightTrees(self, n: int, edges: [[int]]) -> [int]:
        if n == 0:
            return []
        if n < 3:
            return [i for i in range(n)]
        g = defaultdict(set)
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)
        leaves = [i for i in g if len(g[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                adj = g[leaf].pop()
                g[adj].remove(leaf)
                if len(g[adj]) == 1:
                    new_leaves.append(adj)
            leaves = new_leaves
        return leaves


    def findMinHeightTrees_SLOW(self, n: int, edges: [[int]]) -> [int]:
        if n == 0:
            return []
        if n < 3:
            return [i for i in range(n)]
        g = defaultdict(set)
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)
        removed = set()
        while len(removed) < n-2:
            tmp = set()
            for v in g:
                if len(g[v]) == 1:
                    tmp.add(v)
            for r in tmp:
                g[g[r].pop()].remove(r)
            removed = removed.union(tmp)
        return [i for i in range(n) if i not in removed]

    def findMinHeightTrees_TLE(self, n: int, edges: [[int]]) -> [int]:
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        def search(n) -> int:
            seen = set()
            q = Queue()
            q.put([n])
            h = -1
            while not q.empty():
                h += 1
                curr = q.get()
                next_ = []
                for c in curr:
                    seen.add(c)
                    for v in g[c]:
                        if v not in seen:
                            next_.append(v)
                if next_:
                    q.put(next_)
            return h
        res = defaultdict(list)
        for i in range(n):
            res[search(i)].append(i)
        return res[min(res.keys())]        
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
    s.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
    s.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])
