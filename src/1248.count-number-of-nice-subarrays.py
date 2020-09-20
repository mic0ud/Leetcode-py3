#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#
# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
#
# algorithms
# Medium (52.82%)
# Likes:    184
# Dislikes: 5
# Total Accepted:    7.9K
# Total Submissions: 14.7K
# Testcase Example:  '[1,1,2,1,1]\n3'
#
# Given an array of integers nums and an integer k. A subarray is called nice
# if there are k odd numbers on it.
# 
# Return the number of nice sub-arrays.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and
# [1,2,1,1].
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.
# 
# 
# Example 3:
# 
# 
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length


# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: [int], k: int) -> int:
        idx = [-1]
        for i,n in enumerate(nums):
            if n % 2 > 0:
                idx.append(i)
        idx.append(len(nums))
        res = 0
        if len(idx) <= k+1:
            return res
        i = 1
        for j in range(k, len(idx)-1):
            res += (idx[i]-idx[i-1]) * (idx[j+1]-idx[j])
            i += 1
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2],2)
    s.numberOfSubarrays([1,1,2,1,1],3)
