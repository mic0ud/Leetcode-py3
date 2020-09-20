#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#
# https://leetcode.com/problems/smallest-string-starting-from-leaf/description/
#
# algorithms
# Medium (44.87%)
# Likes:    247
# Dislikes: 60
# Total Accepted:    18.8K
# Total Submissions: 41.8K
# Testcase Example:  '[0,1,2,3,4,3,4]'
#
# Given the root of a binary tree, each node has a value from 0 to 25
# representing the letters 'a' to 'z': a value of 0 represents 'a', a value of
# 1 represents 'b', and so on.
# 
# Find the lexicographically smallest string that starts at a leaf of this tree
# and ends at the root.
# 
# (As a reminder, any shorter prefix of a string is lexicographically smaller:
# for example, "ab" is lexicographically smaller than "aba".  A leaf of a node
# is a node that has no children.)

# Example 1:

# Input: [0,1,2,3,4,3,4]
# Output: "dba"

# Example 2:
 
# Input: [25,1,3,1,3,0,2]
# Output: "adz"
 
# Example 3:

# Input: [2,2,1,null,1,0,null,0]
# Output: "abc"

# Note:
# 
# 
# The number of nodes in the given tree will be between 1 and 8500.
# Each node in the tree will have a value between 0 and 25.


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ''
        
        def search(node, s, res: []):
            s = s+chr(node.val+97)
            if not node.left and not node.right:
                if not res[0] or (len(res[0]) == 1 and len(s) > 1):
                    res[0] = s[::-1]
                else:
                    c = s[::-1]
                    res[0] = res[0] if res[0] < c else c
                return
            if node.left:
                search(node.left, s, res)
            if node.right:
                search(node.right, s, res)

        res = ['']
        search(root, '', res)
        return res[0]
# @lc code=end
# [4,0,1,1]
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    s.smallestFromLeaf(root)