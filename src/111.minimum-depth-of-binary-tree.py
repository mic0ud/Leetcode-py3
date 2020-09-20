#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (36.17%)
# Likes:    917
# Dislikes: 523
# Total Accepted:    343.9K
# Total Submissions: 950K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:
            return self.depth(root.right) + 1
        if not root.right:
            return self.depth(root.left) + 1
        return min(self.depth(root.left), self.depth(root.right)) + 1

    def depth(self, node) -> int:
        if not node:
            return 0
        if not node.left:
            return self.depth(node.right) + 1
        if not node.right:
            return self.depth(node.left) + 1
        return min(self.depth(node.left), self.depth(node.right)) + 1     
# @lc code=end

