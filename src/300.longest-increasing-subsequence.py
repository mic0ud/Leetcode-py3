#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (41.67%)
# Likes:    3348
# Dislikes: 76
# Total Accepted:    290.3K
# Total Submissions: 695.6K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        return self.bruteForce(nums)

    def bruteForce(self, nums:[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            maxLen = dp[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    maxLen = max(maxLen, dp[j]+1)
            dp[i] = maxLen
        return max(dp)
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.bruteForce([1,3,6,7,9,4,10,5,6])