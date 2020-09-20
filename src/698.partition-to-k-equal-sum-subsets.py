#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (44.07%)
# Likes:    1172
# Dislikes: 66
# Total Accepted:    61.9K
# Total Submissions: 139.9K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
# 
# 
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: [int], k: int) -> bool:
        if not nums or k > len(nums) or k < 1:
            return False
        numsSum = sum(nums)
        nums.sort(reverse=True)
        if numsSum % k != 0:
            return False
        targets = [numsSum // k] * k
        if nums[0] > targets[0]:
            return False

        def dfs(p: int) -> bool:
            if p == len(nums):
                return True
            for i in range(k):
                if targets[i] >= nums[p]:
                    targets[i] -= nums[p]
                    if dfs(p+1):
                        return True
                    targets[i] += nums[p]
            return False

        return dfs(0)     
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.canPartitionKSubsets([2,2,2,2,3,4],3))
