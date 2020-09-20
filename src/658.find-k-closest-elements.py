#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (39.17%)
# Likes:    946
# Dislikes: 196
# Total Accepted:    77.6K
# Total Submissions: 196.2K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# 
# Given a sorted array, two integers k and x, find the k closest elements to x
# in the array.  The result should also be sorted in ascending order.
# If there is a tie,  the smaller elements are always preferred.
# 
# 
# Example 1:
# 
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]

# Example 2:
# 
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]

# Note:
# 
# The value k is positive and will always be smaller than the length of the
# sorted array.
# ⁠Length of the given array is positive and will not exceed 10^4
# ⁠Absolute value of elements in the array and x will not exceed 10^4

# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list
# of integers). Please reload the code definition to get the latest changes.


# @lc code=start
from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: [int], k: int, x: int) -> [int]:
        if not arr:
            return []
        left, right = 0, len(arr)-k
        while left < right:
            mid = (left+right) // 2
            if x-arr[mid] <= arr[mid+k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left:left+k]

    def findClosestElements_(self, arr: [int], k: int, x: int) -> [int]:
        if not arr:
            return []
        idx = bisect_left(arr, x)
        if idx == 0:
            return arr[:k]
        if idx == len(arr):
            return arr[-k:]
        l, r = idx-1, idx
        while r < len(arr) and arr[r] == x:
            r += 1
            k -= 1
        if k == 0:
            return arr[idx:r]
        while l >= 0 and r < len(arr) and k > 0:
            while l >= 0 and k > 0 and abs(arr[l]-x) <= abs(arr[r]-x):
                l -= 1
                k -= 1
            while r < len(arr) and k > 0 and abs(arr[l]-x) > abs(arr[r]-x):
                r += 1
                k -= 1
        while l >= 0 and k > 0:
            l -= 1
            k -= 1
        while r < len(arr) and k > 0:
            r += 1
            k -= 1
        return arr[l+1:r]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findClosestElements([0,1,2,4,5],4,3)
