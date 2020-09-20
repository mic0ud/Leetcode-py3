#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (50.41%)
# Likes:    1439
# Dislikes: 76
# Total Accepted:    212.2K
# Total Submissions: 419.7K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        q = queue.Queue()
        q.put([root])
        while not q.empty():
            level = q.get()
            rightMost = level[-1]
            res.append(rightMost.val)
            nextLevel = []
            for node in level:
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)
            if len(nextLevel) > 0:
                q.put(nextLevel)
        return res
# @lc code=end

