#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#
# https://leetcode.com/problems/deepest-leaves-sum/description/
#
# algorithms
# Medium (83.51%)
# Likes:    439
# Dislikes: 30
# Total Accepted:    37.8K
# Total Submissions: 45.3K
# Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
#
# Given a binary tree, return the sum of values of its deepest leaves.
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = Queue()
        q.put([root])
        while not q.empty():
            curr = q.get()
            next_ = []
            tmp = 0
            for c in curr:
                tmp += c.val
                if c.left:
                    next_.append(c.left)
                if c.right:
                    next_.append(c.right)
            if not next_:
                return tmp
            else:
                q.put(next_)
        return 0
# @lc code=end

