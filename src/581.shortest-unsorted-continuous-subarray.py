#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (30.57%)
# Likes:    1986
# Dislikes: 98
# Total Accepted:    94.2K
# Total Submissions: 307.6K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.  
# 
# You need to find the shortest such subarray and output its length.
# 
# Example 1:
# 
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# 
# 
# Note:
# 
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means . 
# 
# 
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        # find the maxVal from the left subArr and the minVal of the right subArr
        left, right = -1, -2 # right = -2 -> if the arr is sorted
        leftMax = nums[0]
        rightMin = nums[n-1]
        for i in range(1, n):
            leftMax = max(leftMax, nums[i])
            rightMin = min(rightMin, nums[n-1-i])
            if nums[i] < leftMax:
                right = i
            if nums[n-1-i] > rightMin:
                left = n-1-i
        return right - left + 1
                      
# @lc code=end
# [2,6,4,8,10,9,15]
if __name__ == '__main__':
    s = Solution()
    s.findUnsortedSubarray([2,6,4,8,10,9,15])
