#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (51.91%)
# Likes:    978
# Dislikes: 128
# Total Accepted:    120.6K
# Total Submissions: 231.1K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
# 
# 
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        s1, s2 = '', ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next   
        s = str(int(s1)+int(s2))
        res = ListNode(int(s[0]))
        curr = res
        for c in s[1:]:
            curr.next = ListNode(int(c))
            curr = curr.next
        return res
# @lc code=end

