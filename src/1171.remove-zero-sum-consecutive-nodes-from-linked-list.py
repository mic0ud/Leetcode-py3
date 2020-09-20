#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/
#
# algorithms
# Medium (41.71%)
# Likes:    280
# Dislikes: 24
# Total Accepted:    10K
# Total Submissions: 24.1K
# Testcase Example:  '[1,2,-3,3,1]'
#
# Given the head of a linked list, we repeatedly delete consecutive sequences
# of nodes that sum to 0 until there are no such sequences.
# 
# After doing so, return the head of the final linked list.  You may return any
# such answer.
# 
# 
# (Note that in the examples below, all sequences are serializations of
# ListNode objects.)
# 
# Example 1:
# 
# 
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2,3,-3,-2]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The given linked list will contain between 1 and 1000 nodes.
# Each node in the linked list has -1000 <= node.val <= 1000.
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
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        '''
        Iterate for the first time,
        calculate the prefix sum,
        and save the it to seen[prefix]

        Iterate for the second time,
        calculate the prefix sum,
        and directly skip to last occurrence of this prefix
        '''
        # target = 0
        prefix, seen = 0, {}
        seen[0] = dummy = ListNode(0)
        dummy.next = head
        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next
        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next
        return dummy.next
# @lc code=end

