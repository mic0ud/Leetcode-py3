#
# @lc app=leetcode id=971 lang=python3
#
# [971] Flip Binary Tree To Match Preorder Traversal
#
# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/description/
#
# algorithms
# Medium (43.83%)
# Likes:    165
# Dislikes: 75
# Total Accepted:    8.8K
# Total Submissions: 19.9K
# Testcase Example:  '[1,2]\n[2,1]'
#
# Given a binary tree with N nodes, each node has a different value from {1,
# ..., N}.
# 
# A node in this binary tree can be flipped by swapping the left child and the
# right child of that node.
# 
# Consider the sequence of N values reported by a preorder traversal starting
# from the root.  Call such a sequence of N values the voyage of the tree.
# 
# (Recall that a preorder traversal of a node means we report the current
# node's value, then preorder-traverse the left child, then preorder-traverse
# the right child.)
# 
# Our goal is to flip the least number of nodes in the tree so that the voyage
# of the tree matches the voyage we are given.
# 
# If we can do so, then return a list of the values of all nodes flipped.  You
# may return the answer in any order.
# 
# If we cannot do so, then return the list [-1].
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2], voyage = [2,1]
# Output: [-1]
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [1,2,3], voyage = [1,3,2]
# Output: [1]
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root = [1,2,3], voyage = [1,2,3]
# Output: []
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 100
# 
# 
# 
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
    def __init__(self):
        self.v = 0

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []
        isMatched = self.preorderCheck(root, voyage, res)
        return res if isMatched else [-1]
        
    def preorderCheck(self, root, voyage, res) -> bool:
        if not root:
            return True
        if root.val != voyage[self.v]:
            return False        
        self.v += 1
        if root.left and root.left.val != voyage[self.v]:
            res.append(root.val)
            root.left, root.right = root.right, root.left
        return self.preorderCheck(root.left, voyage, res) and self.preorderCheck(root.right, voyage, res)
# @lc code=end

