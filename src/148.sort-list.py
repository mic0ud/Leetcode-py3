#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (38.14%)
# Likes:    2045
# Dislikes: 102
# Total Accepted:    225.9K
# Total Submissions: 580.8K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next            
        prev.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(slow)
        return self.merge(h1, h2)
    
    def merge(self, n1: ListNode, n2: ListNode) -> ListNode:
        if not n1:
            return n2
        if not n2:
            return n1
        if n1.val <= n2.val:
            n1.next = self.merge(n1.next, n2)
            return n1
        else:
            n2.next = self.merge(n1, n2.next)
            return n2

    def sortList_INSERTION_TLE(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        left, right, p = head, head, head.next 
        while p:            
            if p.val <= left.val:
                tmp = p.next
                p.next = left
                left = p
                p = tmp
            elif p.val >= right.val:
                right.next = p
                p = p.next
                right = right.next                
            else:
                pNext = p.next
                tmp = left
                while tmp.next and tmp.next.val < p.val:
                    tmp = tmp.next
                tmpNext = tmp.next
                tmp.next = p
                p.next = tmpNext
                p = pNext
            right.next = None
        return left        
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    s.sortList(head)
