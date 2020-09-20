#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#
# https://leetcode.com/problems/trim-a-binary-search-tree/description/
#
# algorithms
# Easy (61.26%)
# Likes:    1442
# Dislikes: 148
# Total Accepted:    85.6K
# Total Submissions: 138.7K
# Testcase Example:  '[1,0,2]\n1\n2'
#
# 
# Given a binary search tree and the lowest and highest boundaries as L and R,
# trim the tree so that all its elements lies in [L, R] (R >= L). You might
# need to change the root of the tree, so the result should return the new root
# of the trimmed binary search tree.
# 
# 
# Example 1:
# 
# Input: 
# ⁠   1
# ⁠  / \
# ⁠ 0   2
# 
# ⁠ L = 1
# ⁠ R = 2
# 
# Output: 
# ⁠   1
# ⁠     \
# ⁠      2
# 
# 
# 
# Example 2:
# 
# Input: 
# ⁠   3
# ⁠  / \
# ⁠ 0   4
# ⁠  \
# ⁠   2
# ⁠  /
# ⁠ 1
# 
# ⁠ L = 1
# ⁠ R = 3
# 
# Output: 
# ⁠     3
# ⁠    / 
# ⁠  2   
# ⁠ /
# ⁠1
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
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        def trim(root, l, r) -> TreeNode:
            if not root:
                return None
            if root.val < l:
                return trim(root.right, l, r)
            if root.val > r:
                return trim(root.left, l, r)
            if not root.left or root.left.val < l:
                root.left = None if not root.left else root.left.right
            if not root.right or root.right.val > r:
                root.right = None if not root.right else root.right.left
            root.left = trim(root.left, l, r)
            root.right = trim(root.right, l, r)
            return root

        return trim(root, L, R)
# @lc code=end
# [3,1,4,null,2]\n3\n4
