#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#
# https://leetcode.com/problems/serialize-and-deserialize-bst/description/
#
# algorithms
# Medium (49.46%)
# Likes:    1026
# Dislikes: 62
# Total Accepted:    87K
# Total Submissions: 172.7K
# Testcase Example:  '[2,1,3]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary search tree. There
# is no restriction on how your serialization/deserialization algorithm should
# work. You just need to ensure that a binary search tree can be serialized to
# a string and this string can be deserialized to the original tree structure.
# 
# The encoded string should be as compact as possible.
# 
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        self.preorder(root, res)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        nodes = data.split(',')
        if not nodes or not nodes[0]:
            return None
        return self.construct(nodes)
        
    def preorder(self, node, res: []):
        if not node:
            res.append('#')
            return
        res.append(str(node.val))
        self.preorder(node.left, res)
        self.preorder(node.right, res)

    def construct(self, nodes) -> TreeNode:
        if not nodes:
            return None
        val = nodes.pop(0)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = self.construct(nodes)
        node.right = self.construct(nodes)
        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end
if __name__ == '__main__':
    s = Codec()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    data = s.serialize(root)
    s.deserialize(data)
