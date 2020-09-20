#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
#
# algorithms
# Medium (47.61%)
# Likes:    646
# Dislikes: 33
# Total Accepted:    49.3K
# Total Submissions: 103.2K
# Testcase Example:  '[[10,16],[2,8],[1,6],[7,12]]'
#
# There are a number of spherical balloons spread in two-dimensional space. For
# each balloon, provided input is the start and end coordinates of the
# horizontal diameter. Since it's horizontal, y-coordinates don't matter and
# hence the x-coordinates of start and end of the diameter suffice. Start is
# always smaller than end. There will be at most 10^4 balloons.
# 
# An arrow can be shot up exactly vertically from different points along the
# x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart
# ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An
# arrow once shot keeps travelling up infinitely. The problem is to find the
# minimum number of arrows that must be shot to burst all balloons.
# 
# Example:
# 
# 
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
# 
# Output:
# 2
# 
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons
# [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two
# balloons).
# 
# 
# 
# 
#

# @lc code=start
from operator import itemgetter
class Solution:
    def findMinArrowShots(self, points: [[int]]) -> int:
        if not points or not points[0]:
            return 0
        pointsSort = sorted(points, key=itemgetter(1))
        arrowPos = pointsSort[0][1]
        count = 1
        for i in range(1, len(pointsSort)):
            if pointsSort[i][0] > arrowPos:
                count += 1
                arrowPos = pointsSort[i][1]
        return count
# @lc code=end
# [[1,2],[3,4],[5,6],[7,8]] [[10,16],[2,8],[1,6],[7,12]]
# [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
# [[1,2],[2,3],[3,4],[4,5]]
# [[2,3],[7,15],[5,12],[4,5],[8,13],[9,16],[5,8],[8,16],[3,4],[8,17]]
if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[2,3],[7,15],[5,12],[4,5],[8,13],[9,16],[5,8],[8,16],[3,4],[8,17]]))