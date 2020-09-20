#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (50.90%)
# Likes:    1315
# Dislikes: 30
# Total Accepted:    48.1K
# Total Submissions: 92.4K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# We are given a binary tree (with root node root), a target node, and an
# integer value K.
# 
# Return a list of the values of all nodes that have a distance K from the
# target node.  The answer can be returned in any order.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 
# Output: [7,4,1]
# 
# Explanation: 
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
# 
#             3
#          5       1
#       6    2   0   8
#          7   4
#
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these
# objects.
# 
# 
# 
# 
# Note:
# 
# 
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
# 
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
from queue import Queue
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> [int]:
        return self.distanceK_GRAPH(root, target, K)

    def distanceK_GRAPH(self, root: TreeNode, target: TreeNode, K: int) -> [int]:
        if not root or not target:
            return []
        if K == 0:
            return [target.val]

        g = defaultdict(list)
        
        def build_grapgh(node: TreeNode, prev: TreeNode):
            if not node:
                return
            if prev:
                g[node.val].append(prev.val)
            if node.left:
                g[node.val].append(node.left.val)
                build_grapgh(node.left, node)
            if node.right:
                g[node.val].append(node.right.val)
                build_grapgh(node.right, node)     

        build_grapgh(root, None)     

        if K > len(g)-1:
            return []

        visited = set()
        visited.add(target.val)
        q = Queue()
        q.put(g[target.val])
        k = 0
        while not q.empty():
            k += 1
            level = q.get()
            if k == K:
                return list(set(level))
            tmp = []
            for n in level:
                visited.add(n)
                for i in g[n]:
                    if i not in visited:
                        tmp.append(i)
            if tmp:
                q.put(tmp)
        return []

    def distanceK_UGLY(self, root: TreeNode, target: TreeNode, K: int) -> [int]:
        if not root:
            return []

        res = []
        added = []
        def dfs1(node, distance):
            if not node:
                return
            if distance == 0 and node not in added:
                added.append(node)
                res.append(node.val)
                return
            dfs1(node.left, distance-1)
            dfs1(node.right, distance-1)
        
        # left: -1, right: 1
        def dfs2(node, val, d, path: [[int]], res: []):
            if not node:
                return           
            if node.val == val:
                res[0] = list(path)
                return
            dfs2(node.left, val, d+1, list(path+[[node, -1]]), res) 
            dfs2(node.right, val, d+1, list(path+[[node, 1]]), res)

        dfs1(target, K)
        if root == target or K == 0:
            return res

        rootToTargetRes= [[]]
        dfs2(root, target.val, 0, [], rootToTargetRes)
        rootToTarget = rootToTargetRes[0]
        targetDepth = len(rootToTarget)
        for i in range(targetDepth):
            currDepth = targetDepth - i
            if currDepth > K: continue
            elif currDepth == K: res.append(rootToTarget[i][0].val)
            else:
                dfs1(rootToTarget[i][0].right, K - currDepth - 1) if rootToTarget[i][1] < 0 else dfs1(rootToTarget[i][0].left, K - currDepth - 1)

        return res
# @lc code=end
# [0,null,1,2,5,null,3,null,null,null,4]\n2\n2
# [4,5,0], [4,0]
# [0,1,null,3,2]\n2\n1
# [1,1], [1]

# [0,5,1,null,null,2,6,null,3,null,null,4,null,7]\n7\n3
# [2,6], [2]

# [0,null,1,null,2,null,3]\n1\n2
# [0,6,1,null,null,null,2,7,3,null,8,4,9,null,null,null,5]\n7\n5
if __name__ == '__main__':
    s = Solution()
    # root = TreeNode(0)
    # root.right = TreeNode(1)
    # root.right.right = TreeNode(2)
    # root.right.right.right = TreeNode(3)
    # s.distanceK(root, root.right, 2)
    root = TreeNode(0)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(6)
    root.right.left.right = TreeNode(3)
    root.right.left.right.left = TreeNode(4)
    root.right.left.right.left.left = TreeNode(7)
    s.distanceK(root, root.right.left.right.left.left, 3)