#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (38.07%)
# Likes:    981
# Dislikes: 47
# Total Accepted:    47.5K
# Total Submissions: 123.7K
# Testcase Example:  '[10,5,2,6]\n100'
#
# Your are given an array of positive integers nums.
# Count and print the number of (contiguous) subarrays where the product of all
# the elements in the subarray is less than k.
# 
# Example 1:
# 
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5],
# [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
# 
# 
# 
# Note:
# 0 < nums.length <= 50000
# 0 < nums[i] < 1000.
# 0 .


# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: [int], k: int) -> int:
        if not nums or k <= 1:
            return 0
        i, j, curr, res = 0, 0, nums[0], 0
        while j < len(nums):
            while j < len(nums) and curr < k:
                j += 1
                if j < len(nums):
                    curr *= nums[j]
            res += sum([i for i in range(1, j-i+1)])
            if j >= len(nums):
                return res
            else:  
                while curr >= k:              
                    curr /= nums[i]
                    i += 1
                res -= sum([i for i in range(1, j-i+1)])
        return res 
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.numSubarrayProductLessThanK([1,2,10, 5, 2, 6], 100)
    s.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
