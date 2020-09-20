#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (44.20%)
# Likes:    2575
# Dislikes: 183
# Total Accepted:    143.5K
# Total Submissions: 322.1K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
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

from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        
        def search(node, val, d:{}, res: []):
            if not node:
                return
            val += node.val
            res[0] += d[val-target]
            d[val] += 1
            search(node.left, val, defaultdict(int, d), res)
            search(node.right, val, defaultdict(int, d), res)
        
        res = [0]
        search(root, 0, prefixSum, res)
        return res[0]

    def pathSum_TLE(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        
        def search(node, val, start, res: [()]):
            if not node:
                return
            val += node.val
            if val == target:
                startEnd = (start, node)
                if startEnd not in res:
                    res.append(startEnd)
            search(node.left, val, start, res)
            search(node.right, val, start, res)
            search(node.left, 0, node.left, res)
            search(node.right, 0, node.right ,res)

        res = []
        search(root, 0, root, res)
        return len(res)
# @lc code=end
# [1,null,2,null,3,null,4,null,5]\n3
# [1,-2,-3,1,3,-2,null,-1]\n-1
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    # root.right = TreeNode(2)
    # root.right.right = TreeNode(3)
    # root.right.right.right = TreeNode(4)
    # root.right.right.right.right = TreeNode(5)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.right.left = TreeNode(-2)
    root.left.left = TreeNode(1)
    root.left.left.left = TreeNode(-1)
    root.left.right = TreeNode(3)   
    s.pathSum(root, -1)