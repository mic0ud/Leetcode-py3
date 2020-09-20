#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#
# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
#
# algorithms
# Easy (47.30%)
# Likes:    126
# Dislikes: 12
# Total Accepted:    14.3K
# Total Submissions: 30.4K
# Testcase Example:  '[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]'
#
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
# represents the coordinate of a point. Check if these points make a straight
# line in the XY plane.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.
# 
# 
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: [[int]]) -> bool:
        if len(coordinates) < 2:
            return False
        params = self.findLineFunction(coordinates[0], coordinates[1])
        for c in coordinates[2:]:
            if not self.checkCoordinate(params, c):
                return False
        return True
        
    def findLineFunction(self, c1, c2) -> [int]:
        slope = (c2[1]-c1[1])/(c2[0]-c1[0]) if c2[0] != c1[0] else float('inf')
        const = c1[1] - slope * c1[0] if slope != float('inf') else c1[0]
        return [slope, const]

    def checkCoordinate(self, params: [int], c: [int]) -> bool:
        slope, const = params[0], params[1]
        if slope == 0:
            return c[1] == const
        elif slope == float('inf'):
            return c[0] == const
        else:
            return c[1] == slope * c[0] + const
# @lc code=end

