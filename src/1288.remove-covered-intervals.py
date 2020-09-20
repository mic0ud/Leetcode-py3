#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#
# https://leetcode.com/problems/remove-covered-intervals/description/
#
# algorithms
# Medium (61.66%)
# Likes:    154
# Dislikes: 9
# Total Accepted:    9.4K
# Total Submissions: 15.9K
# Testcase Example:  '[[1,4],[3,6],[2,8]]'
#
# Given a list of intervals, remove all intervals that are covered by another
# interval in the list. Interval [a,b) is covered by interval [c,d) if and only
# if c <= a and b <= d.
# 
# After doing so, return the number of remaining intervals.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 1000
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# intervals[i] != intervals[j] for all i != j
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def removeCoveredIntervals(self, intervals: [[int]]) -> int:
        span = defaultdict(int)
        for i,j in intervals:
            span[i] = max(span[i], j)
        starts = sorted(span.keys())
        right_max = span[starts[0]]
        for s in starts[1:]:
            if span[s] <= right_max:
                span.pop(s)
            else:
                right_max = span[s]
        return len(span)

    def removeCoveredIntervals_SLOW(self, intervals: [[int]]) -> int:
        span = defaultdict(int)
        for i,j in intervals:
            span[i] = max(span[i], j)
        starts = sorted(span.keys())
        for i in range(len(starts)-1):
            if starts[i] in span:
                for j in range(i+1, len(starts)):
                    if starts[j] in span and span[starts[j]] <= span[starts[i]]:
                        span.pop(starts[j])
        return len(span)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.removeCoveredIntervals([[3,10],[4,10],[5,11]])
    s.removeCoveredIntervals([[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]])
    s.removeCoveredIntervals([[1,4],[3,6],[2,8]])
