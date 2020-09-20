#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#
# https://leetcode.com/problems/balance-a-binary-search-tree/description/
#
# algorithms
# Medium (74.52%)
# Likes:    189
# Dislikes: 17
# Total Accepted:    12K
# Total Submissions: 16.2K
# Testcase Example:  '[1,null,2,null,3,null,4,null,null]'
#
# Given a binary search tree, return a balanced binary search tree with the
# same node values.
# 
# A binary search tree is balanced if and only if the depth of the two subtrees
# of every node never differ by more than 1.
# 
# If there is more than one answer, return any of them.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is
# also correct.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is between 1 and 10^4.
# The tree nodes will have distinct values between 1 and 10^5.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        inorder(root)
        def construct(left, right):
            if left > right:
                return None
            mid = (left+right)//2
            node = TreeNode(nodes[mid])
            node.left = construct(left, mid-1)
            node.right = construct(mid+1, right)
            return node
        root = construct(0, len(nodes)-1)
        return root
# @lc code=end

