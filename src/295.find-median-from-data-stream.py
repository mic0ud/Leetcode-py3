#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (39.71%)
# Likes:    1659
# Dislikes: 32
# Total Accepted:    144.4K
# Total Submissions: 361.8K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
# 
# [2,3,4], the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# 
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
# 
# 
# 
# 
# Example:
# 
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 
# 
# 
# Follow up:
# 
# 
# If all integer numbers from the stream are between 0 and 100, how would you
# optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how
# would you optimize it?
# 
# 
#

# @lc code=start
import bisect 
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # always half of the data
        self.small = []
        # half or half + 1
        self.big = []

    # heapq is min heap, good for self.big, but need some extra work for self.small
    def addNum(self, num: int) -> None:
        # push to big
        if len(self.small) == len(self.big):
            n = heapq.heappushpop(self.small, -num)
            heapq.heappush(self.big, -n)
        # push to small
        else:
            n = heapq.heappushpop(self.big, num)
            heapq.heappush(self.small, -n)            


    def findMedian(self) -> float:
        return self.big[0] if len(self.big) > len(self.small) else (self.big[0] - self.small[0]) / 2


    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.nums = []

    # def addNum(self, num: int) -> None:
    #     left = bisect.bisect_left(self.nums, num)
    #     self.nums.insert(left, num)


    # def findMedian(self) -> float:
    #     n = len(self.nums)
    #     return self.nums[n // 2] if n % 2 > 0 else (self.nums[n//2]+self.nums[n//2-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
# [1,2,3,4,5] 3, 4
if __name__ == '__main__':
    s = MedianFinder()
    s.addNum(1)
    s.addNum(2)
    print(s.findMedian())
    s.addNum(3)
    print(s.findMedian())