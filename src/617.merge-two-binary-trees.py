#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#
# https://leetcode.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (71.73%)
# Likes:    2340
# Dislikes: 148
# Total Accepted:    240.3K
# Total Submissions: 332.5K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# Given two binary trees and imagine that when you put one of them to cover the
# other, some nodes of the two trees are overlapped while the others are not.
# 
# You need to merge them into a new binary tree. The merge rule is that if two
# nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.
# 
# Example 1:
# 
# 
# Input: 
# Tree 1                     Tree 2                  
# ⁠         1                         2                             
# ⁠        / \                       / \                            
# ⁠       3   2                     1   3                        
# ⁠      /                           \   \                      
# ⁠     5                             4   7                  
# Output: 
# Merged tree:
# 3
# / \
# 4   5
# / \   \ 
# 5   4   7
# 
# 
# 
# 
# Note: The merging process must start from the root nodes of both trees.
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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        return self.merge(t1, t2)

    def merge(self, node1, node2):
        if not node1 and not node2:
            return None
        val = (0 if node1 is None else node1.val) + (0 if node2 is None else node2.val)
        node = TreeNode(val)
        node.left = self.merge(None if node1 is None else node1.left, None if node2 is None else node2.left)
        node.right = self.merge(None if node1 is None else node1.right, None if node2 is None else node2.right)
        return node
# @lc code=end
# [1,2,null,3]\n[1,null,2,null,3]
# [1,null,2,null,3]
# [2,2,5,null,null,null,3]
# [2,2,2,3,null,null,3]
