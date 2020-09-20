#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (36.67%)
# Likes:    1087
# Dislikes: 39
# Total Accepted:    60.6K
# Total Submissions: 164.7K
# Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
#
# There are n cities connected by m flights. Each fight starts from city u and
# arrives at v with a price w.
# 
# Now given all the cities and flights, together with starting city src and the
# destination dst, your task is to find the cheapest price from src to dst with
# up to k stops. If there is no such route, output -1.
# 
# 
# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.
# 
# 
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
# 
# Note:
# 
# 
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
# n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
# 
# 
#

# @lc code=start
import heapq, collections
class Solution:
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, K: int) -> int:
        city = collections.defaultdict(list)
        for f in flights:
            city[f[0]].append([f[2],f[1]])
        pq = []
        for e in city[src]:
            heapq.heappush(pq, tuple(e+[0])) # 0 stop
        while pq:
            price, d, stops = heapq.heappop(pq)
            if d == dst:
                return price
            if stops < K:
                for e in city[d]:
                    heapq.heappush(pq, (e[0]+price, e[1], stops+1))
        return -1


    def findCheapestPrice_(self, n: int, flights: [[int]], src: int, dst: int, K: int) -> int:
        cityMap = collections.defaultdict(dict)
        for f in flights:
            if f[0] in cityMap.keys():
                cityMap[f[0]].append([f[1],f[2]])
            else:
                cityMap[f[0]] = [[f[1],f[2]]]
        heap = []
        heapq.heappush(heap, (0, src, K+1))
        while heap:
            price, d, stops = heapq.heappop(heap)
            if d == dst:
                return price
            if stops > 0:
                for item in cityMap[d]:
                    heapq.heappush(heap, (price+item[1], item[0], stops-1))
        return -1
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1)
    # s.findCheapestPrice(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1)
