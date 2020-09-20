#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
#
# algorithms
# Easy (47.39%)
# Likes:    500
# Dislikes: 264
# Total Accepted:    58.5K
# Total Submissions: 121.6K
# Testcase Example:  '["KthLargest","add","add","add","add","add"]\n[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'
#
# Design a class to find the kth largest element in a stream. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.
# 
# Your KthLargest class will have a constructor which accepts an integer k and
# an integer array nums, which contains initial elements from the stream. For
# each call to the method KthLargest.add, return the element representing the
# kth largest element in the stream.
# 
# Example:
# 
# 
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# 
# 
# Note: 
# You may assume that nums' length ≥ k-1 and k ≥ 1.
# 
#

# @lc code=start
import heapq
class KthLargest:
    
    def __init__(self, k: int, nums: [int]):
        self.k = k
        nums = sorted(nums, reverse=True)
        # res is the smallest one in big
        # len(big) == k
        self.small = list([-i for i in nums[min(k, len(nums)):]])
        self.big = list(nums[:min(k, len(nums))])
        heapq.heapify(self.small)
        heapq.heapify(self.big)

    def add(self, val: int) -> int:
        if len(self.big) < self.k:
            res = heapq.heappushpop(self.big, val)
            heapq.heappush(self.big, res)
            return res
        tmpFromBig = heapq.heappop(self.big)
        tmpFromSmall = -heapq.heappushpop(self.small, -val)
        if tmpFromBig >= tmpFromSmall:
            heapq.heappush(self.big, tmpFromBig)
            heapq.heappush(self.small, -tmpFromSmall)
            return tmpFromBig
        else:            
            heapq.heappush(self.small, -tmpFromBig)
            tmp = heapq.heappushpop(self.big, tmpFromSmall)
            heapq.heappush(self.big, tmp)
            return tmp


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
if __name__ == '__main__':
    s = KthLargest(1,[])
    print(s.add(3))
    print(s.add(5))
    print(s.add(10))
    print(s.add(9))
    print(s.add(4))
