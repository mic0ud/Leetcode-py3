#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#
# https://leetcode.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (77.56%)
# Likes:    1375
# Dislikes: 186
# Total Accepted:    107.7K
# Total Submissions: 138.5K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 
# Given an integer array with no duplicates. A maximum tree building on this
# array is defined as follow:
# 
# The root is the maximum number in the array. 
# The left subtree is the maximum tree constructed from left part subarray
# divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray
# divided by the maximum number. 
# 
# 
# 
# 
# Construct the maximum tree by the given array and output the root node of
# this tree.
# 
# 
# Example 1:
# 
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
# 
# ⁠     6
# ⁠   /   \
# ⁠  3     5
# ⁠   \    / 
# ⁠    2  0   
# ⁠      \
# ⁠       1
# 
# 
# 
# Note:
# 
# The size of the given array will be in the range [1,1000].
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: [int]) -> TreeNode:
        if not nums:
            return None
        return self.construct(nums, 0, len(nums))
        
    def construct(self, nums: [int], left: int, right: int) -> TreeNode:
        if left >= right:
            return None
        maxNum = max(nums[left:right])
        maxNumIndex = nums.index(maxNum)
        node = TreeNode(maxNum)
        node.left = self.construct(nums, left, maxNumIndex)
        node.right = self.construct(nums, maxNumIndex+1, right)
        return node
# @lc code=end

