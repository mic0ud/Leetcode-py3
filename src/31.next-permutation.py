#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (31.36%)
# Likes:    2400
# Dislikes: 791
# Total Accepted:    292K
# Total Submissions: 930.9K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
#   1. Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
#   2. Find the largest index l > k such that nums[k] < nums[l].
#   3. Swap nums[k] and nums[l].
#   4. Reverse the sub-array nums[k + 1:]
# @lc code=start
class Solution:
    # def nextPermutation(self, nums: List[int]) -> None:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i+1)

    def reverse(self, nums, start) -> None:
        i = start
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.nextPermutation([1,3,2])

