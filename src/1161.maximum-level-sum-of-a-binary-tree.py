#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
#
# algorithms
# Medium (70.80%)
# Likes:    248
# Dislikes: 15
# Total Accepted:    28.7K
# Total Submissions: 40.2K
# Testcase Example:  '[1,7,0,7,-8,null,null]'
#
# Given the root of a binary tree, the level of its root is 1, the level of its
# children is 2, and so on.
# 
# Return the smallest level X such that the sum of all the values of nodes at
# level X is maximal.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given tree is between 1 and 10^4.
# -10^5 <= node.val <= 10^5
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
from collections import defaultdict
from queue import Queue
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        maxSum, res, q, level = float('-inf'), 0, Queue(), 0
        q.put([root])
        while not q.empty():
            level += 1
            curr = q.get()
            next_ = []
            tmp = 0
            for c in curr:
                if c:
                    tmp += c.val
                    if c.left:
                        next_.append(c.left)
                    if c.right:
                        next_.append(c.right)
            if tmp > maxSum:
                maxSum = tmp
                res = level
            if next_:
                q.put(next_)
        return res
# @lc code=end

