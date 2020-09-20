#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (47.99%)
# Likes:    1147
# Dislikes: 80
# Total Accepted:    262.2K
# Total Submissions: 545.1K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        current = ''
        self.search(root, res, current)
        return res
        
    def search(self, node, res, current):
        if not node:
            return
        if current == '':
            current = str(node.val)
        else:
            current += '->' + str(node.val)
        if not node.left and not node.right:
            res.append(current)
            return
        self.search(node.left, res, current)
        self.search(node.right, res, current)
# @lc code=end

