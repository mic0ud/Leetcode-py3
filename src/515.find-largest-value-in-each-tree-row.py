#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (58.82%)
# Likes:    661
# Dislikes: 56
# Total Accepted:    82.6K
# Total Submissions: 138.7K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# You need to find the largest value in each row of a binary tree.
# 
# Example:
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# Output: [1, 3, 9]
# 
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
    def largestValues(self, root: TreeNode) -> [int]:
        if not root:
            return []
        q, res = Queue(), []
        q.put([root])
        while not q.empty():
            curr = q.get()
            next_ = []
            currMax = -float('inf')
            for node in curr:
                if node:
                    currMax = max(currMax, node.val)
                    if node.left:
                        next_.append(node.left)
                    if node.right:
                        next_.append(node.right)
            res.append(currMax)
            if next_:
                q.put(next_)
        return res
# @lc code=end

