#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 is None and node2 is None: return True
        if node1 is None or node2 is None: return False
        return node1.val == node2.val and self._isSymmetric(node1.left, node2.right) and self._isSymmetric(node1.right, node2.left)
# @lc code=end

