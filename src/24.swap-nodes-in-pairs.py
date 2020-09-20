#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (47.13%)
# Likes:    1733
# Dislikes: 152
# Total Accepted:    406K
# Total Submissions: 843.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p1, p2, res, prev = head, head.next, head.next, None
        while p2:
            if prev:
                prev.next = p2
            prev = p1
            tmp = p2.next
            p2.next = p1
            prev.next = tmp
            p1 = tmp
            p2 = p1.next if p1 else None
        return res
# @lc code=end

