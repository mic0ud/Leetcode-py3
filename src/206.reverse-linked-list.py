#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (57.97%)
# Likes:    3369
# Dislikes: 78
# Total Accepted:    791.7K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList_ITER(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev, curr, next_ = None, head, head.next
        while curr:
            curr.next = prev
            if not next_:
                return curr
            prev = curr
            tmp = next_.next
            next_.next = curr
            curr = next_
            next_ = tmp
    
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        def reverse(node, prev) -> ListNode:
            if not node:
                return prev
            tmp = node.next
            node.next = prev
            return reverse(tmp, node)

        return reverse(head, None)
# @lc code=end
# [1,2,3,4,5]
