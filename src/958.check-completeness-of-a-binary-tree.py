#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
#
# algorithms
# Medium (50.37%)
# Likes:    516
# Dislikes: 10
# Total Accepted:    35.5K
# Total Submissions: 69.6K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a binary tree, determine if it is a complete binary tree.
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level
# h.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values
# {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left
# as possible.
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
# 
# 
# 
# 
# 
# Note:
# 
# 
# The tree will have between 1 and 100 nodes.
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
from queue import Queue
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return False        
        q = Queue()
        q.put([root])
        while not q.empty():
            nodes = q.get()
            next_ = []
            nullFound = False
            onlyNull = True
            for i in range(len(nodes)):
                if nodes[i]:
                    if nullFound:
                        return False
                    next_.append(nodes[i].left)
                    next_.append(nodes[i].right)
                    if nodes[i].left or nodes[i].right:
                        onlyNull = False
                else:
                    nullFound = True
            if next_:
                if nullFound and not onlyNull:
                    return False
                q.put(next_)
        return True
# @lc code=end
# [1,2,3,5,null,7,8], [1,2,3,5,null,7], [1,2,3,4,5,6]
# [1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15]
