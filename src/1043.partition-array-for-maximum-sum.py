#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#
# https://leetcode.com/problems/partition-array-for-maximum-sum/description/
#
# algorithms
# Medium (63.05%)
# Likes:    402
# Dislikes: 50
# Total Accepted:    12.3K
# Total Submissions: 19.4K
# Testcase Example:  '[1,15,7,9,2,5,10]\n3'
#
# Given an integer array A, you partition the array into (contiguous) subarrays
# of length at most K.  After partitioning, each subarray has their values
# changed to become the maximum value of that subarray.
# 
# Return the largest sum of the given array after partitioning.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,15,7,9,2,5,10], K = 3
# Output: 84
# Explanation: A becomes [15,15,15,9,10,10,10]
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= A.length <= 500
# 0 <= A[i] <= 10^6
# 
# 
# [1,15,14,10,2,7,5]

# @lc code=start

class Solution:
    def maxSumAfterPartitioning(self, A: [int], K: int) -> int:        
        n = len(A)
        # dp[i]: largest sum partition A[:i]
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            currMax = A[i-1]
            for j in range(1,min(i,K)+1):
                currMax = max(currMax, A[i-j])
                dp[i] = max(dp[i], dp[i-j]+j*currMax)
        return dp[-1]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maxSumAfterPartitioning([1,15,7,9,2,5,10],3)
