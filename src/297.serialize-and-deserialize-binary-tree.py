#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (43.71%)
# Likes:    2170
# Dislikes: 108
# Total Accepted:    242.9K
# Total Submissions: 553.2K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Example: 
# 
# 
# You may serialize the following tree:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
# 
# as "[1,2,3,null,null,4,5]"
# 
# 
# Clarification: The above format is the same as how LeetCode serializes a
# binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.
# 
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

    def serialize_BFS(self, root) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return ''
        q = deque([root])
        # level order traversal 
        while q:
            n = q.popleft()
            res.append(str(n.val) if n else '#')
            if n:
                q.append(n.left)
                q.append(n.right)
        return ','.join(res)    

    def deserialize_BFS(self, data) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        n = len(nodes)
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if i < n and nodes[i] != '#':
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1
            if i < n and nodes[i] != '#':
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        return root  

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end
# [1,2,3,null,null,4,5]
# [1, 2, 3, null, null, 4, 5, null, null, null, null]
# [1, null, 2, null, 3, null, 4, null, 5, null, null]
# [1, 2, null, 3, null, 4, null, 5, null, null, null]
if __name__ == '__main__':
    s = Codec()
    root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(5)
    # root.right = TreeNode(2)
    # root.right.right = TreeNode(3)
    # root.right.right.right = TreeNode(4)
    # root.right.right.right.right = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.left.left = TreeNode(5)
    print(s.serialize(root))