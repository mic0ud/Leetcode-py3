#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#
# https://leetcode.com/problems/valid-triangle-number/description/
#
# algorithms
# Medium (46.72%)
# Likes:    818
# Dislikes: 86
# Total Accepted:    53.1K
# Total Submissions: 111.8K
# Testcase Example:  '[2,2,3,4]'
#
# Given an array consists of non-negative integers,  your task is to count the
# number of triplets chosen from the array that can make triangles if we take
# them as side lengths of a triangle.
# 
# Example 1:
# 
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# 
# 
# 
# Note:
# 
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].


# @lc code=start
from bisect import bisect_left
class Solution:
    def triangleNumber(self, nums: [int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        res = 0
        for i in range(n-1,1,-1):
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += r-l
                    r -= 1
                else:
                    l += 1
        return res

    def triangleNumber_SLOW(self, nums: [int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        res = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                idx = bisect_left(nums, nums[i]+nums[j])
                if idx > n-1:
                    res += n-1 - j
                elif idx > j:
                    res += (idx-1 if nums[idx] >= nums[i]+nums[j] else idx) - j
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.triangleNumber([1,2,2,2,3,4,4,8,10])
    s.triangleNumber([1,2,2,10])
    s.triangleNumber([0,0,0])
