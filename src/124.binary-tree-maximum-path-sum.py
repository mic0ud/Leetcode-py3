#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (31.56%)
# Likes:    2269
# Dislikes: 182
# Total Accepted:    247.8K
# Total Submissions: 782.8K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
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
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, res: [int]) -> int:
            if not node:
                return 0
            left = dfs(node.left, res)
            right = dfs(node.right, res)
            tmp = node.val + (left if left > 0 else 0) + (right if right > 0 else 0)
            res[0] = max(res[0], tmp)
            return max(max(left, right, 0) + node.val, 0)

        res = [float('-inf')]
        dfs(root, res)
        return res[0]
# @lc code=end

