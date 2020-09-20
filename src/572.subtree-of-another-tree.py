#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (42.91%)
# Likes:    1778
# Dislikes: 80
# Total Accepted:    170K
# Total Submissions: 389.2K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
# 
# 
# Example 1:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# Given tree t:
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# Return true, because t has the same structure and node values with a subtree
# of s.
# 
# 
# Example 2:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# Given tree t:
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# Return false.
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
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def check(n1, n2) -> bool:
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val == n2.val and check(n1.left, n2.left) and check(n1.right, n2.right)

        def traverse(node, res: [bool]):
            if not node or res[0]:
                return
            if check(node, t):
                res[0] = True
                return
            traverse(node.left, res)
            traverse(node.right, res)

        res = [False]
        traverse(s, res)
        return res[0]
# @lc code=end

