#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
#
# algorithms
# Medium (37.45%)
# Likes:    337
# Dislikes: 7
# Total Accepted:    11.8K
# Total Submissions: 29K
# Testcase Example:  '[8,2,4,7]\r\n4\r'
#
# Given an array of integers nums and an integer limit, return the size of the
# longest continuous subarray such that the absolute difference between any two
# elements is less than or equal to limit.
# 
# In case there is no subarray satisfying the given condition return 0.
# 
# 
# Example 1:
# 
# 
# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute
# diff is |2-7| = 5 <= 5.
# 
# 
# Example 3:
# 
# 
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
# 
# 
#

# @lc code=start
import heapq
class Solution:
    def longestSubarray(self, nums: [int], limit: int) -> int:
        res, i, minq, maxq = 0, 0, [], []
        for j, n in enumerate(nums):
            heapq.heappush(minq, (n,j))
            heapq.heappush(maxq, (-n,j))
            if -maxq[0][0] - minq[0][0] > limit:
                i = min(minq[0][1], maxq[0][1]) + 1
                while minq[0][1] < i: heapq.heappop(minq)
                while maxq[0][1] < i: heapq.heappop(maxq)
            res = max(res, j-i+1)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.longestSubarray([10,1,2,4,7,2],0)
