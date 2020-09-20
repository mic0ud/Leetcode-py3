#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (41.89%)
# Likes:    791
# Dislikes: 29
# Total Accepted:    59.5K
# Total Submissions: 141K
# Testcase Example:  '[[1,2]]'
#
# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.

# Example 1:
# 
# 
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are
# non-overlapping.
# 
# 
# Example 2:
# 
# 
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals
# non-overlapping.
# 
# 
# Example 3:
# 
# 
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.

# Note:
# 
# 
# You may assume the interval's end point is always bigger than its start
# point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap
# each other.

# @lc code=start
from collections import defaultdict
from operator import itemgetter 
class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        n = len(intervals)
        if n < 2:
            return 0
        m = defaultdict(list)
        for i in intervals:
            m[i[1]].append(i)
        res, prev = 0, float('-inf')
        for k in sorted(m.keys()):
            m[k].sort(key=itemgetter(0))
            count = len(m[k]) - 1
            if m[k][-1][0] < prev:
                count += 1
            if count < len(m[k]):
                prev = k
            res += count
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])
    # s.eraseOverlapIntervals([[1,2],[2,3]])
    # s.eraseOverlapIntervals([[1,2],[1,2],[1,2]])
    # s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
