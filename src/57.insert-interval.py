#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (32.92%)
# Likes:    1545
# Dislikes: 179
# Total Accepted:    245.2K
# Total Submissions: 738.6K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
from bisect import bisect_right
class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        res, left, right = [], newInterval[0], newInterval[1]
        for l,r in intervals:
            if l <= newInterval[0] and r >= newInterval[1]:
                return intervals
            elif l < newInterval[1] and r >= newInterval[0]:
                left = min(left, l)
                right = max(right, r)
            elif r > newInterval[0] and l <= newInterval[1]:
                left = min(left, l)
                right = max(right, r)
            else:
                res.append([l,r])
        idx = bisect_right(res, [left,right])
        return res[:idx] + [[left,right]] + res[idx:]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.insert([[1,5]],[0,3])
    s.insert([[1,5]],[2,3])
    s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[0,1])
    s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])
