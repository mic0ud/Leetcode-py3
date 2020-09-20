#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
# https://leetcode.com/problems/critical-connections-in-a-network/description/
#
# algorithms
# Hard (48.42%)
# Likes:    690
# Dislikes: 62
# Total Accepted:    34.2K
# Total Submissions: 70.4K
# Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
#
# There are n servers numbered from 0 to n-1 connected by undirected
# server-to-server connections forming a network where connections[i] = [a, b]
# represents a connection between servers a and b. Any server can reach any
# other server directly or indirectly through the network.
# 
# A critical connection is a connection that, if removed, will make some server
# unable to reach some other server.
# 
# Return all critical connections in the network in any order.

# Example 1:

# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.

# Constraints:

# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# There are no repeated connections.


# @lc code=start
class Solution:
    def criticalConnections(self, n: int, connections: [[int]]) -> [[int]]:
        adj, res = [[] for _ in range(n)], []
        for c1,c2 in connections:
            adj[c1].append(c2)
            adj[c2].append(c1)
        low, visited = [i for i in range(n)], [False for _ in range(n)]
        def search(curr, prev, depth):
            visited[curr] = True
            low[curr] = depth
            for j in adj[curr]:
                if j != prev:
                    if not visited[j]:
                        search(j, curr, depth+1)
                    low[curr] = min(low[curr], low[j])
                    if low[j] >= depth + 1:
                        res.append([curr if curr < j else j, j if j > curr else curr])
        search(0,-1,0)
        return res

    def criticalConnections_WRONG(self, n: int, connections: [[int]]) -> [[int]]:
        adj = [[] for _ in range(n)]
        for c1,c2 in connections:
            adj[c1].append(c2)
            adj[c2].append(c1)
        res = []
        for i in range(n):
            if len(adj[i]) == 1:
                res.append([i, adj[i][0]])
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.criticalConnections(10,[[1,0],[2,0],[3,0],[4,1],[5,3],[6,1],[7,2],[8,1],[9,6],[9,3],[3,2],[4,2],[7,4],[6,2],[8,3],[4,0],[8,6],[6,5],[6,3],[7,5],[8,0],[8,5],[5,4],[2,1],[9,5],[9,7],[9,4],[4,3]])
    s.criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]])
    s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])
