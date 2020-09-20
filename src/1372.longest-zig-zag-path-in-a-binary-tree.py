#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
#
# algorithms
# Medium (52.74%)
# Likes:    206
# Dislikes: 5
# Total Accepted:    8.2K
# Total Submissions: 15.5K
# Testcase Example:  '[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]'
#
# Given a binary tree root, a ZigZag path for a binary tree is defined as
# follow:
# 
# 
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right then move to the right child of the current
# node otherwise move to the left child.
# Change the direction from right to left or right to left.
# Repeat the second and third step until you can't move in the tree.
# 
# 
# Zigzag length is defined as the number of nodes visited - 1. (A single node
# has a length of 0).
# 
# Return the longest ZigZag path contained in that tree.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left ->
# right).
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# Each tree has at most 50000 nodes..
# Each node's value is between [1, 100].
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        res, memo = [0], defaultdict(list) # {node: [left, right]}
        def search(node) -> [int, int]: # d: 0-left, 1-right
            if not node:
                return [0,0]
            if node in memo:
                return memo[node]
            left = search(node.left)
            right = search(node.right)
            memo[node] = [left[1]+1, right[0]+1]
            res[0] = max(res[0], max(memo[node]))
            return memo[node]
        search(root)
        return res[0]-1
# @lc code=end

