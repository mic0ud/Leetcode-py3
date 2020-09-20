#
# @lc app=leetcode id=1191 lang=python3
#
# [1191] K-Concatenation Maximum Sum
#
# https://leetcode.com/problems/k-concatenation-maximum-sum/description/
#
# algorithms
# Medium (24.90%)
# Likes:    215
# Dislikes: 23
# Total Accepted:    9K
# Total Submissions: 34.9K
# Testcase Example:  '[1,2]\n3'
#
# Given an integer array arr and an integer k, modify the array by repeating it
# k times.
# 
# For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2,
# 1, 2, 1, 2].
# 
# Return the maximum sub-array sum in the modified array. Note that the length
# of the sub-array can be 0 and its sum in that case is 0.
# 
# As the answer can be very large, return the answer modulo 10^9 + 7.

# Example 1:

# Input: arr = [1,2], k = 3
# Output: 9
 
# Example 2:
 
# Input: arr = [1,-2,1], k = 5, 1,-2,1, 1,-2,1, 1,-2,1, 1,-2,1, 1,-2,1
# Output: 2

# Example 3:

# Input: arr = [-1,-2], k = 7
# Output: 0

# Constraints:
# 1 <= arr.length <= 10^5
# 1 <= k <= 10^5
# -10^4 <= arr[i] <= 10^4

# @lc code=start
from collections import defaultdict
class Solution:
    def kConcatenationMaxSum(self, arr: [int], k: int) -> int:
        s, l, preSum = arr[0], len(arr), [0 for _ in range(len(arr))]
        dp1 = [0 for _ in range(l*2)] # i included
        dp2 = [0 for _ in range(l*2)] # i not included
        dp1[0], preSum[0] = arr[0], arr[0]
        if k > 1:
            arr += arr
        for i in range(1, len(arr)):            
            if i < l:
                s += arr[i]
                preSum[i] = s
            dp1[i] = max(arr[i], dp1[i-1]+arr[i])
            dp2[i] = max(dp1[i-1], dp2[i-1])
        res = max(max(dp1), max(dp2))
        if s <= 0:
            return res
        total, suffSum, tmp = s*k, [0 for _ in range(l)], 0
        for i in range(l-1,-1,-1):
            tmp += arr[i]
            suffSum[i] = tmp
        res = max(res, total-min(0,min(preSum))-min(0,min(suffSum)))
        return res % (10**9+7)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.kConcatenationMaxSum([-5,-2,0,0,3,9,-2,-5,4],5)
    s.kConcatenationMaxSum([1,2],1)
    s.kConcatenationMaxSum([-1,-2],7)
    s.kConcatenationMaxSum([1,2],3)
    s.kConcatenationMaxSum([1,-2,1],5)
