#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Medium (44.70%)
# Likes:    1052
# Dislikes: 202
# Total Accepted:    66.6K
# Total Submissions: 147.3K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# There are N network nodes, labelled 1 to N.
# 
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
# 
# Now, we send a signal from a certain node K. How long will it take for all
# nodes to receive the signal? If it is impossible, return -1.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
# 
# 
#

# @lc code=start
from collections import defaultdict
import heapq, queue
class Solution:
    def networkDelayTime(self, times: [[int]], N: int, K: int) -> int:
        g, pq, distance = defaultdict(list), [], [0 if i == K or i == 0 else float('inf') for i in range(N+1)]
        for t in times:
            g[t[0]].append(t[1:])        
        for t in g[K]:
            heapq.heappush(pq, (t[1], t[0]))
        while pq:
            time, node = heapq.heappop(pq)
            if distance[node] == float('inf'):
                distance[node] = time
                for v, t in g[node]:
                    heapq.heappush(pq, (t+time, v))
        res = max(distance)
        return res if res < float('inf') else -1

    def networkDelayTime_SLOW(self, times: [[int]], N: int, K: int) -> int:
        g, visited, res = defaultdict(list), set(), [0 if i == K or i == 0 else float('inf') for i in range(N+1)]
        for t in times:
            g[t[0]].append(t)
        q = queue.Queue()
        q.put(g[K])
        while not q.empty():
            targets = q.get()
            next_ = []
            for t in targets:
                if tuple(t[:2]) in visited:
                    continue
                visited.add(tuple(t[:2]))
                res[t[1]] = min(res[t[1]], res[t[0]]+t[2])
                for e in g[t[1]]:
                    res[e[1]] = min(res[e[1]], res[e[0]]+e[2])
                    if tuple(e[:2]) not in visited:
                        next_.append(e)
            if next_:
                q.put(next_)
        total = max(res)
        return total if total < float('inf') else -1
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.networkDelayTime([[1,2,1],[2,1,3]],2,2)
    # s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,1)
    s.networkDelayTime([[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]],5,3)
