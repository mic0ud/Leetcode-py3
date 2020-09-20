#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (37.22%)
# Likes:    2818
# Dislikes: 222
# Total Accepted:    449K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        i = 0
        intervals = sorted(intervals, key=lambda j: j[0])
        while i < len(intervals) - 1:
            if intervals[i][0] > intervals[i+1][-1] or intervals[i+1][0] > intervals[i][-1]:
                i += 1
            else:
                intervals[i] = [min(intervals[i][0], intervals[i+1][0]), max(intervals[i][-1], intervals[i+1][-1])]
                intervals.remove(intervals[i+1])               
        return intervals

# @lc code=end

