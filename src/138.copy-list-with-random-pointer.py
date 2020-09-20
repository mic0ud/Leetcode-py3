#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (30.41%)
# Likes:    2387
# Dislikes: 564
# Total Accepted:    332.4K
# Total Submissions: 1M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]\r'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# The Linked List is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
# 
# 
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random
# pointer points to, or null if it does not point to any node.
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# Example 2:
# 
# 
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
# 
# 
# Example 4:
# 
# 
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
# 
# 
# 
# Constraints:
# 
# 
# -10000 <= Node.val <= 10000
# Node.random is null or pointing to a node in the linked list.
# Number of Nodes will not exceed 1000.
# 
# 
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        m = {}
        m[head] = 0
        nh = Node(head.val, None, None)
        randoms = [nh]
        dummy = Node(0,nh,None)
        p = head.next
        count = 1
        while p:    
            m[p] = count
            count += 1
            n = Node(p.val)
            randoms.append(n)           
            nh.next = n
            nh = nh.next
            p = p.next
        p = head
        nh = dummy.next
        i = 0
        while p:
            nh.random = randoms[m[p.random]] if p.random in m else None
            i += 1
            p = p.next
            nh = nh.next
        return dummy.next
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    head = Node(7)
    head.next = Node(13, None, head)
    head.next.next = Node(11)
    head.next.next.next = Node(10, None, head.next.next)
    head.next.next.next.next = Node(10, None, head.next)
    head.next.next.random = head.next.next.next.next
    s.copyRandomList(head)
