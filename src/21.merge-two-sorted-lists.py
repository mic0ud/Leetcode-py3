#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (49.96%)
# Likes:    3195
# Dislikes: 469
# Total Accepted:    808.5K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        dummy = head
        while l1 and l2:
            while l1 and l2 and l1.val <= l2.val:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            while l1 and l2 and l2.val <= l1.val:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
        if not l1:
            dummy.next = l2
        if not l2:
            dummy.next = l1
        return head.next
# @lc code=end

