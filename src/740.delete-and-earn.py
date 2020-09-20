#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#
# https://leetcode.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (47.30%)
# Likes:    785
# Dislikes: 74
# Total Accepted:    31K
# Total Submissions: 64.8K
# Testcase Example:  '[3,4,2]'
#
# Given an array nums of integers, you can perform operations on the array.
# 
# In each operation, you pick any nums[i] and delete it to earn nums[i] points.
# After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.
# 
# You start with 0 points. Return the maximum number of points you can earn by
# applying such operations.
# 
# Example 1:
# 
# 
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation: 
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.

# Example 2:
# 
# 
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation: 
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
 
# Note:
# 
# 
# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].


# @lc code=start
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: [int]) -> int:
        if not nums:
            return 0
        maxNum = max(nums)
        # dp[i][0]: i deleted and earned, dp[i][1]: i deleted without earning
        count, dp, res = Counter(nums), [[0,0] for _ in range(maxNum+1)], 0
        for i in range(1, maxNum+1):
            if i not in count:
                dp[i] = dp[i-1]
            else:
                if i-1 in count:
                    dp[i][0] = dp[i-1][1] + i*count[i]
                    dp[i][1] = max(dp[i-1][0], max(dp[i-2]) if i>=2 else 0)                    
                else:
                    dp[i] = [res + i*count[i], res]
                res = max(res, max(dp[i]))
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.deleteAndEarn([2, 2, 3, 3, 3, 4,5,5,6,6,6,7])
    s.deleteAndEarn([3, 4, 2])
    s.deleteAndEarn([8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4])
