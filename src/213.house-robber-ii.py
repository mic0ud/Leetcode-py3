#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (35.72%)
# Likes:    1188
# Dislikes: 40
# Total Accepted:    140.2K
# Total Submissions: 392.1K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
#

# @lc code=start
class Solution:
    def rob(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robHelper(nums[:-1]), self.robHelper(nums[1:]))
        # if not nums:
        #     return 0
        # dpSum = [0 for i in range(len(nums)+1)]
        # dpTake1st = [False for i in range(len(nums)+1)]
        # dpSum[0] = 0
        # dpSum[1] = nums[0]
        # dpTake1st[1] = True
        # for i in range(2, len(nums)+1):
        #     val1 = dpSum[i-2] + nums[i-1]
        #     val2 = dpSum[i-1]
        #     if val1 > val2:
        #         dpSum[i] = val1
        #         dpTake1st[i] = dpTake1st[i-2]
        #     elif val1 < val2:
        #         dpSum[i] = val2
        #         dpTake1st[i] = dpTake1st[i-1]
        #     else:
        #         dpSum[i] = val1
        #         dpTake1st[i] = False
        # if not dpTake1st[-1] or len(dpSum) == 2:
        #     return dpSum[-1]
        # else:
        #     v1 = dpSum[-1]
        #     v2 = dpSum[-2]
        #     v3 = self.robHelper(nums[1:])
        #     return max(v1-nums[0], v1-nums[-1], v2, v3)

    def robHelper(self, nums) -> int:
        if not nums:
            return 0
        dp = [0 for i in range(len(nums)+1)]
        dp[1] = nums[0]
        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        return dp[-1]

# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.rob([2,2,4,3,2,5])
