#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (48.92%)
# Likes:    912
# Dislikes: 172
# Total Accepted:    261.8K
# Total Submissions: 534K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
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
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
        return res[::-1]
# @lc code=end

