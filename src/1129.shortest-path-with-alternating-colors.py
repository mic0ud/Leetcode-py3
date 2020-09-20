#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#
# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
#
# algorithms
# Medium (37.10%)
# Likes:    182
# Dislikes: 10
# Total Accepted:    7.4K
# Total Submissions: 19.9K
# Testcase Example:  '3\n[[0,1],[1,2]]\n[]'
#
# Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this
# graph, each edge is either red or blue, and there could be self-edges or
# parallel edges.
# 
# Each [i, j] in red_edges denotes a red directed edge from node i to node j.
# Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i
# to node j.
# 
# Return an array answer of length n, where each answer[X] is the length of the
# shortest path from node 0 to node X such that the edge colors alternate along
# the path (or -1 if such a path doesn't exist).
# 
# 
# Example 1:
# Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# Output: [0,1,-1]
# Example 2:
# Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# Output: [0,1,-1]
# Example 3:
# Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
# Output: [0,-1,-1]
# Example 4:
# Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
# Output: [0,1,2]
# Example 5:
# Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
# Output: [0,1,1]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 100
# red_edges.length <= 400
# blue_edges.length <= 400
# red_edges[i].length == blue_edges[i].length == 2
# 0 <= red_edges[i][j], blue_edges[i][j] < n
# 
#

# @lc code=start
from collections import defaultdict
from queue import Queue
class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        G = [[[], []] for i in range(n)]
        for i, j in red_edges: G[i][0].append(j)
        for i, j in blue_edges: G[i][1].append(j)
        res = [[0, 0]] + [[n * 2, n * 2] for i in range(n - 1)]
        bfs = [[0, 0], [0, 1]]
        for i, c in bfs:
            for j in G[i][c]:
                if res[j][c] == n * 2:
                    res[j][c] = res[i][1 - c] + 1
                    bfs.append([j, 1 - c])
        return [x if x < n * 2 else -1 for x in map(min, res)]

    def shortestAlternatingPaths_SLOW(self, n: int, red_edges: [[int]], blue_edges: [[int]]) -> [int]:
        # dp[i]: shortest path from 0 to i
        dp = [-1 for _ in range(n)]
        dp[0] = 0
        red = defaultdict(list)
        blue = defaultdict(list)
        for r in red_edges:
            red[r[0]].append(r[1])
        for b in blue_edges:
            blue[b[0]].append(b[1])
        
        def search(i, fromRed: True) -> int:
            q = Queue()
            q.put(red[0] if fromRed else blue[0])
            isRed = not fromRed
            steps = 0
            visited_red = [False for _ in range(n)]
            visited_blue = [False for _ in range(n)]
            while not q.empty():
                vs = q.get()
                steps += 1
                next_ = []
                for v in vs:
                    if v == i:
                        return steps
                    if isRed:
                        visited_blue[v] = True
                    else:
                        visited_red[v] = True
                    tmp = red[v] if isRed else blue[v]                    
                    for w in tmp:
                        if not (visited_red[w] if isRed else visited_blue[w]):
                            next_.append(w)
                isRed = not isRed
                if next_:
                    q.put(next_)
            return -1
        for i in range(1, n):
            r = search(i, True)
            b = search(i, False)
            res = float('inf')
            if r == -1 and b == -1:
                res = -1
            elif r == -1:
                res = b
            elif b == -1:
                res = r
            else:
                res = min(r,b)
            dp[i] = res
        return dp
# @lc code=end
# 5\n[[0,1],[1,2],[2,3],[3,4]]\n[[1,2],[2,3],[3,1]]
# 5\n[[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]]\n[[1,3],[0,0],[0,3],[4,2],[1,0]]
if __name__ == '__main__':
    s = Solution()
    s.shortestAlternatingPaths(5,[[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]],[[1,3],[0,0],[0,3],[4,2],[1,0]])
