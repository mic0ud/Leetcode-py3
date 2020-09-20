#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (59.45%)
# Likes:    2165
# Dislikes: 95
# Total Accepted:    572.9K
# Total Submissions: 961.7K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
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

    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:       
        if root:
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
        return self.res
# @lc code=end

