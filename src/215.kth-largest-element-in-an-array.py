#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (50.90%)
# Likes:    2644
# Dislikes: 199
# Total Accepted:    479.1K
# Total Submissions: 937.9K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#
import heapq
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.kthSmallest(nums, len(nums)-k+1)

    def kthSmallest(self, nums, k) -> int:
        position = self.partition(nums, 0, len(nums)-1)
        if k < position+1:
            return self.kthSmallest(nums[:position], k)
        elif k > position+1:
            return self.kthSmallest(nums[position+1:], k-1-position)
        else:
            return nums[position]

    def partition(self, nums, l, r) -> int:
        postion = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[postion] = nums[postion], nums[l]
                postion += 1
            l += 1
        nums[postion], nums[r] = nums[r], nums[postion]
        return postion
# @lc code=end

# solutions
# O(nlgn) time
def findKthLargest1(self, nums, k):
    return sorted(nums, reverse=True)[k-1]
    
# O(nk) time, bubble sort idea, TLE
def findKthLargest2(self, nums, k):
    for i in range(k):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                # exchange elements, time consuming
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums[len(nums)-k]
    
# O(nk) time, selection sort idea
def findKthLargest3(self, nums, k):
    for i in range(len(nums), len(nums)-k, -1):
        tmp = 0
        for j in range(i):
            if nums[j] > nums[tmp]:
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    return nums[len(nums)-k]
    
# O(k+(n-k)lgk) time, min-heap
def findKthLargest4(self, nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    for _ in range(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)

# O(k+(n-k)lgk) time, min-heap        
def findKthLargest5(self, nums, k):
    return heapq.nlargest(k, nums)[k-1]
    
# O(n) time, quick selection
def findKthLargest(self, nums, k):
    # convert the kth largest to smallest
    return self.findKthSmallest(nums, len(nums)+1-k)
    
def findKthSmallest(self, nums, k):
    if nums:
        pos = self.partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return self.findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return self.findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]
 
# choose the right-most element as pivot   
# [8,7,3,2,1,5,6,4]
# low     l   
# [8,   7,3,2,1,5,6,4]
#    low    l
# [3, 7,  8,2,1,5,6,4]
#      low   l
# [3,2, 8, 7,1,5,6,4]
#         low  l
# [3,2, 1, 7,8,5,6,4]
def partition(self, nums, l, r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low