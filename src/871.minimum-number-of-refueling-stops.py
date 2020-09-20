#
# @lc app=leetcode id=871 lang=python3
#
# [871] Minimum Number of Refueling Stops
#
# https://leetcode.com/problems/minimum-number-of-refueling-stops/description/
#
# algorithms
# Hard (30.38%)
# Likes:    500
# Dislikes: 9
# Total Accepted:    12.2K
# Total Submissions: 39.8K
# Testcase Example:  '1\n1\n[]'
#
# A car travels from a starting position to a destination which is target miles
# east of the starting position.
# 
# Along the way, there are gas stations.  Each station[i] represents a gas
# station that is station[i][0] miles east of the starting position, and has
# station[i][1] liters of gas.
# 
# The car starts with an infinite tank of gas, which initially has startFuel
# liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.
# 
# When the car reaches a gas station, it may stop and refuel, transferring all
# the gas from the station into the car.
# 
# What is the least number of refueling stops the car must make in order to
# reach its destination?  If it cannot reach the destination, return -1.
# 
# Note that if the car reaches a gas station with 0 fuel left, the car can
# still refuel there.  If the car reaches the destination with 0 fuel left, it
# is still considered to have arrived.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.
# 
# 
# 
# Example 2:
# 
# 
# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can't reach the target (or even the first gas station).
# 
# 
# 
# Example 3:
# 
# 
# Input: target = 100, startFuel = 10, stations =
# [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation: 
# We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0
# liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach
# the target.
# We made 2 refueling stops along the way, so we return 2.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= target, startFuel, stations[i][1] <= 10^9
# 0 <= stations.length <= 500
# 0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] <
# target
# 
# 
# 
# 
# 
#

# @lc code=start
from operator import itemgetter
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: [[int]]) -> int:
        if startFuel >= target:
            return 0
        if target > startFuel and not stations:
            return -1
        pq = []
        res = i = 0
        curr = startFuel
        while curr < target:
            while i < len(stations) and stations[i][0] <= curr:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq:
                return -1
            curr += -heapq.heappop(pq)
            res += 1

        return res

    def minRefuelStops_DP_SLOW(self, target: int, startFuel: int, stations: [[int]]) -> int:
        if startFuel >= target:
            return 0
        if target > startFuel and not stations:
            return -1
        # stations.sort(key=itemgetter(0))
        # dp[i]: the largest distance with i times of refueling
        dp = [startFuel for _ in range(len(stations)+1)]
        for i in range(len(stations)):
            for j in range(i,-1,-1):
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j]+stations[i][1])
        for i in range(len(dp)):
            if dp[i] >= target:
                return i
        return -1    

    def minRefuelStops_TLE(self, target: int, startFuel: int, stations: [[int]]) -> int:
        if startFuel >= target:
            return 0
        if target > startFuel and not stations:
            return -1
        stations.sort(key=itemgetter(0))

        def dfs(left: int, f: int, i: int, count: int, res: [int]) -> bool:
            if f >= left:
                res.append(count)
                return True
            if i >= len(stations) and left > f:
                return False
            done = target - left
            reached = False
            for s in range(i+1, len(stations)):
                if done < stations[s][0] <= done+f:
                    if dfs(target-stations[s][0], done+f-stations[s][0]+stations[s][1], s, count+1, res):
                        reached = True
            return reached
        res = []
        if dfs(target, startFuel, -1, 0, res):
            return min(res)
        return -1
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.minRefuelStops(100,50,[[25,25],[50,50]]))
