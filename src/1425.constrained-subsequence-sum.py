#
# @lc app=leetcode id=1425 lang=python3
#
# [1425] Constrained Subsequence Sum
#
# https://leetcode.com/problems/constrained-subsequence-sum/description/
#
# algorithms
# Hard (42.14%)
# Likes:    235
# Dislikes: 12
# Total Accepted:    6.2K
# Total Submissions: 14.2K
# Testcase Example:  '[10,2,-10,5,20]\n2'
#
# Given an integer array nums and an integer k, return the maximum sum of a
# non-empty subsequence of that array such that for every two consecutive
# integers in the subsequence, nums[i] and nums[j], where i < j, the condition
# j - i <= k is satisfied.
# 
# A subsequence of an array is obtained by deleting some number of elements
# (can be zero) from the array, leaving the remaining elements in their
# original order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest
# number.
# 
# 
# Example 3:
# 
# 
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: [int], k: int) -> int:
        n = len(nums)
        res = [float('-inf') for _ in range(n)]
        res[0] = nums[0]
        dq = deque()
        for i in range(n):
            res[i] = nums[i] + (dq[0] if len(dq) > 0 else 0)
            while len(dq) > 0 and dq[-1] <= res[i]:
                dq.pop()
            if res[i] > 0:
                dq.append(res[i])
            if i >= k and len(dq) > 0 and dq[0] == res[i-k]:
                dq.popleft()
        return max(res)

    def constrainedSubsetSum_(self, A: [int], k: int) -> int:
        """
        Transition: A[i] = max(0, A[i - k], A[i - k + 1], .., A[i - 1]) + A[i]. (@lee215 modifies the input A directly)            
        Translated into a traditional dp: dp[i] = max(0, dp[i - k], dp[i - k + 1], .., dp[i -1]) + A[i]
        dp[i] is the max sum we can have from A[:i] when A[i] has been chosen.
        """ 
        # `deque` stores dp[i - k], dp[i-k+1], .., dp[i - 1] whose values are larger than 0 in a decreasing order
        # Note that the length of `deque` is not necessarily `k`. The values smaller than dp[i-1] will be discarded. If u r confused, go on and come back later. 
        deque = deque() 
        for i in xrange(len(A)):
            # deque[0] is the max of (0, dp[i - k], dp[i-k+1], .., dp[i - 1])
            A[i] += deque[0] if deque else 0 
            # 1. We always want to retrieve the max of (0, dp[i - k], dp[i-k+1], .., dp[i - 1]) from `deque`
            # 2. We expect dp[i] to be added to `deque` so that we can compute dp[i + 1] in the next iteration
            # 3. So, if dp[i] is larger than some old values, we can discard them safely.
            # 4. As a result, the length of `deque` is not necessarily `k`
            while len(deque) and A[i] >= deque[-1]:
                deque.pop()
            # no need to store the negative value
            if A[i] > 0:
                deque.append(A[i])
            # we do not need the value of A[i - k] when computing dp[i+1] in the next iteration, because `j - i <= k` has to be satisfied.
            if i >= k and deque and deque[0] == A[i - k]:
                deque.popleft()
        return max(A)   
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.constrainedSubsetSum([10,-2,-10,-5,20],2)
