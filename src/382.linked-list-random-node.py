#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#
# https://leetcode.com/problems/linked-list-random-node/description/
#
# algorithms
# Medium (50.53%)
# Likes:    490
# Dislikes: 147
# Total Accepted:    64.2K
# Total Submissions: 125.8K
# Testcase Example:  '["Solution","getRandom"]\n[[[1,2,3]],[]]'
#
# Given a singly linked list, return a random node's value from the linked
# list. Each node must have the same probability of being chosen.
# 
# Follow up:
# What if the linked list is extremely large and its length is unknown to you?
# Could you solve this efficiently without using extra space?
# 
# 
# Example:
# 
# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
# 
# // getRandom() should return either 1, 2, or 3 randomly. Each element should
# have equal probability of returning.
# solution.getRandom();
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import randint
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        res, node, idx = self.head, self.head.next, 1
        while node:
            if randint(0,idx) == 0:
                res = node
            node = node.next
            idx += 1
        return res.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

