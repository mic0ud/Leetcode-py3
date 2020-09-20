#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (41.86%)
# Likes:    1118
# Dislikes: 25
# Total Accepted:    179.3K
# Total Submissions: 427K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# postorder = [9,15,7,20,3]
# inorder =   [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder[-1])
        rootIndex = inorder.index(postorder[-1])
        left = len(inorder[:rootIndex])
        root.left = self.buildTree(inorder[:rootIndex], postorder[:left])        
        root.right = self.buildTree(inorder[rootIndex+1:], postorder[left:-1])
        return root
# @lc code=end

