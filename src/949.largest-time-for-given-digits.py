#
# @lc app=leetcode id=949 lang=python3
#
# [949] Largest Time for Given Digits
#
# https://leetcode.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Easy (34.59%)
# Likes:    104
# Dislikes: 262
# Total Accepted:    11.8K
# Total Submissions: 34K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array of 4 digits, return the largest 24 hour time that can be
# made.
# 
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from
# 00:00, a time is larger if more time has elapsed since midnight.
# 
# Return the answer as a string of length 5.  If no valid time can be made,
# return an empty string.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4]
# Output: "23:41"
# 
# 
# 
# Example 2:
# 
# 
# Input: [5,5,5,5]
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# A.length == 4
# 0 <= A[i] <= 9
# 
# 
# 
#

# @lc code=start
class Solution:
    def largestTimeFromDigits(self, A: [int]) -> str:
        p = self.generatePermutation(A)
        for item in p:
            if int(item) < 2400 and int(item[2:]) < 60:
                return item[:2] + ':' + item[2:]
        return ''
    
    # assume 0 <= nums[i] <= 9
    def generatePermutation(self, nums: [int]) -> [str]:
        dp = [None for i in range(len(nums) + 1)]
        dp[0] = []
        dp[1] =[str(nums[0])]
        for i in range(1, len(nums)):
            dp[i+1] = []
            for item in dp[i]:
                for j in range(len(item)+1):
                    newItem = (''if j == 0 else item[:j])+str(nums[i])+('' if j == len(item) else item[j:])
                    dp[i+1].append(newItem)
        return reversed(sorted(dp[-1]))
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.generatePermutation([1,2,3,4])
