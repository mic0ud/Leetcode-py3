#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (61.26%)
# Likes:    441
# Dislikes: 40
# Total Accepted:    60.5K
# Total Submissions: 96.7K
# Testcase Example:  '[1,null,3,2,4,null,5,6]\r'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
# 
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).
# 
# 
# Example 1:

# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
# 
# 
# Example 2:

# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
# 
# 
# 
# Constraints:
# 
# 
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]


# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from queue import Queue
class Solution:
    def levelOrder(self, root: 'Node') -> [[int]]:
        if not root:
            return []
        res, q = [], Queue()
        q.put([root])
        while not q.empty():
            tmp = q.get()
            curr, next_ = [], []
            for n in tmp:
                curr.append(n.val)
                next_ += n.children if n.children else []
            res.append(curr)
            if next_:
                q.put(next_)
        return res        
# @lc code=end

