#
# @lc app=leetcode id=1300 lang=python3
#
# [1300] Sum of Mutated Array Closest to Target
#
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/description/
#
# algorithms
# Medium (45.87%)
# Likes:    197
# Dislikes: 32
# Total Accepted:    8.1K
# Total Submissions: 17.7K
# Testcase Example:  '[4,9,3]\n10'
#
# Given an integer array arr and a target value target, return the integer
# value such that when we change all the integers larger than value in the
# given array to be equal to value, the sum of the array gets as close as
# possible (in absolute difference) to target.
# 
# In case of a tie, return the minimum such integer.
# 
# Notice that the answer is not neccesarilly a number from arr.
# 
# 
# Example 1:
# 
# 
# Input: arr = [4,9,3], target = 10
# Output: 3
# Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's
# the optimal answer.
# 
# 
# Example 2:
# 
# 
# Input: arr = [2,3,5], target = 10
# Output: 5
# 
# 
# Example 3:
# 
# 
# Input: arr = [60864,25176,27249,21296,20204], target = 56803
# Output: 11361
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 1 <= arr[i], target <= 10^5
# 
#

# @lc code=start
from collections import defaultdict
from bisect import bisect_left
class Solution:
    def findBestValue(self, arr: [int], target: int) -> int:
        arr.sort(reverse=1)
        max_val = arr[0]
        while arr and target >= arr[-1]*len(arr):
            target -= arr.pop()
        if not arr:
            return max_val
        if target / len(arr) - target // len(arr) <= 0.5:  # Fractional part is <= 0.5
            # Select the smaller one especially when there's two candidates (== 0.5)
            return target // len(arr)
        return target // len(arr) + 1
        

    def findBestValue_SLOW(self, arr: [int], target: int) -> int:
        arr.sort()
        presum = [0]
        for i,a in enumerate(arr):
            presum.append(a+presum[i])
        dis, res, n = float('inf'), float('inf'), len(arr)
        for i in range(max(target, arr[-1])):
            idx = bisect_left(arr, i)
            curr = presum[idx] + i*(n-idx)
            if abs(curr-target) < dis:
                dis = abs(curr-target)
                res = i
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findBestValue([60864,25176,27249,21296,20204], 56803)
    s.findBestValue([4,9,3], 10)
