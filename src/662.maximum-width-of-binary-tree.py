#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (39.55%)
# Likes:    860
# Dislikes: 187
# Total Accepted:    45.6K
# Total Submissions: 115.4K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given a binary tree, write a function to get the maximum width of the given
# tree. The width of a tree is the maximum width among all levels. The binary
# tree has the same structure as a full binary tree, but some nodes are null.
# 
# The width of one level is defined as the length between the end-nodes (the
# leftmost and right most non-null nodes in the level, where the null nodes
# between the end-nodes are also counted into the length calculation.
# 
# Example 1:
# 
# 
# Input: 
# 
# ⁠          1
# ⁠        /   \
# ⁠       3     2
# ⁠      / \     \  
# ⁠     5   3     9 
# 
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4
# (5,3,null,9).
# 
# 
# Example 2:
# 
# 
# Input: 
# 
# ⁠         1
# ⁠        /  
# ⁠       3    
# ⁠      / \       
# ⁠     5   3     
# 
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2
# (5,3).
# 
# 
# Example 3:
# 
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2 
# ⁠      /        
# ⁠     5      
# 
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2
# (3,2).
# 
# 
# Example 4:
# 
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      /     \  
# ⁠     5       9 
# ⁠    /         \
# ⁠   6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8
# (6,null,null,null,null,null,null,7).
# 
# 
# 
# 
# Note: Answer will in the range of 32-bit signed integer.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = Queue()
        q.put([root])
        res = 1
        while True:
            nodes = q.get()
            next_ = []
            i, start, end = 0, 0, 0
            while i < len(nodes) and not nodes[i]:
                i += 1
            if i == len(nodes):
                break
            start, i = i, len(nodes)-1
            while i > start and not nodes[i]:
                i -= 1
            end = i
            res = max(res, end-start+1)
            for k in range(start, end+1):
                next_.append(nodes[k].left if nodes[k] else None)
                next_.append(nodes[k].right if nodes[k] else None)
            q.put(next_)
        return res
# @lc code=end

