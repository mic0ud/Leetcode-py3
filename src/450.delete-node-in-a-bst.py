#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
# https://leetcode.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (41.04%)
# Likes:    1396
# Dislikes: 74
# Total Accepted:    93.6K
# Total Submissions: 223.9K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# Given a root node reference of a BST and a key, delete the node with the
# given key in the BST. Return the root node reference (possibly updated) of
# the BST.
# 
# Basically, the deletion can be divided into two stages:
# 
# Search for a node to remove.
# If the node is found, delete the node.
# 
# 
# 
# Note: Time complexity should be O(height of tree).
# 
# Example:
# 
# root = [5,3,6,2,4,null,7]
# key = 3
# 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Given key to delete is 3. So we find the node with value 3 and delete it.
# 
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
# 
# ⁠   5
# ⁠  / \
# ⁠ 4   6
# ⁠/     \
# 2       7
# 
# Another valid answer is [5,2,6,null,4,null,7].
# 
# ⁠   5
# ⁠  / \
# ⁠ 2   6
# ⁠  \   \
# ⁠   4   7
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
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                tmp = self.minVal(root.right)
                root.val = tmp.val
                root.right = self.deleteNode(root.right, tmp.val)
        return root

    def minVal(self, node) -> TreeNode:
        curr = node
        while curr.left:
            curr = curr.left
        return curr
# @lc code=end

