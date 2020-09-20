#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (37.37%)
# Likes:    2291
# Dislikes: 309
# Total Accepted:    338K
# Total Submissions: 896.2K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        half = []
        slow, fast = head, head
        while fast and fast.next:
            half.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        while slow:
            if slow.val != half.pop():
                return False
            slow = slow.next
        return True
# @lc code=end
# [1,0,0]
