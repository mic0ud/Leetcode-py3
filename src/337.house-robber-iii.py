#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (49.22%)
# Likes:    1997
# Dislikes: 41
# Total Accepted:    129.3K
# Total Submissions: 261.1K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called the "root." Besides the root, each house
# has one and only one parent house. After a tour, the smart thief realized
# that "all houses in this place forms a binary tree". It will automatically
# contact the police if two directly-linked houses were broken into on the same
# night.
# 
# Determine the maximum amount of money the thief can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [3,2,3,null,3,null,1]
# 
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
# 
# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# 
# Example 2:
# 
# 
# Input: [3,4,5,1,3,null,1]
# 
#     3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
# 
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue
from collections import defaultdict
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        def search(node) -> [int]: # [rob, not_rob]
            if not node:
                return [0, 0]
            l = search(node.left)        
            r = search(node.right)        
            return [node.val+l[1]+r[1], max(l)+max(r)] # if not rob node, it doesn't matter if rob node.left, node.right or not, just pick the max val
        
        return max(search(root))

    def rob_SLOW(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum_map = defaultdict(int)

        def search(node) -> int:
            if not node:
                return 0
            if sum_map[node] > 0:
                return sum_map[node]
            tmp1, tmp2 = node.val, 0
            # 1. rob node, and the children of node.left and node.right
            # 2. rob node.left and node.right
            if node.left:
                tmp1 += search(node.left.left) + search(node.left.right)
                tmp2 += search(node.left)
            if node.right:
                tmp1 += search(node.right.left) + search(node.right.right)
                tmp2 += search(node.right)
            sum_map[node] = max(tmp1, tmp2)
            return sum_map[node]

        search(root)
        return sum_map[root]

        
    def rob_WRONG(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = Queue()
        q.put([root])
        res = []
        while not q.empty():
            nodes = q.get()
            level = []
            tmpSum = 0
            for n in nodes:
                tmpSum += n.val
                if n.left:
                    level.append(n.left)
                if n.right:
                    level.append(n.right)
            res.append(tmpSum)
            if level:
                q.put(level)
        dp_with_i = [0 for _ in range(len(res))]
        dp_without_i = [0 for _ in range(len(res))]
        dp_with_i[0] = res[0]
        dp_without_i[0] = 0
        for i in range(len(res)):
            dp_with_i[i] = res[i] + dp_without_i[i-1]
            dp_without_i[i] = max(dp_with_i[i-1], dp_without_i[i-1])
        return max(dp_with_i[len(res)-1], dp_without_i[len(res)-1])
# @lc code=end
# [4,1,null,2,null,3]
if __name__ == '__main__':
    s = Solution()
    # root = TreeNode(3)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.right = TreeNode(3)
    # root.right.right = TreeNode(1)

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)

    s.rob(root)