#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (37.21%)
# Likes:    2099
# Dislikes: 103
# Total Accepted:    253.5K
# Total Submissions: 677.2K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#

# @lc code=start
from collections import deque
class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        if not nums:
            return 0
        res, tmp_sum, i = float('inf'), 0, 0
        for j,n in enumerate(nums):
            tmp_sum += n
            while tmp_sum >= s:
                res = min(j-i+1, res)
                tmp_sum -= nums[i]
                i += 1                
        return res if res < float('inf') else 0

    def minSubArrayLen_(self, s: int, nums: [int]) -> int:
        if not nums:
            return 0
        res, dq, sum_dq = float('inf'), deque(), 0
        for n in nums:
            dq.append(n)
            sum_dq += n                
            while dq and sum_dq-dq[0] >= s:
                sum_dq -= dq[0]
                dq.popleft()
            if sum_dq >= s:
                res = min(res, len(dq))
        return res if res < float('inf') else 0
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minSubArrayLen(7,[2,3,1,2,4,3])
