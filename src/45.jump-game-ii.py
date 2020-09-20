#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (29.20%)
# Likes:    1795
# Dislikes: 98
# Total Accepted:    217K
# Total Submissions: 735.4K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#

# @lc code=start
class Solution:
    # BFS
    def jump(self, nums: [int]) -> int:
        if not nums:
            return False
        n = len(nums)
        count, currEnd, currFarthest = 0, 0, 0
        for i in range(n-1):
            currFarthest = max(currFarthest, nums[i] + i)
            if i == currEnd:
                count += 1
                currEnd = currFarthest
        return count

    def jump_TLE(self, nums: [int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        dp = [float('inf') for _ in range(n)]
        dp[-1] = 0
        for i in range(n-2, -1, -1):
            if nums[i] + i >= n-1:
                dp[i] = 1
            else:
                tmp = min(dp[i+1:nums[i]+i+1])
                if tmp != float('inf'):
                    dp[i] = tmp + 1
        return dp[0]
# @lc code=end
# [3,2,1]
if __name__ == '__main__':
    s = Solution()
    s.jump([5,9,3,2,1,0,2,3,3,1,0,0])
