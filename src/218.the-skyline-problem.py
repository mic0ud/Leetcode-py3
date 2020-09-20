#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
# https://leetcode.com/problems/the-skyline-problem/description/
#
# algorithms
# Hard (32.84%)
# Likes:    1558
# Dislikes: 79
# Total Accepted:    111.2K
# Total Submissions: 337.3K
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
# A city's skyline is the outer contour of the silhouette formed by all the
# buildings in that city when viewed from a distance. Now suppose you are given
# the locations and height of all the buildings as shown on a cityscape photo
# (Figure A), write a program to output the skyline formed by these buildings
# collectively (Figure B).
# ⁠   
# 
# The geometric information of each building is represented by a triplet of
# integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and
# right edge of the ith building, respectively, and Hi is its height. It is
# guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You
# may assume all buildings are perfect rectangles grounded on an absolutely
# flat surface at height 0.
# 
# For instance, the dimensions of all buildings in Figure A are recorded as: [
# [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
# 
# The output is a list of "key points" (red dots in Figure B) in the format of
# [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key
# point is the left endpoint of a horizontal line segment. Note that the last
# key point, where the rightmost building ends, is merely used to mark the
# termination of the skyline, and always has zero height. Also, the ground in
# between any two adjacent buildings should be considered part of the skyline
# contour.
# 
# For instance, the skyline in Figure B should be represented as:[ [2 10], [3
# 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
# 
# Notes:
# 
# 
# The number of buildings in any input list is guaranteed to be in the range
# [0, 10000].
# The input list is already sorted in ascending order by the left x position
# Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height in the output
# skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not
# acceptable; the three lines of height 5 should be merged into one in the
# final output as such: [...[2 3], [4 5], [12 7], ...]
# 
# 
#

# @lc code=start
import heapq
from functools import cmp_to_key
class Solution:
    def cmp(self, p1:(), p2:()) -> int:
        if p1[0] == p2[0]:
            if p1[2] == 0 and p2[2] == 0:
                return -(p1[1] - p2[1])
            elif p1[2] == 1 and p2[2] == 1:
                return p1[1] - p2[1]
            else:
                return -1 if p1[2] == 0 else 1
        else:
            return p1[0] - p2[0]

    def getSkyline(self, buildings: [[int]]) -> [[int]]:
        res = []
        heap = []
        heapq.heappush(heap, 0)
        high = 0
        points = [] # x,y,1 or x,y,0  0 - start, 1 - end
        for b in buildings:
            points.append((b[0],b[2],0))
            points.append((b[1],b[2],1))
        points.sort(key=cmp_to_key(self.cmp))
        for p in points:
            if p[2] == 0:
                heapq.heappush(heap, p[1])
                tmpHigh = heapq.nlargest(1, heap)[0]
                if tmpHigh > high:
                    res.append([p[0],tmpHigh])
                    high = tmpHigh
            elif p[2] == 1:
                heap.remove(p[1])
                heapq.heapify(heap)
                tmpHigh = heapq.nlargest(1, heap)[0]
                if tmpHigh < high:
                    res.append([p[0],tmpHigh])
                    high = tmpHigh
        return res
# @lc code=end
# [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# [[2,9,10],[9,12,15]] -- [[2,10],[9,15],[12,0]]
# [[0,2,3],[2,5,3]] -- [[0,3],[5,0]]
# [[2,4,7],[2,4,5],[2,4,6]] -- [[2,7],[4,0]]

def getSkylineTLE(self, buildings: [[int]]) -> [[int]]:
    if not buildings or not buildings[0]:
        return []
    height = [0 for _ in range(buildings[-1][1]+1)]
    height.append(0)
    for b in buildings:
        for i in range(b[0],b[1]+1):
            height[i] = max(height[i], b[2])
    res = []
    cur = height[0]
    if cur > 0:
        res.append([0, cur])
    for i in range(1, len(height)):
        if height[i] > cur:
            res.append([i, height[i]])
            cur = height[i]
        elif height[i] < cur:
            res.append([i-1, height[i]])
            cur = height[i]
    return res

if __name__ == '__main__':
    s = Solution()
    s.getSkyline([[2,4,7],[2,4,5],[2,4,6]])
    s.getSkyline([[0,2,3],[2,5,3]])
    s.getSkyline([[2,9,10],[9,12,15]])