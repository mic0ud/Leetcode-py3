#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#
# https://leetcode.com/problems/rectangle-overlap/description/
#
# algorithms
# Easy (47.73%)
# Likes:    455
# Dislikes: 88
# Total Accepted:    35.6K
# Total Submissions: 74.4K
# Testcase Example:  '[0,0,2,2]\n[1,1,3,3]'
#
# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the
# coordinates of its bottom-left corner, and (x2, y2) are the coordinates of
# its top-right corner.
# 
# Two rectangles overlap if the area of their intersection is positive.  To be
# clear, two rectangles that only touch at the corner or edges do not overlap.
# 
# Given two (axis-aligned) rectangles, return whether they overlap.
# 
# Example 1:
# 
# 
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# 
# 
# Notes:
# 
# 
# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.
# 
# 
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]
# @lc code=end
# [1,2,3,4]
# [7,8,13,15]
# [10,8,12,20]