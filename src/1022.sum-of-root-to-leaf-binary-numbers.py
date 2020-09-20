#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (62.33%)
# Likes:    251
# Dislikes: 62
# Total Accepted:    24.6K
# Total Submissions: 39.1K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path
# represents a binary number starting with the most significant bit.  For
# example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
# 01101 in binary, which is 13.
# 
# For all leaves in the tree, consider the numbers represented by the path from
# the root to that leaf.
# 
# Return the sum of these numbers.
# 
# 
# 
# Example 1:
#             1
#           0   1
#          0 1 0 1
# 
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is between 1 and 1000.
# node.val is 0 or 1.
# The answer will not exceed 2^31 - 1.
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

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = []
        curr = ''
        self.search(root, curr, res)
        sumVal = 0
        for path in res:
            sumVal += self.binaryToDecimal(path)
        return sumVal

    def search(self, node, curr, res):
        curr += str(node.val)
        if not node.left and not node.right:
            res.append(curr)           
            return        
        if node.left:
            self.search(node.left, curr, res)
        if node.right:
            self.search(node.right, curr, res)
    
    def binaryToDecimal(self, bStr: str) -> int:
        res = 0
        b = str(int(bStr))
        length = len(b) - 1
        for i in b:
            res += (2 ** length) * int(i)
            length -= 1
        return res
# @lc code=end
# [1,0,1,0,1,0,1] 22
