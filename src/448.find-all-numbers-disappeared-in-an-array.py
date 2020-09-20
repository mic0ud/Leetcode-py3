#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (54.54%)
# Likes:    2157
# Dislikes: 199
# Total Accepted:    201.8K
# Total Submissions: 367.7K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
# 
# Find all the elements of [1, n] inclusive that do not appear in this array.
# 
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        for n in nums:
            i = abs(n)-1
            if nums[i] > 0:
                nums[i] = -nums[i]
        return [i for i in range(1, len(nums)+1) if nums[i-1] > 0]

    def findDisappearedNumbers_RECURSIVE(self, nums: [int]) -> [int]:
        def dfs(i):
            if i< 0 or nums[i-1] == -1:
                return
            tmp = nums[i-1]
            nums[i-1] = -1
            dfs(tmp)
        for n in nums:
            dfs(n)
        return [i for i in range(1, len(nums)+1) if nums[i-1] > 0]

    def findDisappearedNumbers_COUNTER(self, nums: [int]) -> [int]:
        c = Counter(nums)
        return [i for i in range(1, len(nums)+1) if c[i] == 0]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    # s.findDisappearedNumbers([2,2])
