#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (23.80%)
# Likes:    973
# Dislikes: 28
# Total Accepted:    28.4K
# Total Submissions: 118.1K
# Testcase Example:  '[1]\n1'
#
# Return the length of the shortest, non-empty, contiguous subarray of A with
# sum at least K.
# 
# If there is no non-empty subarray with sum at least K, return -1.

# Example 1:
# 
# 
# Input: A = [1], K = 1
# Output: 1

# Example 2:
# 
# 
# Input: A = [1,2], K = 4
# Output: -1

# Example 3:
# 
# 
# Input: A = [2,-1,2], K = 3
# Output: 3

# Note:
# 
# 
# 1 <= A.length <= 50000
# -10 ^ 5 <= A[i] <= 10 ^ 5
# 1 <= K <= 10 ^ 9


# @lc code=start
from collections import deque
import heapq
class Solution:
    def shortestSubarray(self, A: [int], K: int) -> int:
        pre_sum, i, res, minq, sum_dq = 0, -1, float('inf'), [], 0
        for j,n in enumerate(A):
            sum_dq += n
            heapq.heappush(minq, (sum_dq,j))
            while minq and sum_dq-minq[0][0] >= K:
                pre_sum, i = heapq.heappop(minq)   
                res = min(res, j-i)                 
            if sum_dq-pre_sum >= K:
                res = min(res, j-i)
                i += 1     
        return res if res < float('inf') else -1
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.shortestSubarray([11,47,97,35,-46,59,46,51,59,80,14,-6,2,20,96,1,18,74,-17,71], 282)
    s.shortestSubarray([56,-21,56,35,-9], 61)
    s.shortestSubarray([2,-1,2], 3)
    s.shortestSubarray([84,-37,32,40,95], 167)
