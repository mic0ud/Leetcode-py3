#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (77.74%)
# Likes:    618
# Dislikes: 63
# Total Accepted:    83.6K
# Total Submissions: 106.2K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# Given the root node of a binary search tree (BST) and a value to be inserted
# into the tree, insert the value into the BST. Return the root node of the BST
# after the insertion. It is guaranteed that the new value does not exist in
# the original BST.
# 
# Note that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
# 
# For example, 
# 
# 
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# And the value to insert: 5
# 
# 
# You can return this binary search tree:
# 
# 
# ⁠        4
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   /
# ⁠   1   3 5
# 
# 
# This tree is also valid:
# 
# 
# ⁠        5
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   
# ⁠   1   3
# ⁠        \
# ⁠         4
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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
# @lc code=end

