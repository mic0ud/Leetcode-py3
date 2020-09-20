#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
#
# algorithms
# Medium (78.11%)
# Likes:    493
# Dislikes: 71
# Total Accepted:    32.1K
# Total Submissions: 40.7K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# Given the root of a binary search tree with distinct values, modify it so
# that every node has a new value equal to the sum of the values of the
# original tree that are greater than or equal to node.val.
# 
# As a reminder, a binary search tree is a tree that satisfies these
# constraints:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
#               4(30) 
#           1(36)         6(21)
#      0(36)   2(35)   5(26)    7(15)
#                3(33)              8(8)

# Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

# Note:
# 
# 
# The number of nodes in the tree is between 1 and 100.
# Each node will have value between 0 and 100.
# The given tree is a binary search tree.


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        sumMap = defaultdict(int)

        def calcSum(node):
            if not node:
                return
            tmpMin = float('inf')
            for k in sumMap.keys():
                if k < node.val:
                    sumMap[k] += node.val
                else:
                    tmpMin = min(tmpMin, k)
            if tmpMin < float('inf'):
                sumMap[node.val] = sumMap[tmpMin] + node.val
            else:
                sumMap[node.val] = node.val
            calcSum(node.left)
            calcSum(node.right)
        
        def putVal(node):
            if not node:
                return
            node.val = sumMap[node.val]
            putVal(node.left)
            putVal(node.right)
        
        calcSum(root)
        putVal(root)
        return root
# @lc code=end

