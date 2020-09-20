#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#
# https://leetcode.com/problems/corporate-flight-bookings/description/
#
# algorithms
# Medium (49.59%)
# Likes:    314
# Dislikes: 57
# Total Accepted:    12.8K
# Total Submissions: 25.3K
# Testcase Example:  '[[1,2,10],[2,3,20],[2,5,25]]\n5'
#
# There are n flights, and they are labeled from 1 to n.
# 
# We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k]
# means that we booked k seats from flights labeled i to j inclusive.
# 
# Return an array answer of length n, representing the number of seats booked
# on each flight in order of their label.
# 
# 
# Example 1:
# 
# 
# Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# Output: [10,55,45,25,25]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= bookings.length <= 20000
# 1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
# 1 <= bookings[i][2] <= 10000
# 
#

# @lc code=start
# from collections import defaultdict
from operator import itemgetter
# import bisect
class Solution:
    def corpFlightBookings(self, bookings: [[int]], n: int) -> [int]:
        if not bookings or not bookings[0] or n == 0:
            return [0]
        startEnd = [[0,0] for _ in range(n+1)] # 0: start, 1: end
        for b in bookings:   
            startEnd[b[0]][0] += b[2]
            startEnd[b[1]][1] += b[2]
        res = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            res[i] = res[i-1] + startEnd[i][0] - startEnd[i-1][1]  
        return res[1:]

    def corpFlightBookings_TLE(self, bookings: [[int]], n: int) -> [int]:
        if not bookings or not bookings[0] or n == 0:
            return [0]
        res = [0 for _ in range(n+1)]
        bookings = sorted(bookings, key=itemgetter(0))
        for b in bookings:
            for k in range(b[0],b[1]+1):
                res[k] += b[2]
        return res[1:]
# @lc code=end
# [[2,2,30],[2,2,45]]\n2
if __name__ == '__main__':
    s = Solution()
    s.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5)