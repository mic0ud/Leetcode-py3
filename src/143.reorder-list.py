#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (33.13%)
# Likes:    1234
# Dislikes: 92
# Total Accepted:    185.2K
# Total Submissions: 555K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# Example 1:
# 
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# 
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
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
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        p1 = head
        p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        if not p1.next:
            return head

        halfHead = p1.next
        p1.next = None
        half = self.reverse(halfHead)
        p3 = head
        while half:
            tmp = p3.next
            p3.next = half
            half = half.next
            p3.next.next = tmp
            p3 = tmp
        return head

    def reverse(self, head):
        if not head:
            return None
        prev = None
        curr = head       
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
# @lc code=end

