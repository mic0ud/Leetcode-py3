#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (74.09%)
# Likes:    445
# Dislikes: 19
# Total Accepted:    30.2K
# Total Submissions: 40.7K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# Return the root node of a binary search tree that matches the given preorder
# traversal.
# 
# (Recall that a binary search tree is a binary tree where for every node, any
# descendant of node.left has a value < node.val, and any descendant of
# node.right has a value > node.val.  Also recall that a preorder traversal
# displays the value of the node first, then traverses node.left, then
# traverses node.right.)
# 
# 
# 
# Example 1:
#            8 
#         5    10
#      1    7    12
# 
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Note: 
# 
# 
# 1 <= preorder.length <= 100
# The values of preorder are distinct.
# 
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
    def bstFromPreorder(self, preorder: [int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        
        def build(root, val) -> TreeNode:
            if not root:
                return TreeNode(val)
            if val < root.val:
                root.left = build(root.left, val)
            else:
                root.right = build(root.right, val)
            return root

        for val in preorder[1:]:
            build(root, val)
        return root    
# @lc code=end

