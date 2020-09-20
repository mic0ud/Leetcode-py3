#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (39.99%)
# Likes:    2327
# Dislikes: 137
# Total Accepted:    203.9K
# Total Submissions: 508.4K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# 
# Example:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
# 
# Follow up:
# Could you solve it in linear time?
#

# @lc code=start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        if not nums:
            return []     
        n = len(nums)
        res = []
        dq = deque()
        for i in range(k):
            while len(dq) > 0 and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])
        for i in range(k,n):
            if dq[0] <= i-k:
                dq.popleft()
            while len(dq) > 0 and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i) 
            res.append(nums[dq[0]])
        return res

    # MONOTONIC QUEUE
    # First traversing through K in the nums and only adding maximum value's index to the deque.
    # Note: We are olny storing the index and not the value.
    # Now, Comparing the new value in the nums with the last index value from deque,
    # and if new valus is less, we don't need it
    # Now we will traverse from k to the end of array and do 4 things
    # 1. Appending left most indexed value to the result
    # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
    # 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
    # 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)
    def maxSlidingWindow_(self, nums: [int], k: int) -> [int]:
        if not nums:
            return []     
        n = len(nums)
        res = []
        dq = deque([0])
        for i in range(1, k):
            while len(dq) > 0 and nums[dq[-1]] <= nums[i]:   
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])
        for i in range(1, n-k+1):
            if dq[0] < i:
                dq.popleft()
            while len(dq) > 0 and nums[dq[-1]] <= nums[i+k-1]:
                dq.pop()
            dq.append(i+k-1)
            res.append(nums[dq[0]])
        return res

    def maxSlidingWindow_SLOW(self, nums: [int], k: int) -> [int]:   
        if not nums:
            return []     
        n = len(nums)
        res = []
        for i in range(n-k+1):
            res.append(max(nums[i:i+k]))
        return res
# @lc code=end
# [9,10,9,-7,-4,-8,2,-6]\n5
if __name__ == '__main__':
    s = Solution()
    s.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6],5)