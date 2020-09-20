#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (52.77%)
# Likes:    1606
# Dislikes: 102
# Total Accepted:    102.6K
# Total Submissions: 192.5K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
# 
# 
# Example:
# 
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
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
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        def inorder(node, val) -> int:
            if not node:
                return 0
            rightSum = inorder(node.right, val)
            node.val += rightSum + val
            left = inorder(node.left, node.val)
            return node.val + left - val
        inorder(root, 0)
        return root
# @lc code=end
# [2,0,3,-4,1], [5,11,3,7,6], [5,6,3,2,6]
