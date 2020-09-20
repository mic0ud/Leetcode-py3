#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (32.83%)
# Likes:    2872
# Dislikes: 258
# Total Accepted:    348.6K
# Total Submissions: 1.1M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums: [int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        d= 0
        for i, x in enumerate(nums):
            if i > d:
                return False
            d = max(i+x, d)
            if d >= n - 1:
                return True
        return False        

    def canJump_SLOW(self, nums: [int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        if n == 1:
            return True
        d = nums[0]
        if d == 0:
            return False
        if d >= n - 1:
            return True
        for i in range(1, n-1):
            tmp = d
            for j in range(i, d+1):
                tmp = max(nums[j]+j, tmp)
                if tmp >= n-1:
                    return True
            if tmp == d:
                return False
            i = d
            d = tmp
        return False
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.canJump([1,2])
