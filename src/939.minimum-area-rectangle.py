#
# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#
# https://leetcode.com/problems/minimum-area-rectangle/description/
#
# algorithms
# Medium (51.73%)
# Likes:    463
# Dislikes: 86
# Total Accepted:    34.8K
# Total Submissions: 66.9K
# Testcase Example:  '[[1,1],[1,3],[3,1],[3,3],[2,2]]'
#
# Given a set of points in the xy-plane, determine the minimum area of a
# rectangle formed from these points, with sides parallel to the x and y axes.
# 
# If there isn't any rectangle, return 0.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
# 
# 
# 
#

# @lc code=start
class Solution:
    def minAreaRect(self, points: [[int]]) -> int:
        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1-x2) * abs(y1-y2)
                    res = min(res, area)
            seen.add((x1,y1))
        return res if res < float('inf') else 0
# @lc code=end
# [[1,1],[1,3],[3,1],[3,3],[2,2]]
# [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
