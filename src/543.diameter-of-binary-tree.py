#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (47.76%)
# Likes:    2007
# Dislikes: 123
# Total Accepted:    193.7K
# Total Submissions: 402.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# 
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
# 
# 
# 
# Example:
# Given a binary tree 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def depth(node, res: [int]) -> int:
            if not node:
                return 0
            l = depth(node.left, res)
            r = depth(node.right, res)
            res[0] = max(res[0], l+r)
            return max(l, r) + 1   
                     
        res = [0]
        depth(root, res)
        return res[0]


    def diameterOfBinaryTree_TLE(self, root: TreeNode) -> int:
        if not root:
            return 0
        g = defaultdict(list)
        leaves = []
        self.buildGraph(root, None, g, leaves)
        
        def dfs(node, depth, res: [int], visited: {}):
            if visited[node]:
                res[0] = max(res[0], depth-1)
                return
            visited[node] = True
            # found = False
            for n in g[node]:
                # if not visited[n]:
                #     found = True
                dfs(n, depth+1, res, visited)
            # if not found:
            #     res[0] = max(res[0], depth)

        def dfs2(val, depth, res: [int], visited: {}):
            if visited[val]:
                res[0] = max(res[0], depth)
                return
            visited[val] = True
            for n in g[val]:
                dfs2(n, depth+1, res, visited)

        res = [0]
        count = 0
        for lf in leaves:
            visited = defaultdict(bool)
            dfs(lf, 0, res, visited)
            count = max(count, res[0])
        return count
    
    def buildGraph(self, node, pre, g: {}, leaves: []):
        if not node:
            return
        if pre:
            g[node].append(pre)
        if node.left:
            g[node].append(node.left)
            self.buildGraph(node.left, node, g, leaves)
        if node.right:
            g[node].append(node.right)
            self.buildGraph(node.right, node, g, leaves)
        if not node.left and not node.right:
            leaves.append(node)

    def buildGraph2(self, node, pre, g: {}, leaves: []):
        if not node:
            return
        if pre:
            g[node.val].append(pre.val)
        if node.left:
            g[node.val].append(node.left.val)
            self.buildGraph2(node.left, node, g, leaves)
        if node.right:
            g[node.val].append(node.right.val)
            self.buildGraph2(node.right, node, g, leaves)
        if not node.left and not node.right:
            leaves.append(node.val)
# @lc code=end
# [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    s.diameterOfBinaryTree(root)
