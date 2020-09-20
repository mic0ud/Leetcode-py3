#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (44.05%)
# Likes:    1352
# Dislikes: 74
# Total Accepted:    276.5K
# Total Submissions: 626.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = queue.Queue()
        q.put([root])
        zigzag = True
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
                if zigzag:
                    res.append(level)
                else:
                    res.append(level[::-1])
                zigzag = not zigzag
            if len(nextLevelList) > 0:
                q.put(nextLevelList)
        return res
# @lc code=end

