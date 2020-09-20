#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (47.65%)
# Likes:    1040
# Dislikes: 186
# Total Accepted:    52.5K
# Total Submissions: 107.8K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them.
# 
# Two trees are duplicate if they have the same structure with same node
# values.
# 
# Example 1: 
# 
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# 
# The following are two duplicate subtrees:
# 
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# 
# and
# 
# 
# ⁠   4
# 
# Therefore, you need to return above trees' root in the form of a list.
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        seen = {}
        def search(node, res:[]) -> str:
            if not node:
                return ''
            l = search(node.left, res)
            r = search(node.right, res)
            tmp = (l if l else 'l') + ',' + (r if r else 'r') + ',' + str(node.val)
            if tmp in seen:
                if not seen[tmp]:
                    res.append(node)
                    seen[tmp] = True
            else:
                seen[tmp] = False
            return tmp
        res = []
        search(root, res)
        return res    
# @lc code=end

