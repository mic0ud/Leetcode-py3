#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (34.42%)
# Likes:    1002
# Dislikes: 70
# Total Accepted:    38.7K
# Total Submissions: 112.1K
# Testcase Example:  '[1,3,5,4,7]'
#
# 
# Given an unsorted array of integers, find the number of longest increasing
# subsequence.
# 
# 
# Example 1:
# 
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1,
# 3, 5, 7].
# 
# 
# 
# Example 2:
# 
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1,
# and there are 5 subsequences' length is 1, so output 5.
# 
# 
# 
# Note:
# Length of the given array will be not exceed 2000 and the answer is
# guaranteed to be fit in 32-bit signed int.
# 
#

# @lc code=start
import collections
class Solution:
    def findNumberOfLIS(self, nums: [int]) -> int:
        if len(nums) < 2:
            return len(nums)
        dp = [1 for _ in range(len(nums)+1)]
        dp[0] = 0
        count = [1 for _ in range(len(nums)+1)]
        longest = 0
        for i in range(1, len(nums)):
            tmpMax = 1
            tmpMap = collections.defaultdict(int)
            tmpMap[1] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    tmpMap[dp[j+1]+1] += count[j+1]
                    tmpMax = max(tmpMax, dp[j+1]+1)
            dp[i+1] = tmpMax
            count[i+1] = tmpMap[tmpMax]
            longest = max(longest, dp[i+1])
        res = 0
        for i in range(len(dp)):
            if dp[i] == longest:
                res += count[i]
        return res 
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findNumberOfLIS([1,1,1,2,2,2,3,3,3])
