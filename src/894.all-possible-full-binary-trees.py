#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#
# https://leetcode.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (72.27%)
# Likes:    639
# Dislikes: 64
# Total Accepted:    28.1K
# Total Submissions: 38.7K
# Testcase Example:  '7'
#
# A full binary tree is a binary tree where each node has exactly 0 or 2
# children.
# 
# Return a list of all possible full binary trees with N nodes.  Each element
# of the answer is the root node of one possible tree.
# 
# Each node of each tree in the answer must have node.val = 0.
# 
# You may return the final list of trees in any order.
# 
# 
# 
# Example 1:
# 
# 
# Input: 7
# Output:
# [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 20
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
from copy import deepcopy
class Solution:
    def allPossibleFBT(self, N: int) -> [TreeNode]:
        if N % 2 == 0:
            return []
        # dp[i]: list of nodes at N == i
        dp = [[] for _ in range(N+1)]
        dp[1] = [TreeNode(0)]
        for i in range(3, N+1, 2):
            for j in range(1, i, 2):
                for l in dp[j]:
                    for r in dp[i-j-1]:
                        dp[i].append(self.addNodes(l, r))
        return dp[N]

    def addNodes(self, left, right):
        root = TreeNode(0)
        root.left = left
        root.right = right
        return root

# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.allPossibleFBT(7)
