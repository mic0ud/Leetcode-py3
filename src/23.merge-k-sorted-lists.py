#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (36.98%)
# Likes:    3311
# Dislikes: 216
# Total Accepted:    499.5K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None 
        
import heapq
class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, id(l), l))
        if not heap:
            return None
        head = heapq.heappop(heap)[-1]
        dummy = head
        while heap:
            if head.next:
                heapq.heappush(heap, (head.next.val, id(head.next), head.next))
            head.next = heapq.heappop(heap)[-1]
            head = head.next
        return dummy

    def mergeKLists_SLOW(self, lists: [ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        res = self.merge(lists[0], lists[1])
        for l in lists[2:]:
            res = self.merge(res, l)
        return res
        
    def merge(self, l1, l2) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        dummy = head
        while l1 and l2:
            while l1 and l2 and l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            while l1 and l2 and l2.val <= l1.val:
                head.next = l2
                l2 = l2.next
                head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next
# @lc code=end
# [[1,4,5],[1,3,4],[2,6]]
if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    lists = [l1,l2,l3]
    s.mergeKLists(lists)
