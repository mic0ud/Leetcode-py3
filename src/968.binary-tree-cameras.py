#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#
# https://leetcode.com/problems/binary-tree-cameras/description/
#
# algorithms
# Hard (36.39%)
# Likes:    479
# Dislikes: 12
# Total Accepted:    13.5K
# Total Submissions: 36.9K
# Testcase Example:  '[0,0,null,0,0]'
#
# Given a binary tree, we install cameras on the nodes of the tree. 
# 
# Each camera at a node can monitor its parent, itself, and its immediate
# children.
# 
# Calculate the minimum number of cameras needed to monitor all nodes of the
# tree.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
# 
# 
# 
# Example 2:
# 
# 
# Input: [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the
# tree. The above image shows one of the valid configurations of camera
# placement.
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given tree will be in the range [1, 1000].
# Every node has value 0.


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if not root:
            return 0
        # greedy, always put camera on the parents of leaves
        # Return 0 if it's a leaf or it needs a camera
        # Return 1 if it's a parent of a leaf, or with a camera on this node.
        # Return 2 if it's coverd, without a camera on this node.
        def putCamera(node, res: [int]) -> int:
            if not node.left and not node.right:
                return 0
            left, right = -1, -1
            if node.left:
                left = putCamera(node.left, res)
            if node.right:
                right = putCamera(node.right, res)
            if left == 0 or right == 0:
                res[0] += 1
                return 1
            return 2 if left == 1 or right == 1 else 0

        res = [0]
        r = putCamera(root, res)
        return res[0] if r > 0 else res[0] + 1
# @lc code=end
# [0,0,null,null,0,0,null,null,0,0] 2
# [0,null,0,null,0,null,0]
