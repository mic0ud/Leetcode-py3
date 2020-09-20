#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
#
# algorithms
# Hard (30.21%)
# Likes:    677
# Dislikes: 23
# Total Accepted:    24.6K
# Total Submissions: 81.2K
# Testcase Example:  '[1,3,1]\n1'
#
# Given an integer array, return the k-th smallest distance among all the
# pairs. The distance of a pair (A, B) is defined as the absolute difference
# between A and B. 
# 
# Example 1:
# 
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0 
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# 
# 
# 
# Note:
# 
# 2 .
# 0 .
# 1 .
# 
# 
#

# @lc code=start
import heapq
class Solution:
    # def smallestDistancePair(self, nums: List[int], k: int) -> int:
    def smallestDistancePair(self, nums: [int], k: int) -> int:
        sortedNums = sorted(nums)
        minHeap = []
        distances = []
        for i in range(len(sortedNums)-1):
            candiate = sortedNums[i+1]-sortedNums[i]
            distances.append(candiate)  
        sortedDistances = sorted(distances)
        res = []
        heapq.heappush(minHeap, sortedDistances[0])
        while len(res) < k:
            c = heapq.heappop(minHeap)
            res.append(c)
            while 
        # minHeap = [] 
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         heapq.heappush(minHeap, abs(nums[j]-nums[i]))  
        # count = len(minHeap)    
        # for j in range(min(k, count)):
        #     res = heapq.heappop(minHeap)
        #     if j == k-1 or j == count - 1:
        #         return res
# @lc code=end
# [1,6,1]\n3
# [9,10,7,10,6,1,5,4,9,8]\n18
# [1, 4, 5, 6, 7, 8, 9, 9, 10, 10]
# [0, 0, 1, 1, 1, 1, 1, 1, 3]

if __name__ == '__main__':
    s = Solution()
    print(s.smallestDistancePair([9,10,7,10,6,1,5,4,9,8], 18))