#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (59.72%)
# Likes:    680
# Dislikes: 115
# Total Accepted:    86.4K
# Total Submissions: 144.4K
# Testcase Example:  '[2,1,3]'
#
# 
# Given a binary tree, find the leftmost value in the last row of the tree. 
# 
# 
# Example 1:
# 
# Input:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Output:
# 1
# 
# 
# 
# ⁠ Example 2: 
# 
# Input:
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
# 
# Output:
# 7
# 
# 
# 
# Note:
# You may assume the tree (i.e., the given root node) is not NULL.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = Queue()
        q.put([root])
        while not q.empty():
            curr = q.get()
            next_ = []
            for node in curr:
                if node:
                    if node.left:
                        next_.append(node.left)
                    if node.right:
                        next_.append(node.right)
            if next_:
                q.put(next_)
            else:
                return curr[0].val
        return 0
# @lc code=end

