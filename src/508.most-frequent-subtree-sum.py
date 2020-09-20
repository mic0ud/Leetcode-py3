#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#
# https://leetcode.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (55.90%)
# Likes:    495
# Dislikes: 97
# Total Accepted:    60.3K
# Total Submissions: 107K
# Testcase Example:  '[5,2,-3]'
#
# 
# Given the root of a tree, you are asked to find the most frequent subtree
# sum. The subtree sum of a node is defined as the sum of all the node values
# formed by the subtree rooted at that node (including the node itself). So
# what is the most frequent subtree sum value? If there is a tie, return all
# the values with the highest frequency in any order.
# 
# 
# Examples 1
# Input:
# 
# ⁠ 5
# ⁠/  \
# 2   -3
# 
# return [2, -3, 4], since all the values happen only once, return all of them
# in any order.
# 
# 
# Examples 2
# Input:
# 
# ⁠ 5
# ⁠/  \
# 2   -5
# 
# return [2], since 2 happens twice, however -5 only occur once.
# 
# 
# Note:
# You may assume the sum of values in any subtree is in the range of 32-bit
# signed integer.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> [int]:
        if not root:
            return []
        count = Counter()

        def dfs(node) -> int:
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            count[s] += 1
            return s
        dfs(root)
        maxSum = max(count.values())
        return [s for s in count if count[s] == maxSum]
# @lc code=end

