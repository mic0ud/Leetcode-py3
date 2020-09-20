#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
#
# algorithms
# Medium (61.76%)
# Likes:    297
# Dislikes: 15
# Total Accepted:    20K
# Total Submissions: 32K
# Testcase Example:  '[8,3,10,1,6,null,14,null,null,4,7,13]'
#
# Given the root of a binary tree, find the maximum value V for which there
# exists different nodes A and B where V = |A.val - B.val| and A is an ancestor
# of B.
# 
# (A node A is an ancestor of B if either: any child of A is equal to B, or any
# child of A is an ancestor of B.)
 
# Example 1:

# Input: [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: 
# We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1|
# = 7.

# Note:
# 
# 
# The number of nodes in the tree is between 2 and 5000.
# Each node will have value between 0 and 100000.


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def calc(node, largest, smallest, res: [int]):
            if not node:
                return
            tmp = abs(node.val - largest)
            tmp = max(tmp, abs(node.val-smallest))
            res[0] = max(res[0], tmp)
            l = max(largest, node.val)
            s = min(smallest, node.val)
            calc(node.left, l, s, res)
            calc(node.right, l, s, res)
            
        res = [0]
        calc(root.left, root.val, root.val, res)
        calc(root.right, root.val, root.val, res)
        return res[0]
# @lc code=end

