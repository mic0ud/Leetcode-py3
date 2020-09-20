#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#
# https://leetcode.com/problems/delete-nodes-and-return-forest/description/
#
# algorithms
# Medium (64.52%)
# Likes:    598
# Dislikes: 22
# Total Accepted:    32.2K
# Total Submissions: 49.4K
# Testcase Example:  '[1,2,3,4,5,6,7]\n[3,5]'
#
# Given the root of a binary tree, each node in the tree has a distinct value.
# 
# After deleting all nodes with a value in to_delete, we are left with a forest
# (a disjoint union of trees).
# 
# Return the roots of the trees in the remaining forest.  You may return the
# result in any order.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.
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
    def delNodes(self, root: TreeNode, to_delete: [int]) -> [TreeNode]:
        if not root:
            return []
        if not to_delete:
            return [root]
            
        def delete(node, vals: [int], res: []):
            left = node.left
            right = node.right
            if node.val in vals:
                if node in res:
                    res.remove(node)
                if left:
                    res.append(left)
                if right:
                    res.append(right)
            if left:
                delete(left, vals, res)
                if left.val in vals:
                    node.left = None
            if right:
                delete(right, vals, res)
                if right.val in vals:
                    node.right = None    

        res = [root]
        delete(root, to_delete, res) 
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    s.delNodes(root, [3,5])
