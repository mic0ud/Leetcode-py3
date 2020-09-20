#
# @lc app=leetcode id=546 lang=python3
#
# [546] Remove Boxes
#
# https://leetcode.com/problems/remove-boxes/description/
#
# algorithms
# Hard (39.84%)
# Likes:    458
# Dislikes: 41
# Total Accepted:    11.5K
# Total Submissions: 28.9K
# Testcase Example:  '[1,3,2,2,2,3,4,3,1]'
#
# Given several boxes with different colors represented by different positive
# numbers. 
# You may experience several rounds to remove boxes until there is no box left.
# Each time you can choose some continuous boxes with the same color (composed
# of k boxes, k >= 1), remove them and get k*k points.
# Find the maximum points you can get.
# 
# 
# Example 1:
# Input: 
# 
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# 
# Output:
# 
# 23
# 
# Explanation: 
# 
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
# ----> [1, 3, 3, 3, 1] (1*1=1 points) 
# ----> [1, 1] (3*3=9 points) 
# ----> [] (2*2=4 points)
# 
# 
# 
# Note:
# The number of boxes n would not exceed 100.
# 
# 
#

# @lc code=start
class Solution:
    def removeBoxes(self, boxes: [int]) -> int:
        if not boxes:
            return 0
        
# @lc code=end

