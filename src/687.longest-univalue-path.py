#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (34.71%)
# Likes:    1287
# Dislikes: 340
# Total Accepted:    75.4K
# Total Submissions: 215.6K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
# 
# The length of path between two nodes is represented by the number of edges
# between them.
# 
# 
# 
# Example 1:
# 
# Input:
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input:
# 
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# Output: 2
# 
# 
# 
# Note: The given binary tree has not more than 10000 nodes. The height of the
# tree is not more than 1000.
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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = [0]
        def depth(node) -> int:
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            left = left+1 if node.left and node.left.val == node.val else 0
            right = right+1 if node.right and node.right.val == node.val else 0
            res[0] = max(res[0], left+right)
            return max(left, right)
        depth(root)
        return res[0]

    def longestUnivaluePath_SLOW(self, root: TreeNode) -> int:
        if not root:
            return 0  
        
        g = defaultdict(list)
        self.build_graph(root, None, g)

        def dfs(node, count, visited: {}, res: []):
            visited[node] = True
            for n in g[node]:
                if n.val == node.val and not visited[n]:
                    dfs(n, count+1, visited, res)
            res[0] = max(res[0], count)

        res = [0]
        for n in g:
            visited = defaultdict(bool)
            dfs(n, 0, visited, res)
        return res[0]
    
    def build_graph(self, node, prev, g: {}):
        if not node:
            return
        if prev:
            g[node].append(prev)
        if node.left:
            g[node].append(node.left)
            self.build_graph(node.left, node, g)
        if node.right:
            g[node].append(node.right)        
            self.build_graph(node.right, node, g)
# @lc code=end
# [1,null,1,1,1,1,1,1]
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    s.longestUnivaluePath(root)