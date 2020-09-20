#
# @lc app=leetcode id=1104 lang=python3
#
# [1104] Path In Zigzag Labelled Binary Tree
#
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/description/
#
# algorithms
# Medium (70.47%)
# Likes:    160
# Dislikes: 106
# Total Accepted:    10.8K
# Total Submissions: 15.3K
# Testcase Example:  '14'
#
# In an infinite binary tree where every node has two children, the nodes are
# labelled in row order.
# 
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is
# left to right, while in the even numbered rows (second, fourth, sixth,...),
# the labelling is right to left.
# 
# 
# 
# Given the label of a node in this tree, return the labels in the path from
# the root of the tree to the node with that label.
# 
# 
# Example 1:
# 
# 
# Input: label = 14
# Output: [1,3,4,14]
# 
# 
# Example 2:
# 
# 
# Input: label = 26
# Output: [1,2,6,10,26]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= label <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        power = 0
        while label >= 2 ** power:
            power += 1
        res = [label]   
        parent = label    
        for p in range(power-1, 0, -1):
            # zigzag = p % 2 == 0
            n = 2 ** p
            parent = (n + 2*n-parent - 1) // 2
            res = [parent] + res
        return res
# @lc code=end

