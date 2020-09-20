#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#
# https://leetcode.com/problems/valid-square/description/
#
# algorithms
# Medium (41.20%)
# Likes:    187
# Dislikes: 346
# Total Accepted:    27.2K
# Total Submissions: 64.9K
# Testcase Example:  '[0,0]\n[1,1]\n[1,0]\n[0,1]'
#
# Given the coordinates of four points in 2D space, return whether the four
# points could construct a square.
# 
# The coordinate (x,y) of a point is represented by an integer array with two
# integers.
# 
# Example:
# 
# 
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True

# Note:
# 
# 
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal
# angles (90-degree angles).
# Input points have no order.


# @lc code=start
from collections import defaultdict
class Solution:
    def validSquare(self, p1: [int], p2: [int], p3: [int], p4: [int]) -> bool:
        c = defaultdict(int)
        pts = [p1,p2,p3,p4]
        for i in range(3):
            for j in range(i+1,4):
                l = self.sideLength(pts[i], pts[j])
                c[l] += 1
        return len(c) == 2 and 4 in c.values() and 2 in c.values()

    def validSquare_UGLY(self, p1: [int], p2: [int], p3: [int], p4: [int]) -> bool:
        l12, l13, l14 = self.sideLength(p1,p2), self.sideLength(p1,p3), self.sideLength(p1,p4)
        if len(set([l12, l13, l14])) != 2:
            return False
        threshold = 10**(-6)
        if max([l12, l13, l14]) == l12:
            if abs(l12**2 - (l13**2 + l14**2)) > threshold:
                return False
            l34 = self.sideLength(p3,p4)
            if abs(l34**2 - (l13**2 + l14**2)) > threshold:
                return False
            l24 = self.sideLength(p2, p4)
            if abs(l12**2 - (l14**2 + l24**2)) > threshold:
                return False
        if max([l12, l13, l14]) == l13:
            if abs(l13**2 - (l12**2 + l14**2)) > threshold:
                return False
            l24 = self.sideLength(p2,p4)
            if abs(l24**2 - (l12**2 + l14**2)) > threshold:
                return False
            l34 = self.sideLength(p3, p4)
            if abs(l13**2 - (l14**2 + l34**2)) > threshold:
                return False
        if max([l12, l13, l14]) == l14:
            if abs(l14**2 - (l12**2 + l13**2)) > threshold:
                return False
            l23 = self.sideLength(p2,p3)
            if abs(l23**2 - (l12**2 + l13**2)) > threshold:
                return False
            l34 = self.sideLength(p3, p4)
            if abs(l14**2 - (l13**2 + l34**2)) > threshold:
                return False
        return True

    def sideLength(self, p1, p2) -> float:
        return (abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1])**2)**0.5
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.validSquare([0,0], [1,1], [1,0], [0,1])
