#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (50.94%)
# Likes:    1980
# Dislikes: 55
# Total Accepted:    469.2K
# Total Submissions: 919.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = queue.Queue()
        q.put([root])
        while not q.empty():
            nodeList = q.get()
            nextLevelList = []
            level = []
            for n in nodeList:
                if n is not None:                    
                    level.append(n.val)
                    nextLevelList.append(n.left)
                    nextLevelList.append(n.right)
            if len(level) > 0:
                res.append(level)
            if len(nextLevelList) > 0:
                q.put(nextLevelList)
        return res
# @lc code=end

