#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (51.10%)
# Likes:    1221
# Dislikes: 66
# Total Accepted:    309.5K
# Total Submissions: 603.2K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [3,2,1]
# 
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        self.postorder(root, res)
        return res

    def postorder(self, node, res):
        if not node:
            return
        self.postorder(node.left, res)  
        self.postorder(node.right, res)
        res.append(node.val)  

# @lc code=end

