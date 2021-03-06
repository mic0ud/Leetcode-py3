#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (43.45%)
# Likes:    1448
# Dislikes: 79
# Total Accepted:    208.6K
# Total Submissions: 473.5K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        p = head
        vals = []
        while p:
            vals.append(p.val)
            p = p.next
        return self.arrayToBST(vals, 0, len(vals))
        
    def arrayToBST(self, vals: [int], left, right) -> TreeNode:
        if left >= right:
            return None
        mid = (left+right) // 2
        root = TreeNode(vals[mid])
        root.left = self.arrayToBST(vals, left, mid)
        root.right = self.arrayToBST(vals, mid+1, right)
        return root
# @lc code=end

