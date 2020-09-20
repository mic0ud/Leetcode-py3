#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
#
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/
#
# algorithms
# Medium (35.96%)
# Likes:    229
# Dislikes: 24
# Total Accepted:    12.4K
# Total Submissions: 34K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a binary tree root. Split the binary tree into two subtrees by removing
# 1 edge such that the product of the sums of the subtrees are maximized.
# 
# Since the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10.
# Their product is 110 (11*10)
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation:  Remove the red edge and get 2 binary trees with sum 15 and
# 6.Their product is 90 (15*6)
# 
# 
# Example 3:
# 
# 
# Input: root = [2,3,9,10,7,8,6,5,4,11,1]
# Output: 1025
# 
# 
# Example 4:
# 
# 
# Input: root = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# Each tree has at most 50000 nodes and at least 2 nodes.
# Each node's value is between [1, 10000].
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        pre_sum, mod = defaultdict(int), 10**9+7
        def calc_presum(node) -> int:
            if not node:
                return 0
            left = calc_presum(node.left)
            right = calc_presum(node.right)
            pre_sum[node] = left + right + node.val
            return pre_sum[node]
        calc_presum(root)
        res = [0]
        def search(node):
            if not node:
                return
            res[0] = max(res[0], pre_sum[node.left]*(pre_sum[root]-pre_sum[node.left]))
            res[0] = max(res[0], pre_sum[node.right]*(pre_sum[root]-pre_sum[node.right]))
            search(node.left)
            search(node.right)
        search(root)
        return res[0]%mod
# @lc code=end
# [1,null,2,3,4,null,null,5,6]
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(6)
    s.maxProduct(root)