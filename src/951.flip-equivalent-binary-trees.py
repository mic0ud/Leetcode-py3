#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
#
# https://leetcode.com/problems/flip-equivalent-binary-trees/description/
#
# algorithms
# Medium (65.22%)
# Likes:    435
# Dislikes: 17
# Total Accepted:    32.8K
# Total Submissions: 50.1K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]'
#
# For a binary tree T, we can define a flip operation as follows: choose any
# node, and swap the left and right child subtrees.
# 
# A binary tree X is flip equivalent to a binary tree Y if and only if we can
# make X equal to Y after some number of flip operations.
# 
# Write a function that determines whether two binary trees are flip
# equivalent.  The trees are given by root nodes root1 and root2.

# Example 1:
# 
# 
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =
# [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
 
# Note:
# 
# 
# Each tree will have at most 100 nodes.
# Each value in each tree will be a unique integer in the range [0, 99].


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def checkFlip(root1, root2) -> bool:
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False   
            l1 = checkFlip(root1.left, root2.left)
            r1 = checkFlip(root1.right, root2.right)
            if l1 and r1:
                return True
            else:
                l2 = checkFlip(root1.right, root2.left)
                r2 = checkFlip(root1.left, root2.right)           
                return l2 and r2
                
        return checkFlip(root1, root2)
# @lc code=end

