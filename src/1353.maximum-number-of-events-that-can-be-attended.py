#
# @lc app=leetcode id=1353 lang=python3
#
# [1353] Maximum Number of Events That Can Be Attended
#
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/
#
# algorithms
# Medium (32.39%)
# Likes:    331
# Dislikes: 49
# Total Accepted:    10K
# Total Submissions: 31.9K
# Testcase Example:  '[[1,2],[2,3],[3,4]]\r'
#
# Given an array of events where events[i] = [startDayi, endDayi]. Every event
# i starts at startDayi and ends at endDayi.
# 
# You can attend an event i at any day d where startTimei <= d <= endTimei.
# Notice that you can only attend one event at any time d.
# 
# Return the maximum number of events you can attend.
# 
# 
# Example 1:
# 
# 
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.
# 
# 
# Example 2:
# 
# 
# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: events = [[1,100000]]
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# 1 <= events.length <= 10^5
# events[i].length == 2
# 1 <= events[i][0] <= events[i][1] <= 10^5


# @lc code=start
from functools import cmp_to_key
import heapq
class Solution:
    def maxEvents(self, events: [[int]]) -> int:
        events.sort(reverse=True)
        h = []
        res = d = 0
        while events or h:
            if not h:
                d = events[-1][0]
            while events and events[-1][0] <= d:
                heapq.heappush(h, events.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res
        
    def my_cmp(self, e1, e2) -> int:
        if e1[0] == e2[0]:
            return e1[1]-e2[1]
        else:
            return e1[0]-e2[0]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.maxEvents([[25,26],[19,19],[9,13],[16,17],[17,18],[20,21],[22,25],[11,12],[19,23],[7,9],[1,1],[21,23],[14,14],[4,7],[16,16],[24,28],[16,18],[4,5],[18,20],[16,16],[25,26]])
    s.maxEvents([[1,2],[1,2],[1,6],[1,2],[1,2]])
    s.maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]])
    s.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]])
    s.maxEvents([[1,1],[2,2],[1,3],[2,4],[1,5],[2,6],[1,7]])
    s.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]])
