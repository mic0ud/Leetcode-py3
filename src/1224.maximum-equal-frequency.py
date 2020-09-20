#
# @lc app=leetcode id=1224 lang=python3
#
# [1224] Maximum Equal Frequency
#
# https://leetcode.com/problems/maximum-equal-frequency/description/
#
# algorithms
# Hard (31.69%)
# Likes:    134
# Dislikes: 16
# Total Accepted:    4.8K
# Total Submissions: 14.6K
# Testcase Example:  '[2,2,1,1,5,3,3,5]'
#
# Given an array nums of positive integers, return the longest possible length
# of an array prefix of nums, such that it is possible to remove exactly one
# element from this prefix so that every number that has appeared in it will
# have the same number of occurrences.
# 
# If after removing one element there are no remaining elements, it's still
# considered that every appeared number has the same number of ocurrences
# (0).

# Example 1:

# Input: nums = [2,2,1,1,5,3,3,5]
# Output: 7
# Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove
# nums[4]=5, we will get [2,2,1,1,3,3], so that each number will appear exactly
# twice.
 
# Example 2:

# Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
# Output: 13

# Example 3:

# Input: nums = [1,1,1,2,2,2]
# Output: 5

# Example 4:

# Input: nums = [10,2,8,9,3,8,1,5,2,3,7,6]
# Output: 8

# Constraints:

# 2 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5


# @lc code=start
from collections import defaultdict
class Solution:
    # cnt records the occurence of each num, freq records the frequence of number of occurences. max_F is the largest frequence.
    # There are three cases which satify the condition:
    # 1. all elements appear exact once.
    # 2. all elements appear max_F times, except one appears once.
    # 3. all elements appear max_F-1 times, except one appears max_F.
    def maxEqualFreq(self, nums:  [int]) -> int:
        count, freq, maxFreq, res = defaultdict(int), defaultdict(int), 0, 0
        for i,n in enumerate(nums):
            count[n] += 1
            freq[count[n]-1] -= 1
            freq[count[n]] += 1
            maxFreq = max(maxFreq, count[n])
            if maxFreq == 1 or (freq[maxFreq]*maxFreq == i and freq[1] == 1) or (freq[maxFreq-1]*(maxFreq-1) + maxFreq == i+1):
                res = i+1
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maxEqualFreq([1,1,1,2,2,2])
    s.maxEqualFreq([2,2,1,1,5,3,3,5])
    s.maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5])
